APP = izh_curr_stochastic
NEURAL_MODELLING_DIRS=/home/micky/src/spinnaker/sPyNNaker-2015.001/neural_modelling
EXTRA_SRC_DIR = $(CURDIR)/../
SOURCE_DIR = $(NEURAL_MODELLING_DIRS)/src/neuron
MODEL_OBJS = izh_curr_stochastic.o $(SOURCE_DIR)/static_synapses.o
NEURON_MODEL_H = izh_curr_stochastic.h
SYNAPSE_SHAPING_H = $(NEURAL_MODELLING_DIRS)/src/neuron/synapses/exponential_impl.h
CFLAGS=-I.
CFLAGS+= -I$(NEURAL_MODELLING_DIRS)/src
APP_OUTPUT_DIR = $(CURDIR)
include $(NEURAL_MODELLING_DIRS)/src/neuron/builds/Makefile.common
