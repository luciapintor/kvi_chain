# author lucia pintor
import numpy as np
from classes.solution import Solution
  
if __name__ == "__main__":
    
    # kvis
    kvis = ["renewable_energy_percentage", "gender_equality_index", "workplace_quality", "inclusion_index"]
    kvi_num = len(kvis)
    kvi_aggregators = ["weighted_average", "min", "min", "min"]
    
    # number of solutions
    sol_num = 3
    
    # ranking parameters
    mu = 0.5
    e_m = 0.1
    
    # request model
    v = np.random.rand(kvi_num)
    # weights
    w = np.random.rand(kvi_num)
    
    # solution matrix
    s = Solution(kvis, kvi_aggregators)
    
    # get the ranking of the solutions
    s.rank_solutions(v, w, mu, e_m)
        