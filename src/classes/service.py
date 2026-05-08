import numpy as np

class Service:
    def __init__(self, kvis, kvi_values, kpis, kpi_values, e):
        self.kvis = kvis
        self.kvi_values = kvi_values
        self.kpis = kpis
        self.kpi_values = kpi_values
        self.e = e

class StreamingService(Service):
    def __init__(self, kvis, kvi_values, kpis, kpi_values, e):
        super().__init__(kvis, kvi_values, kpis, kpi_values, e)

class RenewableEnergyService(Service):
    def __init__(self, kvis, kvi_values, kpis, kpi_values, e):
        super().__init__(kvis, kvi_values, kpis, kpi_values, e)

class GenderEqualityService(Service):
    def __init__(self, kvis, kvi_values, kpis, kpi_values, e):
        super().__init__(kvis, kvi_values, kpis, kpi_values, e)

class WorkplaceService(Service):
    def __init__(self, kvis, kvi_values, kpis, kpi_values, e):
        super().__init__(kvis, kvi_values, kpis, kpi_values, e)

class InclusionService(Service):
    def __init__(self, kvis, kvi_values, kpis, kpi_values, e):
        super().__init__(kvis, kvi_values, kpis, kpi_values, e)