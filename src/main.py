# author lucia pintor
import numpy as np
from classes.key_indicator_list import KeyIndicatorList
from classes.service import *
from classes.solution import Solution
  
if __name__ == "__main__":
    
    # kvis
    kvi_names = ["renewable_energy_percentage", "gender_equality_index", "workplace_quality", "inclusion_index"]
    kvi_aggregators = ["weighted_average", "min", "min", "min"]
    
    # kpis
    kpi_names = ["delay_time", "energy_consumption", "cost"]
    kpi_aggregators = ["average", "sum", "sum"]
    
    # number of solutions
    sol_num = 8
    
    # ranking parameters
    mu = 0.5
    e_m = 0.1
    
    # Key indicators
    kvis = KeyIndicatorList(names=kvi_names, aggregators=kvi_aggregators)
    kpis = KeyIndicatorList(names=kpi_names, aggregators=kpi_aggregators)
    
    # kvi request and weights
    v = np.array([0.8, 0.5, 0.5, 0.5])
    w = np.array([0.25, 0.25, 0.25, 0.25])
    
    # kpi minimal performance and weights
    p = np.array([0.1, 0.2, 0.3])
    l = np.array([0.1, 0.2, 0.3])
    
    # service instantiation
    streaming_service_1 = StreamingService(kvis=kvis, kvi_values=[0.1,0.1,0.1,0.1], kpis=kpis, kpi_values=[0.9,0.5,0.8])
    streaming_service_2 = StreamingService(kvis=kvis, kvi_values=[0.2,0.2,0.2,0.2], kpis=kpis, kpi_values=[0.9,0.5,0.8])
    renewable_energy_service_1 = RenewableEnergyService(kvis=kvis, kvi_values=[0.9,0.3,0.3,0.3], kpis=kpis, kpi_values=[0.1,0.2,0.3])
    renewable_energy_service_2 = RenewableEnergyService(kvis=kvis, kvi_values=[0.8,0.4,0.4,0.4], kpis=kpis, kpi_values=[0.1,0.2,0.3])
    
    # solution matrix
    solutions = [
        Solution(services=[streaming_service_1, renewable_energy_service_1]), 
        Solution(services=[streaming_service_1, renewable_energy_service_2]),
        Solution(services=[streaming_service_2, renewable_energy_service_1]),
        Solution(services=[streaming_service_2, renewable_energy_service_2]),
    ]
    
    # get the ranking of the solutions
    for i, s in enumerate(solutions):
        print(f"Solution {i+1} ranking: {
            s.rank_single_solution(kpi_minimal_performance=p, kpi_weights=l, kvi_request=v, kvi_weights=w, mu=mu, e_m=e_m)
            }")
        