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
    sol_num = 3
    
    # ranking parameters
    mu = 0.5
    e_m = 0.1
    
    # Key indicators
    kvis = KeyIndicatorList(names=kvi_names, aggregators=kvi_aggregators)
    kpis = KeyIndicatorList(names=kpi_names, aggregators=kpi_aggregators)
    
    # request model
    v = np.random.rand(len(kvis))
    # weights
    w = np.random.rand(len(kvis))
    
    # solution matrix
    s = Solution(kvis=kvis, kvi_aggregators=kvi_aggregators)
    
    # get the ranking of the solutions
    s.rank_solutions(v, w, mu, e_m)
        