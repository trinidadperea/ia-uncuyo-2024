from environment import Environment
from agent import Agent

def main():

    #inicializo entorno
    env = Environment(sizeX = 5, sizeY = 4,init_posX = 2, init_posY = 1, dirt_rate = 0.3)

    #inicializo al agente
    agent = Agent(env)

    print("estado inicial")
    env.print_environment()
    print("")

    #realizamos acciones aleatorias mediante el agente
    for _ in range(18):
        agent.think(env) #el agente va a decidir que hago
        env.print_environment() #muestro despues de cada accion
        print(f"Limpie: {env.get_performance()}") #imprimo suciedad



if __name__ == "__main__":
    main()
