
import gymnasium as gym
from gymnasium.envs.toy_text.frozen_lake import generate_random_map
import random


def frozenLake(env):
    #env = gym.make('FrozenLake-v1', render_mode = 'human')
    #env = gym.make('FrozenLake-v1', desc=None, map_name="4x4", render_mode='human')
    #desc=["SFFF", "FHFH", "FFFH", "HFFG"]
    #env = gym.make('FrozenLake-v1', desc=desc, render_mode='human')
    print("Numero de estados:", env.observation_space.n)
    print("Numero de acciones:", env.action_space.n)

    state = env.reset()
    print("Posicion inicial del agente:", state[0])

    done = truncated = False
    while not (done or truncated):
        action = env.action_space.sample() # Acci´on aleatoria
        next_state, reward, done, truncated, _ = env.step(action)
        print(f"Accion: {action}, Nuevo estado: {next_state}, Recompensa: {reward}")
        print(f"¿Gano? (encontro el objetivo): {done}")
        print(f"¿Freno? (alcanzo el maximo de pasos posible): {truncated}\n")
        state = next_state

def generate_random_map(tamaño, probabilidad):
    #genero un mapa con todo slos espacios en "F" frozen
    map = [['F' for _ in range(tamaño)]for _ in range(tamaño)]

    #coloco de forma aleatoria el star y el goal
    start_pos = (random.randint(0,tamaño-1),random.randint(0,tamaño-1))
    goal_pos = (random.randint(0,tamaño-1),random.randint(0,tamaño-1))

    #verifico que no esten en la misma pos
    while start_pos == goal_pos:
        goal_pos = (random.randint(0,tamaño-1),random.randint(0,tamaño-1))

    #coloco s en la posicion inicial del agente
    map[start_pos[0]][start_pos[1]] = 'S'
    #coloco g en la posicion del objetivo
    map[goal_pos[0]][goal_pos[1]] = 'G'

    #saco las '' y los corchetes para que se vea mejor
    map = [''.join(row) for row in map]
    
    return map

#busqueda no informada
def generate_random_map_obstaculos(tamaño,probabilidad):
    #genero un mapa en frozen
    map = [['F' for _ in range(tamaño)]for _ in range(tamaño)]
    
    #coloco de forma aleatoria el star y el goal
    start_pos = (random.randint(0,tamaño-1),random.randint(0,tamaño-1))
    goal_pos = (random.randint(0,tamaño-1),random.randint(0,tamaño-1))

    #verifico que no esten en la misma pos
    while start_pos == goal_pos:
        goal_pos = (random.randint(0,tamaño-1),random.randint(0,tamaño-1))

    #coloco s en la posicion inicial del agente
    map[start_pos[0]][start_pos[1]] = 'S'
    #coloco g en la posicion del objetivo
    map[goal_pos[0]][goal_pos[1]] = 'G'

    #ahora coloco obstaculos con la probabilidad dada
    for i in range(tamaño):
        for j in range(tamaño):
            if (i,j) != start_pos and (i,j) != goal_pos:
                if random.random() < probabilidad:
                    map[i][j] = 'H'
    
    #saco las '' y los corchetes para que se vea mejor
    map = [''.join(row) for row in map]
    
    return map

