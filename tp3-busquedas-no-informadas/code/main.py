from custom_map import generate_random_map
from custom_map import frozenLake
from gymnasium.envs.toy_text.frozen_lake import generate_random_map
import gymnasium as gym
from gymnasium.wrappers import TimeLimit
from custom_map import generate_random_map_obstaculos
from algoritmosDeBusqueda import bfs, dfs, dfs_limit, ucs


tamaño = 4
probabilidad = 0.2
custom_map = generate_random_map_obstaculos(tamaño, probabilidad)
for row in custom_map:
    print(row)


env = gym.make('FrozenLake-v1', desc=custom_map, render_mode='human')
frozenLake(env)
start = (0,0)
goal = (99,99)
print("BFS")
path1 = bfs(env,start,goal)
#print(path1)
#print(" imprimo ")
#path = ucs(env,start,goal)
#print(path)
#print(" imprimo limit ")
#si el limite es muy chico devuelve none, porque no alcanza el objetivo
#path3 = dfs_limit(env,start,goal,1000)
#print(path3)

#cambio la vida del agente

#nuevo_limite = 1000
#env = gym.make('FrozenLake-v1', render_mode='human').env
#env = TimeLimit(env, nuevo_limite)

#state = env.reset()
#done = False

#while not done:
#    action = env.action_space.sample()  # Elegir una acción aleatoria
#   state, reward, done, truncated, info = env.step(action)
#    print(f"Estado: {state}, Recompensa: {reward}, Hecho: {done}, Truncado: {truncated}")

#env.close()

