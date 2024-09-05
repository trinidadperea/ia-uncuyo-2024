class Node:
    def __init__(self, position, parent=None, action=None, cost=0):
        self.position = position
        self.parent = parent
        self.action = action
        self.cost = cost