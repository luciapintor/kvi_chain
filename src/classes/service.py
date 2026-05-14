import numpy as np

class Service:
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
            raise ValueError("The number of kvi values must be equal to the number of kvis")
        if isinstance(values, list):
            values = np.array(values)
        self._kvi_values = values

class StreamingService(Service):
    def __init__(self, kvis, kvi_values, cost):
        super().__init__(kvis, kvi_values, cost)

class RenewableEnergyService(Service):
    def __init__(self, kvis, kvi_values, cost):
        super().__init__(kvis, kvi_values, cost)

class GenderEqualityService(Service):
    def __init__(self, kvis, kvi_values, cost):
        super().__init__(kvis, kvi_values, cost)

class WorkplaceService(Service):
    def __init__(self, kvis, kvi_values, cost):
        super().__init__(kvis, kvi_values, cost)

class InclusionService(Service):
    def __init__(self, kvis, kvi_values, cost):
        super().__init__(kvis, kvi_values, cost)