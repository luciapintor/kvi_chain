import numpy as np

class Solution:
    """
    A solution is a service chain calculated given all the services available in the network.
    Each service has its own indicators that are used to rank the solution.
    """
    
    def __init__(self, services):
        
        self.services = services
        self.kvis = services[0].kvis # we assume all the services in the solution have the same kvis
        
        # cumulative indicators of the solution
        self.chain_kvis = self.get_chain_kvis()
        
    def get_chain_kvis(self):
        # calculate the cumulative indicators of the solution as the aggregation of the indicators of the services in the solution
        
        chain_kvis = []
        
        if len(self.services) == 0:
            raise ValueError("The solution must have at least one service")
        
        # pivoting the kvi values of the services
        services_kvis = np.matrix([s.kvi_values for s in self.services])
        
        for i in range(len(self.kvis.aggregators)):
            if self.kvis.aggregators[i] == "average":
                chain_kvis.append(np.mean(services_kvis[:,i]))
            elif self.kvis.aggregators[i] == "weighted_average":
                chain_kvis.append(np.average(services_kvis[:,i])) #TODO: add weights to the average 
            elif self.kvis.aggregators[i] == "sum":
                chain_kvis.append(np.sum(services_kvis[:,i]))
            elif self.kvis.aggregators[i] == "min":
                chain_kvis.append(np.min(services_kvis[:,i]))
            elif self.kvis.aggregators[i] == "max":
                chain_kvis.append(np.max(services_kvis[:,i]))
            else:
                raise ValueError(f"Invalid aggregation method: {self.kvis.aggregators[i]}")
            
            # TODO: manage case of min and max because we are assuming the threshold is the minimum value to reach,
            # but for some indicators the threshold is the maximum value to reach (e.g. delay time, energy consumption, cost)
        
        return chain_kvis          
            
    def calculate_chain_cost(self):
        """
        The cost of the solution is calculated as the sum of the costs of the services in the solution.
        """
        chain_cost = 0.0
        
        for s in self.services:
            chain_cost += s.cost
        
        return chain_cost

    def rank_single_solution(self, kvi_request, kvi_weights, mu=0.5):
        """
        The ranking is calculated for each solution s_m through a sigmoid function of
        the summatory of the difference between the kvi request and the kvi of the solution chain, 
        weighted by the kvi weights. The economic cost of the solution is balanced with the parameter mu.
        """
        
        s_cost = self.calculate_chain_cost()
        
        score = 0.0
        
        for n in range(len(kvi_request)):
            score += (kvi_request[n] - self.chain_kvis[n]) * kvi_weights[n]
            
        self.s_value = (1 - mu) * score + mu * s_cost
        
        return self.s_value