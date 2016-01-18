#import pyNN.spiNNaker as p
import spynnaker.pyNN as p
import spynnaker_external_devices_plugin.pyNN as q

import numpy
import pylab

from pprint import pprint


delay        = 1.0
sim_length   = 100
num_neurons  = 100
spike_weight = 2.0
delay        = 17

p.setup( 
        timestep=1.0, 
        min_delay=1.0,
        max_delay=100.0,
        debug=True
        )

cell_params = {'cm': 0.25,
                   'i_offset': 0.0,
                   'tau_m': 20.0,
                   'tau_refrac': 2.0,
                   'tau_syn_E': 5.0,
                   'tau_syn_I': 5.0,
                   'v_reset': -70.0,
                   'v_rest': -65.0,
                   'v_thresh': -50.0
                   }

cell_params_spike_injector_with_prefix = {
        'host_port_number'  : 12345,
        'host_ip_address'   : "localhost",
        'virtual_key'       : 458752,
        'prefix'            : 7,
        'prefix_type'       : q.EIEIOPrefixType.UPPER_HALF_WORD
        }

populations = list()
projections = list()

pop_1 = p.Population(
        1, 
        p.SpikeSourceArray, 
        { 'spike_times': [[0]] }, 
        label='input_spike')

#pop_1 = p.Population(
#        1,
#        q.ReverseIpTagMultiCastSource,
#        cell_params_spike_injector_with_prefix,
#        label='spike_injector_1'
#        )

pop_2 = p.Population(
        num_neurons, 
        p.IF_curr_exp, 
        cell_params, 
        label='pop_2'
        )

populations.append(pop_1)
populations.append(pop_2)

connections = list()
for i in range(0, num_neurons):
    conn = (i, ((i + 1) % num_neurons), spike_weight, delay)
    connections.append(conn)

conn_list = [(0, 0, spike_weight, delay)]
    
proj_1 = p.Projection(populations[0], populations[1],
        p.FromListConnector(conn_list))

proj_1 = p.Projection(populations[1], populations[1],
        p.FromListConnector(connections))

populations[1].record()

p.run(500)
spikes = populations[1].getSpikes()
pprint(populations[1].getSpikes())

#pylab.figure()
#pylab.plot( [i[0] for i in spikes], [i[1] for i in spikes], ".")
#pylab.xlabel("neuronid")
#pylab.ylabel("spiketime")
#pylab.show()


