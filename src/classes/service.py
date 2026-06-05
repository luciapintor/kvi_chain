import numpy as np


class Service:
    """
    A single service function in a chain.
    
    kvis         : KeyIndicatorList shared across all services
    kvi_values   : list/array of KVI contributions for this function
    cost         : normalised operational cost in [0, 1]
    """

    def __init__(self, kvis, kvi_values, cost):
        self.kvis = kvis
        self.kvi_values = kvi_values
        self.cost = cost

    @property
    def kvi_values(self):
        return self._kvi_values

    @kvi_values.setter
    def kvi_values(self, values):
        if len(values) != len(self.kvis):
            raise ValueError(
                "The number of kvi values must be equal to the number of kvis"
            )
        if isinstance(values, list):
            values = np.array(values, dtype=float)
        self._kvi_values = values