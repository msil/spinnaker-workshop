"""
Synfirechain-like example
"""
import pyNN.spiNNaker as p
import pylab
#import spynnaker_external_devices_plugin.pyNN as q

p.setup(timestep=1.0, min_delay=1.0, max_delay=144.0)
nNeurons = 200  # number of neurons in each population
#p.set_number_of_neurons_per_core("IF_curr_exp", nNeurons/16)

#
#set up and export spikes to be captured by receiver_output.py
#

cell_params_lif = {'cm': 0.25,
                   'i_offset': 0.0,
                   'tau_m': 20.0,
                   'tau_refrac': 2.0,
                   'tau_syn_E': 5.0,
                   'tau_syn_I': 5.0,
                   'v_reset': -70.0,
                   'v_rest': -65.0,
                   'v_thresh': -50.0
                   }

populations = list()
projections = list()

weight_to_spike = 2.0
delay = 17

loopConnections = list()
for i in range(0, nNeurons):
    singleConnection = (i, ((i + 1) % nNeurons), weight_to_spike, delay)
    loopConnections.append(singleConnection)

injectionConnection = [(0, 0, weight_to_spike, 1)]
spikeArray = {'spike_times': [[0]]}
populations.append(p.Population(nNeurons, p.IF_curr_exp, cell_params_lif,
                   label='pop_1'))

#populations.append(p.Population(1, p.SpikeSourceArray, spikeArray,
#                   label='inputSpikes_1'))

#cell_params_spike_injector_with_prefix = {
#	'host_port_number':12345,
#	'host_ip_address' : "localhost",
#	'virtual_key': 458752,
#	'prefix':7,
#	'prefix_type': q.EIEIOPrefixType.UPPER_HALF_WORD}

 #injectgor
#populations.append(p.Population(1, q.ReverseIpTagMultiCastSource, cell_params_spike_injector_with_prefix, label='spike_injector1'))

populations.append(p.Population(1, p.SpikeSourceArray, spikeArray,
                   label='inputSpikes_1'))

projections.append(p.Projection(populations[0], populations[0],
                   p.FromListConnector(loopConnections)))
projections.append(p.Projection(populations[1], populations[0],
                   p.FromListConnector(injectionConnection)))

#populations[0].record_v()
#populations[0].record_gsyn()
#populations[0].record()

portNo=18250
hostname="192.168.240.254" #ipaddress of packets to be sent to
strip_sdp=True



#p.activate_live_output_for(populations[0], portNo, hostname,  tag, strip_sdp, use_prefix, right_shift,
#				payload_as_time_stamps, use_payload_prefix, 
#				payload_prefix, payload_right_shift,
#				number_of_packets_sent_per_time_step)



p.activate_live_output_for(populations[0], portNo, hostname,tag=1,  strip_sdp=strip_sdp)



#populations[0].set_constraint( p.PartitionerMaximumSizeConstraint(5))
# 4 chips addressed (0,0) (0,1) (1,0) (1,1) so (2,2) out of range
#populations[0].set_mapping_constraint({'x':2, 'y':2, 'p':0})
#However (1,1) should work, but doesn't?
#populations[0].set_mapping_constraint({'x':1, 'y':1, 'p':0})

#same problem as above
#populations[0].set_constraint( p.PlacerChipAndCoreConstraint(2,2,0))

#populations[0].set_constraint( p.PlacerChipAndCoreConstraint(0,0,0))

p.run(400)

# p.end()
