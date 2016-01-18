from izh_curr_stochastic import model_binaries

def _init_module():
    import logging
    import os
    import spynnaker.pyNN
    spynnaker.pyNN.register_binary_search_path(os.path.dirname(model_binaries.__file__))

_init_module()
