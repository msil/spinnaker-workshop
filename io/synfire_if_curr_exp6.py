import pylab
import threading
import time

import pyNN.spiNNaker                         as p
import spynnaker_external_devices_plugin.pyNN as q

from spinnman.messages.eieio.eieio_header                                   import EIEIOHeader
from spinnman.messages.eieio.eieio_message                                  import EIEIOMessage
from spinnman.messages.eieio.eieio_type_param                               import EIEIOTypeParam
from spinnman.messages.eieio.eieio_prefix_type                              import EIEIOPrefixType
from spinnman.connections.udp_packet_connections.reverse_iptag_connection   import ReverseIPTagConnection

class SynFire( threading.Thread ):

    def __init__( self, time, num_neurons ):
        threading.Thread.__init__( self )

        p.setup( timestep=1.0, min_delay=1.0, max_delay=144.0 )

        self.time             = time
        self.num_neurons      = num_neurons
        self.loop_connections = list()
        self.weight_to_spike  = 2.0
        self.delay            = 17

        self.cell_params      = {
                'cm'        : 0.25,
                'i_offset'  : 0.0,
                'tau_m'     : 20.0,
                'tau_refrac': 2.0,
                'tau_syn_E' : 5.0,
                'tau_syn_I' : 5.0,
                'v_reset'   : -70.0,
                'v_rest'    : -65.0,
                'v_thresh'  : -50.0
        }

        self.injector_cell_params = {
            'host_port_number' : 12345,
            'host_ip_address'  : "localhost",
            'virtual_key'      : 458752,
            'prefix'           : 7,
            'prefix_type'      : q.EIEIOPrefixType.UPPER_HALF_WORD
        }
       
        for i in range( 0, self.num_neurons - 1 ):
            single_connection = ( i, ( ( i + 1 ) % self.num_neurons ), self.weight_to_spike, self.delay )
            self.loop_connections.append( single_connection )

        self.injection_connections = {
                'pop1' : [( 0, 0, self.weight_to_spike, 1 )],
                'pop2' : [( 1, 0, self.weight_to_spike, 1 )]
        }

        self.populations = {
        #       pop name                   num neurons       neuron type                    cell parameters            label
                "injector" : p.Population( 2,                q.ReverseIpTagMultiCastSource, self.injector_cell_params, label='spike_injector' ),
                "pop1"     : p.Population( self.num_neurons, p.IF_curr_exp,                 self.cell_params,          label='pop1'           ),
                "pop2"     : p.Population( self.num_neurons, p.IF_curr_exp,                 self.cell_params,          label='pop2'           ),
                "pop3"     : p.Population( self.num_neurons, p.IF_curr_exp,                 self.cell_params,          label='pop3'           )
        }

        self.projections = [
                p.Projection( self.populations['pop1'],      self.populations['pop1'], p.FromListConnector( self.loop_connections              ) ),
                p.Projection( self.populations['pop2'],      self.populations['pop2'], p.FromListConnector( self.loop_connections              ) ),
                p.Projection( self.populations['pop2'],      self.populations['pop3'], p.FromListConnector( self.loop_connections              ) ),
                p.Projection( self.populations['injector'],  self.populations['pop1'], p.FromListConnector( self.injection_connections['pop1'] ) ),
                p.Projection( self.populations['injector'],  self.populations['pop2'], p.FromListConnector( self.injection_connections['pop2'] ) )
        ]

    def plot_spikes( self, population, label ):
        spikes = population.getSpikes( compatible_output=True )
        if spikes is not None:
                pylab.figure()
                pylab.plot( [i[1] for i in spikes], [i[0] for i in spikes], "." )
                pylab.xlabel( 'Time/ms' )
                pylab.ylabel( 'spikes'  )
                pylab.title( 'spikes for %s' % label )
                pylab.show()
        else:
                print "No spikes received"

    def run( self ):
        print( "starting simulation. length: %d" % self.time )
        self.populations['pop1'].record()
        self.populations['pop2'].record()
        self.populations['pop3'].record()

        p.run( self.time )

        self.plot_spikes( populations['pop1'], "population 1" )
        self.plot_spikes( populations['pop2'], "population 2" )
        self.plot_spikes( populations['pop3'], "population 3" )


class SpikeInjector( threading.Thread ):

    def __init__( self, delay, remote_host='192.168.240.253', remote_port=12345 ):
        threading.Thread.__init__( self )
        self.delay          = delay
        self.remote_host    = remote_host
        self.remote_port    = remote_port
        self.udp_connection = ReverseIPTagConnection( remote_host=self.remote_host, remote_port=self.remote_port )
        self.header         = EIEIOHeader( type_param=EIEIOTypeParam.KEY_16_BIT, count_param=1 )
        self.message        = EIEIOMessage ( eieio_header = self.header, data=bytearray())

    def run( self ):
        import time

        print( "injector waiting..." )
        time.sleep( self.delay )

        self.message.write_key( 1 )

        print( "sending message..." )
        self.udp_connection.send_eieio_message( self.message )


thread_1 = SynFire( 15000, 100 )
thread_2 = SpikeInjector( 5 )

thread_1.start()
thread_2.start()

while 1:
    pass
