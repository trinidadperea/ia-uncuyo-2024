from environment import *

def hill_climbing(max_iterations, start):  
    current = start
    i = 0
    h_variation = []
    
    while i < max_iterations:
        current_heuristic = heuristic(current)
        h_variation.append(current_heuristic)
        
        if current_heuristic == 0:  
            return current, i, h_variation
        else:
            neighbor = best_neighbor(current)
            neighbor_heuristic = heuristic(neighbor)
            
            if neighbor_heuristic < current_heuristic:
                current = neighbor
            # else:
            #     return current, i, h_variation  
        
        i += 1
    
    return current, i, h_variation 