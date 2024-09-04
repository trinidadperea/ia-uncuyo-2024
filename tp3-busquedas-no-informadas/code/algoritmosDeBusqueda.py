
from collections import deque
import gymnasium as gym
import random
import heapq

from collections import deque

from collections import deque

def bfs(env, start, goal):
    queue = deque([(start, [start])])
    came_from = {start: None}
    visited = set()
    visited.add(start)

    while queue:
        (current, path) = queue.popleft()
        if current == goal:
            #print_environment_info(env)  # Imprime el entorno generado
            #print("Secuencia de estados:", path)  # Imprime la secuencia de estados
            return path

        for action in range(env.action_space.n):
            next_state = take_action(env, current, action)
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [next_state]))
                came_from[next_state] = current
    #print_environment_info(env) # Imprime el entorno generado
    #print("Secuencia de estados: No encontrado")  # Imprime que no se encontró una secuencia
    return None


def dfs(env,start,goal):
    stack = deque([(start, [start])])
    
    came_from = {start: None}
    visited = set()
    visited.add(start)
    
    while stack:
        (current, path) = stack.pop()
        
        if current == goal:
            return path  
        

        for action in range(env.action_space.n):
            next_pos = take_action(env, current, action)
            if next_pos not in visited:
                visited.add(next_pos)
                stack.append((next_pos, path + [next_pos]))
                came_from[next_pos] = current
            
    
    return None
def dfs_limit(env,start,goal,limit):

    stack = deque([(start, [start],0)])
    came_from = {start: None}
    visited = set()
    visited.add(start)
    
    while stack:
        (current, path, depth) = stack.pop()
        
        if current == goal:
            return path 
        
        if depth < limit:
            for action in range(env.action_space.n):
                next_pos = take_action(env, current, action)
                if next_pos not in visited:
                    visited.add(next_pos)
                    stack.append((next_pos, path + [next_pos],depth + 1))
                    came_from[next_pos] = current
            
    return None

def ucs(env, start, goal):
    # La cola de prioridad se implementa usando heapq
    queue = []
    heapq.heappush(queue, (0, start, [start]))  # (costo acumulado, estado actual, camino)
    
    came_from = {start: None}
    cost_so_far = {start: 0}
    visited = set()

    while queue:
        current_cost, current, path = heapq.heappop(queue)

        if current == goal:
            return path

        if current in visited:
            continue

        visited.add(current)

        for action in range(env.action_space.n):
            next_state = take_action(env, current, action)
            new_cost = current_cost + 1  # Aquí puedes ajustar el costo según sea necesario

            if next_state not in visited and (next_state not in cost_so_far or new_cost < cost_so_far[next_state]):
                cost_so_far[next_state] = new_cost
                priority = new_cost
                heapq.heappush(queue, (priority, next_state, path + [next_state]))
                came_from[next_state] = current

    return None

#funcion donde elijo la accion a realizar
def take_action(env,position,action):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    direction = directions[action]

    # Calculamos la nueva posición
    new_x = position[0] + direction[0]
    new_y = position[1] + direction[1]

    if 0 <= new_x < env.spec.max_episode_steps and 0 <= new_y < env.spec.max_episode_steps:
        return (new_x, new_y)
    
    return position

def print_environment_info(env):
    # Usar `env.unwrapped` para acceder a la información subyacente
    unwrapped_env = env.unwrapped

    if hasattr(unwrapped_env, 'desc'):
        print("Descripción del entorno:")
        print(unwrapped_env.desc)
    else:
        print("Descripción del entorno no disponible.")

    if hasattr(unwrapped_env, 'observation_space'):
        print("Espacio de observación:")
        print(unwrapped_env.observation_space)

    if hasattr(unwrapped_env, 'action_space'):
        print("Espacio de acción:")
        print(unwrapped_env.action_space)
    
    # Intentar obtener el estado actual de `unwrapped_env`
    if hasattr(unwrapped_env, 'state'):
        print("Estado actual:")
        print(unwrapped_env.state)
    else:
        print("El entorno no tiene un estado disponible para imprimir.")
