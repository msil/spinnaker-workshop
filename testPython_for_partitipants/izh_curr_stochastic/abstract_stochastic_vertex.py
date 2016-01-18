from abc import ABCMeta
from six import add_metaclass
from abc import abstractmethod


@add_metaclass(ABCMeta)
class AbstractStochasticVertex(object):

    # noinspection PyPep8Naming
    def __init__(self, membrane_noise_sd):
        self._membrane_noise_sd = membrane_noise_sd

    @abstractmethod
    def is_stochastic(self):
        """
        helper method for is instance
        :return:
        """
