"""
class Node:
    def __init__(self, position, parent=None, action=None, cost=0):
        self.position = position
        self.parent = parent
        self.action = action
        self.cost = cost
"""
class Node:
    def __init__(self, position, parent=None, action=None):
        self.position = position  # La posición actual del nodo (x, y)
        self.parent = parent  # Nodo padre para reconstruir el camino
        self.action = action  # Acción realizada para llegar a este nodo
        self.g = 0  # Costo acumulado desde el inicio hasta este nodo (g)
        self.h = 0  # Heurística estimada desde este nodo hasta el objetivo (h)
        self.f = 0  # f = g + h, el costo total estimado

    # Implementar el método __lt__ para permitir comparaciones entre nodos
    def __lt__(self, other):
        return self.f < other.f

    def __eq__(self, other):
        return self.position == other.position