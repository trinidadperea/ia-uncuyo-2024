import random
from environment import Environment

class Agent:
    def __init__(self,env):
        self.env = env
    
    def up(self):
        self.env.accept_action("Arriba")

    def down(self):
        self.env.accept_action("Abajo")
    
    def left(self):
        self.env.accept_action("Izquierda")

    def right(self):
        self.env.accept_action("Derecha")

    def suck(self):
        self.env.accept_action("Limpia")

    def idle(self):
        self.env.accept_action("NoHacerNada")
    
    def perspective(self,env):
        return self.env.clean()
    
    #implementa las acciones a seguir por el agente
    def think(self,env):
        #si cae en un lugar sucio lo limpia
        if self.perspective(env):
            self.suck()
        else:
            #hace lo pedido 
            action = random.choice(["Arriba","Abajo","Izquierda","Derecha"])
            print(action)
            if action == "Arriba":
                self.up()
            if action == "Abajo":
                self.down()
            if action == "Izquierda":
                self.left()
            if action == "Derecha":
                self.right()


