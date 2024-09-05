
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
    

