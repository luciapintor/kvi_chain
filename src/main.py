"""
author lucia pintor
Use Case — Section V: A Network Provider Demonstrating Commitment to SDGs
 
6 candidate service chains combining strategy B (3 instances per service type)
and strategy C (chains of length 2 and 3).
 
KVIs
----
n=1  Renewable Energy Percentage  (SDG 7)  — aggregator: weighted_average
n=2  Gender Equality Index        (SDG 5)  — aggregator: min
n=3  Workplace Quality            (SDG 8)  — aggregator: min
n=4  Inclusion / Anti-discrim.    (SDG 10) — aggregator: min
 
Request : e.g., V = [0.8, 0.5, 0.7, 0.5]
Weights : e.g., W = [0.25, 0.25, 0.25, 0.25]
mu      : e.g., mu = 0.5  (trade-off between sustainability gap and cost)

"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

import numpy as np
from classes.key_indicator_list import KeyIndicatorList
from classes.service import *
from classes.solution import Solution
  
if __name__ == "__main__":
    
    # -----------------------------------------------------------------------
    # KVI configuration
    # -----------------------------------------------------------------------
    
    kvi_names = ["renewable_energy_percentage", "gender_equality_index", "workplace_quality", "inclusion_index"]
    kvi_aggregators = ["weighted_average", "min", "min", "min"]
    
    # Key indicators
    kvis = KeyIndicatorList(names=kvi_names, aggregators=kvi_aggregators)
    
    # -----------------------------------------------------------------------
    # Request and ranking parameters
    # -----------------------------------------------------------------------
    
    v = np.array([0.8, 0.6, 0.7, 0.6])       # KVI targets
    w  = np.array([0.25, 0.25, 0.25, 0.25])  # equal weights
    mu = 0.5                                 # sustainability / cost trade-off
    
    # -----------------------------------------------------------------------
    # Service function instances
    # kvi_values = [RE_pct, gender, workplace, inclusion]
    # resource_weight = pm,i (used only by weighted_average aggregator)
    # -----------------------------------------------------------------------
    
    # --- StreamingService (pm,i = 0.6) ---
    SS1 = StreamingService(kvis=kvis, kvi_values=[0.8, 0.0,  0.0,  0.0],  cost=0.2,  resource_weight=0.6)
    SS2 = StreamingService(kvis=kvis, kvi_values=[0.8, 0.6,  0.8,  0.6],  cost=0.4,  resource_weight=0.6)
    
    # --- RenewableEnergyService (pm,i = 0.4) ---
    RE1 = RenewableEnergyService(kvis=kvis, kvi_values=[0.9,  0.3,  0.3,  0.3],  cost=0.2,  resource_weight=0.4)
    RE2 = RenewableEnergyService(kvis=kvis, kvi_values=[0.85, 0.5,  0.75, 0.5],  cost=0.3,  resource_weight=0.4)
    
    # --- Specialized services (pm,i = 0.2) ---
    GE1 = GenderEqualityService(kvis=kvis, kvi_values=[0.75, 0.9,  0.7,  0.55], cost=0.25, resource_weight=0.2)
    WP1 = WorkplaceService     (kvis=kvis, kvi_values=[0.75, 0.55, 0.95, 0.55], cost=0.25, resource_weight=0.2)
    IN1 = InclusionService     (kvis=kvis, kvi_values=[0.75, 0.55, 0.7,  0.9],  cost=0.25, resource_weight=0.2)
    
        
    # -----------------------------------------------------------------------
    # Candidate service chains
    # -----------------------------------------------------------------------
    
    chains = {
        "C1": Solution(services=[SS1, RE1]),        # 2 SF, low sustainability, low cost
        "C2": Solution(services=[SS1, RE2]),        # 2 SF, improved energy
        "C3": Solution(services=[SS2, GE1]),   # 3 SF, balanced, gender specialist — expected feasible
        "C4": Solution(services=[SS2, WP1]),   # 3 SF, balanced, workplace specialist — expected feasible
        "C5": Solution(services=[SS2, IN1]),   # 3 SF, min penalises SS1/RE1 social scores
        "C6": Solution(services=[SS2, RE2, GE1, WP1, IN1]),   # 5 SF, high sustainability, high cost — expected feasible
    }
    
    # -----------------------------------------------------------------------
    # Results
    # -----------------------------------------------------------------------
    
    print("=" * 65)
    print("USE CASE — Candidate Service Chain Ranking")
    print("=" * 65)
    print(f"KVI targets  V = {v}")
    print(f"KVI weights  W = {w}")
    print(f"mu             = {mu}")
    print("-" * 65)
    
    results = {}
    for name, chain in chains.items():
        score = chain.rank_single_solution(kvi_request=v, kvi_weights=w, mu=mu)
        results[name] = score
    
    # Sort by score (lower is better)
    ranked = sorted(results.items(), key=lambda x: x[1])
    
    print(f"\n{'Chain':<6} {'RE%':>6} {'Gender':>8} {'Wkplace':>8} "
        f"{'Incl':>6} {'Cost':>6} {'Score':>8} {'Feasible':>10}")
    print("-" * 65)
    
    for name, chain in chains.items():
        kv = chain.chain_kvis
        cost = chain.calculate_chain_cost()
        score = results[name]
        feasible = chain.meets_requirements(v)
        print(f"{name:<6} {kv[0]:>6.3f} {kv[1]:>8.3f} {kv[2]:>8.3f} "
            f"{kv[3]:>6.3f} {cost:>6.3f} {score:>8.4f} {'YES' if feasible else 'NO':>10}")
    
    print("\n--- Ranking (best to worst) ---")
    for rank, (name, score) in enumerate(ranked, 1):
        feasible = chains[name].meets_requirements(v)
        print(f"  {rank}. {name}  score={score:.4f}  {'[feasible]' if feasible else '[INFEASIBLE]'}")