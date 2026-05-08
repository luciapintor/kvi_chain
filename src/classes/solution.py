import numpy as np

class Solution:
    """
    A solution is a service chain calculated given all the services available in the network.
    Each service has its own indicators that are used to rank the solution.
    """
    
    def __init__(self, services, kvi_request, kvi_weights, kpi_minimal_performance, kpi_weights):
        
        self.services = services
        
        # requests and weights for the ranking
        self.kvi_request = kvi_request
        self.kvi_weights = kvi_weights
        self.kpi_minimal_performance = kpi_minimal_performance
        self.kpi_weights = kpi_weights
        
        # cumulative indicators of the solution
        self.services_kvi = np.random.rand(len(services[0].kvis)) # todo: this should be calculated as the aggregation of the kvis of the services in the solution
        self.services_kpi = np.random.rand(len(services[0].kpis)) # todo: this should be calculated as the aggregation of the kpis of the services in the solution    
        
        # calculate the ranking of the solution
        self.s_performance = self.calculate_kpi_performance()
        
    def calculate_cumulative_indicators(self):
        # calculate the cumulative indicators of the solution as the aggregation of the indicators of the services in the solution
        pass
    
    def calculate_kpi_performance(self):
        # calculate the performance of the solution for each kpi
        pass
    
    def rank_single_solution(self, mu=0.5, e_m=0.0):
        """
        The ranking is calculated for each solution s_m through a sigmoid function of
        the summatory of the difference between v_n and s_mn multiplied by w_n.

        Args:
            mu (float, optional): is a parameter to balance the sustanability and the performance of the solution. 
            e_m (float, optional): is a cost parameter to take in account performance degradation and cost increase
        """
        
        score = 0.0
        
        for n in range(len(self.kvi_request)):
            score += (self.kvi_request[n] - self.services_kvi[n]) * self.kvi_weights[n]
            
        self.s_value = (1 - mu) * score + mu * e_m
        
        return self.s_value