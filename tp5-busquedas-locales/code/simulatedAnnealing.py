from environment import *
import math
import random

def simulated_annealing(schedule, start, size):
    current = start
    i = 0
    h_variation = []
    
    while True:
        h_variation.append(heuristic(current))
        
        if heuristic(current) == 0:
            return current, i, h_variation
        
        T = schedule(i, size)
        
        if T == 0:
            return current, i, h_variation

        next_state = random.choice(neighbors(current))
        delta_e = heuristic(next_state) - heuristic(current)
   
        if delta_e < 0 or random.uniform(0, 1) < math.exp(-delta_e / T):
            current = next_state
        
        i += 1

def logarithmic(k):
    return 100 / (1 + k)

def exponential(k, n):
    t0 = 10 * n
    alpha = 0.95
    return t0 * (alpha ** k)