
from collections import deque
import gymnasium as gym
import random
import heapq
from node import Node
from custom_map import validLocation


def bfs(env, start, goal):
    node = Node(start) #nodo inicial
    queue = [node]  #creo la cola

    visited = set()
    count = 0
    cost = 0
    cost2 = 0

    while queue:
        node = queue.pop()
        visited.add(node.position)
        count += 1

        if node.position == goal: #llegue al goal, retorno la cantidad de pasos
            return count, cost, cost2
        
        for action in ["arriba", "abajo", "izquierda", "derecha"]:
            cost += 1 #escenario 1 cada accion tiene costo 1
            cost2 += calculate_cost2(action)
            x, y = take_action(node.position, action)
            if (x, y) not in visited and validLocation(env,x, y):
                new_node = Node((x, y), node, action)
                visited.add(new_node.position) 
                queue.append(new_node)
    
    return None, cost, cost2

def dfs(env, start, goal):

    node = Node(start)
    stack = [node]
    visited = set()
    count = 0
    cost = 0
    cost2 = 0

    while stack:

        node = stack.pop(0)
        count += 1
        visited.add(node.position)

        if node.position == goal:
            return count, cost, cost
        
        for action in ["arriba", "abajo", "izquierda", "derecha"]:
            cost += 1
            cost2 += calculate_cost2(action)
            x, y = take_action(node.position, action)
            if (x,y) not in visited and validLocation(env,x,y):
                new_node = Node((x,y), node,)
                stack.insert(0,new_node)

    return None, cost, cost2

def dfs_limit(env, start, goal, limit):
    stack = [Node(start)]
    visited = set()
    count = 0
    cost = 0
    cost2 = 0

    while stack:
        node = stack.pop()
        count += 1
        visited.add(node.position)
        limit -= 1

        if node.position == goal:
            return count, cost, cost2
        
        if limit <= 0:
            return None, cost, cost2
        
        for action in ["arriba", "abajo", "izquierda", "derecha"]:
            cost += 1
            cost2 += calculate_cost2(action)
            x, y = take_action(node.position, action)
            if (x, y) not in visited and validLocation(env,x, y):
                new_node = Node((x, y), node)
                stack.append(new_node)

    return None, cost, cost2

def ucs(env, start, goal):

    queue = [(0, Node(start))]
    visited = set()
    count = 0
    cost = 0
    cost2 = 0

    while queue:
        cost, node = queue.pop(0)
        count += 1

        if node.position == goal:
            return count, cost, cost2

        if node.position in visited:
            continue

        visited.add(node.position)
        for action in ["arriba", "abajo", "izquierda", "derecha"]:
            cost += 1
            cost2 += calculate_cost2(action)
            x, y = take_action(node.position, action)
            if validLocation(env, x, y):
                new_node = Node((x, y), node, action)
                new_cost = cost + 1  # Incrementamos el costo
                queue.append((new_cost, new_node))

        queue.sort(key=lambda x: x[0])  # Ordenar por costo

    return None, cost, cost2 
def a_star(env, start, goal, heuristic_func):
    queue = [(0, 0, Node(start))]  # (costo_total, costo_acumulado, nodo)
    visited = set()
    count = 0
    cost2_total = 0  # Para almacenar el costo secundario si es necesario

    while queue:
        # Obtenemos el nodo con el menor costo total
        cost_total, cost_accumulated, node = heapq.heappop(queue)
        count += 1

        # Si alcanzamos el objetivo
        if node.position == goal:
            return count, cost_accumulated, cost2_total

        # Verificamos si ya visitamos el nodo
        if node.position in visited:
            continue

        visited.add(node.position)

        # Expandimos los vecinos (acciones posibles)
        for action in ["arriba", "abajo", "izquierda", "derecha"]:
            x, y = take_action(node.position, action)

            if validLocation(env, x, y):  # Verificamos si la ubicación es válida
                new_node = Node((x, y), node, action)
                action_cost = calculate_cost2(action)  # Costo asociado a la acción
                new_cost_accumulated = cost_accumulated + action_cost  # Costo acumulado
                heuristic_cost = heuristic_func((x, y), goal)  # Coste estimado heurístico

                # Costo total en A* = Costo acumulado + Heurística
                new_cost_total = new_cost_accumulated + heuristic_cost

                # Incrementamos el costo secundario si es necesario
                cost2_total += action_cost

                # Añadimos el nuevo nodo con su costo total y acumulado a la cola
                heapq.heappush(queue, (new_cost_total, new_cost_accumulated, new_node))

    # Si no encontramos una solución
    return None, float('inf'), cost2_total


#funcion donde elijo la accion a realizar
def take_action(position,action):
    x, y = position
    if action == "arriba":
        return x - 1, y
    elif action == "abajo":
        return x + 1 , y
    elif action == "izquierda":
        return x, y - 1
    elif action == "derecha":
        return x, y + 1
    
#escenario 2
def calculate_cost2(action):
    if action == "arriba":
        return 3
    if action == "abajo":
        return 1
    if action == "izquierda":
        return 0
    if action == "derecha":
        return 2
    

