

#ifndef _IZH_CURR_NEURON_
#define _IZH_CURR_NEURON_


#include  "neuron/models/generic_neuron.h"


typedef struct neuron_t {

// nominally 'fixed' parameters
	REAL 		A;
	REAL 		B;
	REAL 		C;			
	REAL		D;

// Variable-state parameters
	REAL 		V;
	REAL 		U;
	
// offset current [nA]
	REAL		I_offset;

// anything from here onwards is private to the c code (non neural parameters)
// current timestep - simple correction for threshold in beta version	
	REAL		this_h;

	
} neuron_t;


//
neuron_pointer_t create_izh_neuron( REAL A, REAL B, REAL C, REAL D, REAL V, REAL U, REAL I );

													
#endif   // include guard

