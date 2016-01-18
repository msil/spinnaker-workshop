"""
Synfirechain-like example
"""
import pyNN.spiNNaker as p
import pylab
import spynnaker_external_devices_plugin.pyNN as q

p.setup(timestep=1.0, min_delay=1.0, max_delay=144.0)
nNeurons = 20  # number of neurons in each population
#p.set_number_of_neurons_per_core("IF_curr_exp", nNeurons)

#
# set up to receive input from inject_input.py
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
for i in range(0, nNeurons-1):
    singleConnection = (i, ((i + 1) % nNeurons), weight_to_spike, delay)
    loopConnections.append(singleConnection)

injectionConnection = [(0, 0, weight_to_spike, 1)]
#spikeArray = {'spike_times': [[0]]}
populations.append(p.Population(nNeurons, p.IF_curr_exp, cell_params_lif,
                   label='pop_1'))

#populations.append(p.Population(1, p.SpikeSourceArray, spikeArray,
#                   label='inputSpikes_1'))

cell_params_spike_injector_with_prefix1 = {
	'host_port_number':12345,
	'host_ip_address' : "localhost",
	#'virtual_key': 458752,
	'virtual_key': 458752,
	'prefix':7,
	'prefix_type': q.EIEIOPrefixType.UPPER_HALF_WORD}

cell_params_spike_injector_with_prefix2 = {
	'host_port_number':12346,
	'host_ip_address' : "localhost",
	'virtual_key': 196608,
	'prefix':3,
	'prefix_type': q.EIEIOPrefixType.UPPER_HALF_WORD}


 #injectgor
populations.append(p.Population(1, q.ReverseIpTagMultiCastSource, cell_params_spike_injector_with_prefix1, label='spike_injector1'))

populations.append(p.Population(nNeurons, p.IF_curr_exp, cell_params_lif,
                   label='pop_2'))

populations.append(p.Population(1, q.ReverseIpTagMultiCastSource, cell_params_spike_injector_with_prefix2, label='spike_injector2'))

#populations.append(p.Population(1, p.SpikeSourceArray, spikeArray,
#                  label='inputSpikes_1'))

projections.append(p.Projection(populations[0], populations[0],
                   p.FromListConnector(loopConnections)))

projections.append(p.Projection(populations[1], populations[0],
                   p.FromListConnector(injectionConnection)))


projections.append(p.Projection(populations[2], populations[2],
                   p.FromListConnector(loopConnections)))

projections.append(p.Projection(populations[3], populations[2],
                   p.FromListConnector(injectionConnection)))

#populations[0].record_v()
#populations[0].record_gsyn()
populations[0].record()
populations[2].record()
 
def plotSpikes(spikes, pop):
	if spikes is not None:
		print spikes
    		pylab.figure()
    		pylab.plot([i[1] for i in spikes], [i[0] for i in spikes], ".")
    		pylab.xlabel('Time/ms')
    		pylab.ylabel('spikes')
    		pylab.title('spikes for Population %d' %pop)
    		pylab.show()
	else:
    		print "No spikes received"


p.run(10000)
spikes1 = populations[0].getSpikes(compatible_output=True)
spikes2 = populations[2].getSpikes(compatible_output=True)
plotSpikes(spikes1,0)
plotSpikes(spikes2,2)


# p.end()
