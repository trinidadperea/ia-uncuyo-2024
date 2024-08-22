from environment import Environment
from agentS import AgentS
from agentA import AgentA
import random 
def main():

    #inicializo entorno
    sizes = [2,4,8,16,32,64,128]
    dirt_rates = [0.1,0.2,0.4,0.8]

    #almaceno resultados
    results = {}

    #numero de repeticiones por combinacion
    num_repeats = 10

    for size in sizes:
        for dirt_rate in dirt_rates:
            clean_counts = []
            for _ in range(num_repeats):
                #inicializo entorno
                sizeX = size
                sizeY = size
                posX = 0
                posY = 0
                dirty = dirt_rate
                env = Environment(sizeX,sizeY,posX,posY,dirt_rate)
                #inicializo agente
                agent = AgentS(env)

                for _ in range(100):
                    agent.think(env)
                clean_counts.append(env.get_performance())

            resp_clean_count = sum(clean_counts) / num_repeats
            results[(size,dirt_rate)] = resp_clean_count
    # Mostrar resultados
    for key, value in results.items():
        print(f"Tamaño: {key[0]}x{key[0]}, Suciedad: {key[1]}, Desempeño Promedio: {value}")


if __name__ == "__main__":
    main()
