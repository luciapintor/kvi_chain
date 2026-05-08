import numpy as np

class Solution:
    """
    A solution is a service chain calculated given all the services available in the network.
    Each service has its own indicators that are used to rank the solution.
    """
    
    def __init__(self, services):
        
        self.services = services
        
        # cumulative indicators of the solution
        self.cumulative_services_kvi = self.calculate_cumulative_indicators(cumulate_kvis=True)
        self.cumulative_services_kpi = self.calculate_cumulative_indicators(cumulate_kvis=False)
        
    def calculate_cumulative_indicators(self, cumulate_kvis=True):
        # calculate the cumulative indicators of the solution as the aggregation of the indicators of the services in the solution
        
        cumulative_indicator_values = []
        
        if len(self.services) == 0:
            raise ValueError("The solution must have at least one service")
        
        if cumulate_kvis:
            # aggregate the kvis of the services in the solution
            indicator_names = self.services[0].kvis.names
            indicator_aggregators = self.services[0].kvis.aggregators
            indicator_values = np.array([s.kvi_values for s in self.services])
        else:
            # aggregate the kpis of the services in the solution
            indicator_names = self.services[0].kpis.names
            indicator_aggregators = self.services[0].kpis.aggregators
            indicator_values = np.array([s.kpi_values for s in self.services])
            
        for i in range(len(indicator_names)):
            if indicator_aggregators[i] == "average":
                cumulative_indicator_values.append(np.mean(indicator_values[:,i]))
            elif indicator_aggregators[i] == "weighted_average":
                cumulative_indicator_values.append(np.average(indicator_values[:,i])) #TODO: add weights to the average 
            elif indicator_aggregators[i] == "sum":
                cumulative_indicator_values.append(np.sum(indicator_values[:,i]))
            elif indicator_aggregators[i] == "min":
                cumulative_indicator_values.append(np.min(indicator_values[:,i]))
            elif indicator_aggregators[i] == "max":
                cumulative_indicator_values.append(np.max(indicator_values[:,i]))
            else:
                raise ValueError(f"Invalid aggregation method: {indicator_aggregators[i]}")
        
        return cumulative_indicator_values          
            
    def calculate_kpi_performance(self, kpi_minimal_performance, kpi_weights):
        # calculate the performance of the solution for each kpi given 
        # the minimal performance required for each kpi and the weights of each kpi in the ranking of the solution
        s_performance = []
        
        for i in range(len(self.cumulative_services_kpi)):
            performance = max(0.0, (kpi_minimal_performance[i] - self.cumulative_services_kpi[i])/ kpi_minimal_performance[i])
            s_performance.append(performance * kpi_weights[i])
        
        return sum(s_performance)

    def rank_single_solution(self, kpi_minimal_performance, kpi_weights, kvi_request, kvi_weights, mu=0.5):
        """
        The ranking is calculated for each solution s_m through a sigmoid function of
        the summatory of the difference between the kvi request and the cumulative kvi of the solution, 
        weighted by the kvi weights, and the performance of the solution for each kpi, weighted by the kpi weights.
        """
        
        s_performance = self.calculate_kpi_performance(kpi_minimal_performance, kpi_weights)
        
        score = 0.0
        
        for n in range(len(kvi_request)):
            score += (kvi_request[n] - self.cumulative_services_kvi[n]) * kvi_weights[n]
            
        self.s_value = (1 - mu) * score + mu * s_performance
        
        return self.s_value