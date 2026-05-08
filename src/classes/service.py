import numpy as np

class Service:
    def __init__(self, kvis, kvi_values, kpis, kpi_values):
        self.kvis = kvis
        self.kvi_values = kvi_values
        self.kpis = kpis
        self.kpi_values = kpi_values
    
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
    
    @property
    def kpi_values(self):
        return self._kpi_values
    
    @kpi_values.setter
    def kpi_values(self, values):   
        if len(values) != len(self.kpis):
            raise ValueError("The number of kpi values must be equal to the number of kpis")
        if isinstance(values, list):
            values = np.array(values)
        self._kpi_values = values

class StreamingService(Service):
    def __init__(self, kvis, kvi_values, kpis, kpi_values):
        super().__init__(kvis, kvi_values, kpis, kpi_values)

class RenewableEnergyService(Service):
    def __init__(self, kvis, kvi_values, kpis, kpi_values):
        super().__init__(kvis, kvi_values, kpis, kpi_values)

class GenderEqualityService(Service):
    def __init__(self, kvis, kvi_values, kpis, kpi_values):
        super().__init__(kvis, kvi_values, kpis, kpi_values)

class WorkplaceService(Service):
    def __init__(self, kvis, kvi_values, kpis, kpi_values):
        super().__init__(kvis, kvi_values, kpis, kpi_values)

class InclusionService(Service):
    def __init__(self, kvis, kvi_values, kpis, kpi_values):
        super().__init__(kvis, kvi_values, kpis, kpi_values)