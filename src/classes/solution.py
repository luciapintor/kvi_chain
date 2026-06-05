import numpy as np

class Solution:
    """
    A candidate service chain composed of an ordered sequence of Service objects.
 
    The chain KVI vector is computed by aggregating each service function's
    contribution according to the operator defined in KeyIndicatorList:
      - weighted_average : uses per-service resource_weight (pm,i) — eq. 11
      - min              : worst-link criterion — eq. 12
      - average          : uniform mean
      - sum              : additive
      - max              : best-link
 
    The ranking score follows eq. 10 of the paper:
      R(Sm) = (1 - mu) * sigmoid( sum_n (vn - sm,n) * wn ) + mu * Em
    where Em is the normalised chain cost.
    A lower score is better (sigmoid near 0 means sm,n >= vn for all n).
    """
    
    def __init__(self, services, resource_weights=None):
        if len(services) == 0:
            raise ValueError("A solution must contain at least one service.")
        self.services = services
        self.kvis = services[0].kvis # we assume all the services in the solution have the same kvis
        self.chain_kvis = self._compute_chain_kvis(resource_weights)
     
    # ------------------------------------------------------------------
    # Chain KVI aggregation
    # ------------------------------------------------------------------
 
    def _compute_chain_kvis(self, resource_weights=None):
        # Matrix: rows = services, cols = KVI indices
        kvi_matrix = np.array([s.kvi_values for s in self.services], dtype=float)
 
        chain_kvis = []
        for i, (name, aggregator) in enumerate(self.kvis):
            col = kvi_matrix[:, i]
 
            if aggregator == "weighted_average":
                weights = resource_weights 
                chain_kvis.append(float(np.average(col, weights=weights)))
 
            elif aggregator == "average":
                chain_kvis.append(float(np.mean(col)))
 
            elif aggregator == "sum":
                chain_kvis.append(float(np.sum(col)))
 
            elif aggregator == "min":
                chain_kvis.append(float(np.min(col)))
 
            elif aggregator == "max":
                chain_kvis.append(float(np.max(col)))
 
            else:
                raise ValueError(f"Unknown aggregation method: '{aggregator}'")
            
            # TODO: manage case of min and max because we are assuming the threshold is the minimum value to reach,
            # but for some indicators the threshold is the maximum value to reach (e.g. delay time, energy consumption, cost)
 
        return np.array(chain_kvis)      
    
    def _get_resource_weights(self):
        """
        Extract pm,i weights from each service.
        If resource_weight is not set, fall back to uniform weights.
        Weights are normalised so they sum to 1.
        """
        weights = np.array(
            [
                s.resource_weight if s.resource_weight is not None else 1.0
                for s in self.services
            ],
            dtype=float,
        )
        total = weights.sum()
        if total == 0:
            raise ValueError("Sum of resource weights is zero.")
        return weights / total
 
    # ------------------------------------------------------------------
    # Cost
    # ------------------------------------------------------------------
    def calculate_chain_cost(self):
        """
        Normalised chain cost: average of per-service costs so that
        longer chains are not automatically penalised more than shorter ones.
        Cost is assumed to be in [0, 1] for each service.
        """
        costs = np.array([s.cost for s in self.services], dtype=float)
        return float(np.mean(costs))
 
    # ------------------------------------------------------------------
    # Ranking (eq. 10)
    # ------------------------------------------------------------------
 
    @staticmethod
    def _sigmoid(x):
        return 1.0 / (1.0 + np.exp(-x))
 
    def rank_single_solution(self, kvi_request, kvi_weights, mu=0.5):
        """
        The ranking is calculated for each solution s_m through a sigmoid function of
        the summatory of the difference between the kvi request and the kvi of the solution chain, 
        weighted by the kvi weights. The economic cost of the solution is balanced with the parameter mu.
        
        Compute the ranking score R(Sm) as in eq. 10.
 
        Parameters
        ----------
        kvi_request : array-like, shape (N,)
            Target KVI values vn in [0, 1].
        kvi_weights : array-like, shape (N,)
            Priority weights wn, must sum to 1.
        mu : float
            Trade-off between sustainability gap (1-mu) and cost (mu).
 
        Returns
        -------
        float
            Ranking score. Lower is better.
        """
        kvi_request = np.asarray(kvi_request, dtype=float)
        kvi_weights = np.asarray(kvi_weights, dtype=float)
 
        Em = self.calculate_chain_cost()
 
        # Weighted deviation from targets (positive = below target = penalised)
        deviation = float(np.dot(kvi_request - self.chain_kvis, kvi_weights))
 
        sustainability_term = self._sigmoid(deviation)
        self.score = (1 - mu) * sustainability_term + mu * Em
 
        return self.score
 
    def meets_requirements(self, kvi_request):
        """Return True if all chain KVIs meet or exceed their targets."""
        return bool(np.all(self.chain_kvis >= np.asarray(kvi_request, dtype=float)))
 
    # ------------------------------------------------------------------
    # Display
    # ------------------------------------------------------------------
 
    def summary(self, kvi_request, kvi_weights, mu=0.5):
        score = self.rank_single_solution(kvi_request, kvi_weights, mu)
        feasible = self.meets_requirements(kvi_request)
        lines = [
            f"  Chain KVIs : {np.round(self.chain_kvis, 3)}",
            f"  Cost (Em)  : {self.calculate_chain_cost():.3f}",
            f"  Score      : {score:.4f}  ({'feasible' if feasible else 'INFEASIBLE'})",
        ]
        return "\n".join(lines)
    