# author lucia pintor
import numpy as np

def rank_solutions(v,w,s_m, mu=0.5, e_m=0.1):
    """
    The ranking is calculated for each solution s_m through a sigmoid function of
    the summatory of the difference between v_n and s_mn multiplied by w_n.

    Args:
        v (_type_): is an array of values for each kvi, where v_n is the value of the n-th kvi.
        w (_type_): is an array of weights for each kvi, where w_n is the weight of the n-th kvi.
        s_m (_type_): is an array of solutions, where s_mn is the value of the n-th kvi in the m-th solution.
        mu (float, optional): is a parameter to balance the sustanability and the performance of the solution. 
        e_m (float, optional): is a cost parameter to take in account performance degradation and cost increase
    """
    
    ranking = []
    for s_n in s_m:
        score = 0
        for n in range(len(v)):
            score += w[n] * (v[n] - s_n)
        ranking.append(1/(1+np.exp(-mu*score + e_m)))
        
    # now sum up the ranking and get the final value 
    return (1 - mu) * sum(ranking) + mu * e_m
    
    
    

if __name__ == "__main__":
    
    # number of kvis
    kvi_num = 4
    # number of solutions
    sol_num = 3
    
    # request model
    v = np.random.rand(kvi_num)
    # weights
    w = np.random.rand(kvi_num)
    
    # solution matrix
    s = np.random.rand(sol_num, kvi_num)
    
    # get the ranking of the solutions
    ranking = []
    for i in range(sol_num):
        ranking.append(rank_solutions(v,w,s[i]))
        print(f"Ranking of solution {i}: {ranking[-1]}")
        