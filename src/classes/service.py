import numpy as np

class Service:
    def __init__(self, kvis, kvi_values, e_i):
        self.kvis = kvis
        self.kvi_values = kvi_values
        self.e_i = e_i

class StreamingService(Service):
    def __init__(self, kvis, kvi_values, e_i):
        super().__init__(kvis, kvi_values, e_i)
        
class RenewableEnergyService(Service):
    def __init__(self, kvis, kvi_values, e_i):
        super().__init__(kvis, kvi_values, e_i)

class GenderEqualityService(Service):
    def __init__(self, kvis, kvi_values, e_i):
        super().__init__(kvis, kvi_values, e_i)
        
class WorkplaceService(Service):
    def __init__(self, kvis, kvi_values, e_i):
        super().__init__(kvis, kvi_values, e_i)
        
class InclusionService(Service):
    def __init__(self, kvis, kvi_values, e_i):
        super().__init__(kvis, kvi_values, e_i)