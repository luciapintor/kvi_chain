import numpy as np

class Solution:
    def __init__(self, kvis, kvi_aggregators):
        self.kvis = kvis
        self.kvi_aggregators = kvi_aggregators
        
        self.sol_num = 6
        self.s = np.random.rand(self.sol_num, len(kvis))
        
    def __iter__(self):
        for i in range(self.sol_num):
            yield self.s[i]

    def __rank_single_solution(self, v, w, s_m, mu=0.5, e_m=0.1):
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
    
    def rank_solutions(self, v, w, mu=0.5, e_m=0.1):
        """
        This method ranks all the calculated solutions

        Args:
            v (_type_): _description_
            w (_type_): _description_
            mu (float, optional): _description_. Defaults to 0.5.
            e_m (float, optional): _description_. Defaults to 0.1.

        Returns:
            _type_: _description_
        """
        
        ranking = []
        
        for i, s_m in enumerate(self):
            ranking.append(self.__rank_single_solution(v, w, s_m, mu, e_m))
            print(f"Ranking of solution {i}: {ranking[-1]}")
        return ranking
    