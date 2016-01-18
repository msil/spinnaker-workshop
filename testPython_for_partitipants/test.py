"""
Synfirechain-like example
"""
#import pyNN.spiNNaker as p
import pylab

import spynnaker.pyNN as p
from izh_curr_stochastic.izhikevich_current_exponential_stochastic_population \
    import IzhikevichCurrentExponentialStochasticPopulation

stochastic = True
p.setup(timestep=1.0, min_delay=1.0, max_delay=32.0)
p.set_number_of_neurons_per_core("IZK_curr_exp", 100)
nNeurons = 100  # number of neurons in each population

if stochastic:
    pass
else:
    cell_params_izk = {'a': 0.02,
                       'b': 0.20,
                       'c': -65.0,
                       'd': 8.0,
                       'v_init': -75.0,
                       'u_init': 0.0,
                       'tau_syn_E': 5.0,
                       'tau_syn_I': 5.0,
                       'i_offset': 0.0}

populations = list()
projections = list()

weight_to_spike = 6.5
delay = 1

spike_list = []
for spike in range(0, 100):
    spike_list.append(spike * 5)
print spike_list
spikeArray = {'spike_times': spike_list}

if stochastic:
    pass
else:
    populations.append(p.Population(nNeurons, p.IZK_curr_exp,
                                    cell_params_izk, label='pop_1'))

populations.append(p.Population(1, p.SpikeSourceArray, spikeArray,
                                label='inputSpikes_1'))

projections.append(p.Projection(populations[1], populations[0],
                                p.AllToAllConnector(weights=weight_to_spike,
                                                    delays=delay)))

populations[0].record()

p.run(500)

spikes = None

spikes = populations[0].getSpikes(compatible_output=True)
if len(spikes) != 0:
    pylab.figure()
    pylab.plot([i[1] for i in spikes], [i[0] for i in spikes], ".")
    pylab.xlabel('Time/ms')
    pylab.xticks([0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500])
    pylab.ylabel('spikes')
    pylab.title('spikes')
    pylab.show()
else:
    print "No spikes received"
p.end()

