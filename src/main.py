# author lucia pintor
import numpy as np
from classes.kvi import KVI
from classes.solution import Solution
  
if __name__ == "__main__":
    
    # kvis
    kvi_names = ["renewable_energy_percentage", "gender_equality_index", "workplace_quality", "inclusion_index"]
    kvi_aggregators = ["weighted_average", "min", "min", "min"]
    
    # number of solutions
    sol_num = 3
    
    # ranking parameters
    mu = 0.5
    e_m = 0.1
    
    # KVIS
    kvis = KVI(kvi_names=kvi_names, kvi_aggregators=kvi_aggregators)
    
    # request model
    v = np.random.rand(len(kvis))
    # weights
    w = np.random.rand(len(kvis))
    
    # solution matrix
    s = Solution(kvis=kvis)
    
    # get the ranking of the solutions
    s.rank_solutions(v, w, mu, e_m)
        