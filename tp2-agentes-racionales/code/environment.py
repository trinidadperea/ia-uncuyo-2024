import random 

class Environment:
    def __init__(self, sizeX, sizeY, init_posX, init_posY, dirt_rate):
        self.sizeX = sizeX #filas
        self.sizeY = sizeY #columnas
        self.agent_posX = init_posX
        self.agent_posY = init_posY
        self.dirt_rate = dirt_rate
        #armo la grilla de suciedad con la libreria random 
        #voy a generar un nro aleatorio entre 0 y 1, si cuando paso por ahi el valor obtenido es menor a 
        #el valor de dirt_rate, lo coloco como sucio, con un 1
        self.grid = [[1 if random.random() < dirt_rate else 0 for _ in range(sizeY)] for _ in range(sizeX)]
        self.clean_count = 0
    
    def accept_action(self,action):
        if action == "Arriba":
            self.move(-1,0)
        if action == "Abajo":
            self.move(1,0)
        if action == "Izquierda":
            self.move(0,-1)
        if action == "Derecha":
            self.move(0,1)
        if action == "Limpiar":
            self.clean()
        if action == "NoHacerNada": #no me muevo, ni limpio
            self.move(0,0)

    def clean(self):
        if self.grid[self.agent_posX][self.agent_posY] == 1:
            self.grid[self.agent_posX][self.agent_posY] = 0
            self.clean_count += 1
        return self.clean_count
    
    def move(self,dx,dy):
        x = self.agent_posX + dx
        y = self.agent_posY + dy
        #verifico para no salirme de la grilla
        if 0 <= x < self.sizeX and 0 <= y < self.sizeY:
            #actualizo
            self.agent_posX = x
            self.agent_posY = y


    def is_dirty(self):
        #si esta sucio debo devolver 1
        return self.grid[self.agent_posX][self.agent_posY] == 1

    def get_performance(self):
        return self.clean_count
    
    def print_environment(self):
        for x in range(self.sizeX):
            for y in range(self.sizeY):
                #coloco una A si el agente esta en la celda
                if self.agent_posX == x and self.agent_posY == y:
                    print("A", end=" ")
                elif self.grid[x][y] == 1:
                    #celda sucia
                    print("D", end=" ")
                else:
                    #celda limpia
                    print(".", end=" ")
            print(" ")

