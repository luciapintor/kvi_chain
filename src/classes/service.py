import numpy as np


class Service:
    """
    A single service function in a chain.
    
    kvis         : KeyIndicatorList shared across all services
    kvi_values   : list/array of KVI contributions for this function
    cost         : normalised operational cost in [0, 1]
    resource_weight : pm,i — share of chain resources used by this function.
                      Used by the weighted_average aggregator (eq. 11 of the paper).
                      Must be set consistently across all services in a chain so
                      that the weights sum to 1 within each chain.
    """

    def __init__(self, kvis, kvi_values, cost, resource_weight=None):
        self.kvis = kvis
        self.kvi_values = kvi_values
        self.cost = cost
        self.resource_weight = resource_weight  # pm,i

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


class StreamingService(Service):
    def __init__(self, kvis, kvi_values, cost, resource_weight=None):
        super().__init__(kvis, kvi_values, cost, resource_weight)


class RenewableEnergyService(Service):
    def __init__(self, kvis, kvi_values, cost, resource_weight=None):
        super().__init__(kvis, kvi_values, cost, resource_weight)


class GenderEqualityService(Service):
    def __init__(self, kvis, kvi_values, cost, resource_weight=None):
        super().__init__(kvis, kvi_values, cost, resource_weight)


class WorkplaceService(Service):
    def __init__(self, kvis, kvi_values, cost, resource_weight=None):
        super().__init__(kvis, kvi_values, cost, resource_weight)


class InclusionService(Service):
    def __init__(self, kvis, kvi_values, cost, resource_weight=None):
        super().__init__(kvis, kvi_values, cost, resource_weight)