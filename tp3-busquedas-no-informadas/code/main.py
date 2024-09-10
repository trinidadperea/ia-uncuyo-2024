from custom_map import generate_random_map
from custom_map import frozenLake
from gymnasium.envs.toy_text.frozen_lake import generate_random_map
import gymnasium as gym
from gymnasium.wrappers import TimeLimit
from custom_map import generate_random_map_obstaculos
from algoritmosDeBusqueda import *
import random
import matplotlib.pyplot as plt
import csv
import statistics
from datetime import datetime
import csv
import time

tamaño = 100
probabilidad = 0.08
iteraciones = 30
#listas para almacenar los resultados
resultsBFS = []
resultsBFS_cost = []
resultsBFS_cost2 = []
resultsDFS = []
resultsDFS_cost = []
resultsDFS_cost2 = []
resultsDFS_LIMIT = []
resultsDFS_LIMIT_cost = []
resultsDFS_LIMIT_cost2 = []
resultsUCS = []
resultsUCS_cost = []
resultsUCS_cost2 = []
resultsA_star = []
resultsA_star_cost = []
resultsA_star_cost2 = []

#listas que llevan los tiempos
BFS_time = []
DFS_time = []
UCS_time = []
DFS_LIMIT_time = []
resultsA_star_time = []

custom_map = generate_random_map_obstaculos(tamaño, probabilidad)
for row in custom_map:
    print(row)


env = gym.make('FrozenLake-v1', desc=custom_map, render_mode='human')
frozenLake(env)

# Definir la función de heurística
def manhattan_distance(current, goal):
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1])

for i in range(0,iteraciones):
    Sx = random.randint(0,tamaño-1)
    Sy = random.randint(0,tamaño-1)
    Gx = random.randint(0,tamaño-1)
    Gy = random.randint(0,tamaño-1)
    #verifico que sean distintos
    while (Sx,Sy) == (Gx,Gy):
        Gx = random.randint(0,tamaño-1)
        Gy = random.randint(0,tamaño-1)
    start = (Sx,Sy)
    goal = (Gx,Gy)
    #almaceno los resultados
    #los e hacen referencia a los costos del escenario 2

    #agrego los tiempos bfs
    start_time = time.time()
    count1, cost1, e2_1 = bfs(env,start,goal)
    end_time = time.time()
    resultsBFS.append(count1)
    resultsBFS_cost.append(cost1)
    resultsBFS_cost2.append(e2_1)
    BFS_time.append(end_time - start_time)
    
    #agrego tiempo dfs
    start_time = time.time()
    count2, cost2, e2_2 = dfs(env,start,goal)
    end_time = time.time()
    resultsDFS.append(count2)
    resultsDFS_cost.append(cost2)
    resultsDFS_cost2.append(e2_2)
    DFS_time.append(end_time - start_time)

    #agrego tiempo UCS
    start_time = time.time()
    count3, cost3, e2_3= ucs(env,start,goal)
    end_time = time.time()
    resultsUCS.append(count3)
    resultsUCS_cost.append(cost3)
    resultsUCS_cost2.append(e2_3)
    UCS_time.append(end_time - start_time)
 
    #tiempo dfs limit
    start_time = time.time()
    limit, cost4, e2_4 = dfs_limit(env,start,goal,5000) #limite 5000 ya que es la mitad de el tamaño 
    end_time = time.time()
    if limit != None:
        resultsDFS_LIMIT.append(limit)
        resultsDFS_LIMIT_cost.append(cost4)
        resultsDFS_LIMIT_cost2.append(e2_4)
        DFS_LIMIT_time.append(end_time - start_time)

    #agrego A*
    start_time = time.time()
    count5, cost5, e2_5 = a_star(env,start,goal,manhattan_distance)
    end_time = time.time()
    resultsA_star.append(count5)
    resultsA_star_cost.append(cost5)
    resultsA_star_cost2.append(e2_5)
    resultsA_star_time.append(end_time - start_time)

    #imprimo los resultados
    print(f"[BFS]: {resultsBFS[i]}")
    print(f"[DFS]: {resultsDFS[i]}")
    print(f"[UCS]: {resultsUCS[i]}")
    print(f"[A*]:  {resultsA_star[i]}")
    if i < len(resultsDFS_LIMIT):
        print(f"[DFS_LIMIT]: {resultsDFS_LIMIT[i]}")
algoritmosDeBusqueda = ["BFS", "DFS", "UCS","DFSL","A*"]
resultados = [resultsBFS, resultsDFS, resultsUCS, resultsDFS_LIMIT, resultsA_star ]

plt.boxplot(resultados, tick_labels=algoritmosDeBusqueda)
plt.ylabel("Cantidad de pasos")
plt.title("Grafico de caja Algoritmos de busqueda")
plt.savefig('boxplot_resultados.png')

mean_results = [statistics.mean(results) for results in resultados]
std_dev_results = [statistics.stdev(results) for results in resultados]

print(" ")

for i, algorithm in enumerate(algoritmosDeBusqueda):
    print(f"Algoritmo: {algoritmosDeBusqueda}")
    print(f"Media: {mean_results[i]}")
    print(f"Desviación estándar: {std_dev_results[i]}")
    print()

with open('no-informada-results.csv', 'w', newline='') as csvfile:
    fieldnames = ['algorithm_name', 'env_n','states_n','cost_e1','cost_e2','time', 'solution_found']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    for env_n in range(iteraciones):
        writer.writerow({'algorithm_name': 'BFS', 'env_n': env_n + 1, 'states_n': resultsBFS[env_n], 'cost_e1' : resultsBFS_cost[env_n],'cost_e2':resultsBFS_cost2[env_n],'time': BFS_time[env_n] ,'solution_found': 'Yes' if resultsBFS[env_n] is not None else 'No'})
        writer.writerow({'algorithm_name': 'DFS', 'env_n': env_n+ 1, 'states_n': resultsDFS[env_n],'cost_e1' : resultsDFS_cost[env_n],'cost_e2':resultsDFS_cost2[env_n],'time': DFS_time[env_n] ,'solution_found': 'Yes' if resultsDFS[env_n] is not None else 'No'})
        writer.writerow({'algorithm_name': 'UCS', 'env_n': env_n + 1, 'states_n': resultsUCS[env_n], 'cost_e1' : resultsUCS_cost[env_n],'cost_e2':resultsUCS_cost2[env_n],'time': UCS_time[env_n] ,'solution_found': 'Yes' if resultsUCS[env_n] is not None else 'No'})
        writer.writerow({'algorithm_name': 'A*', 'env_n': env_n + 1, 'states_n': resultsA_star[env_n], 'cost_e1' : resultsA_star_cost[env_n],'cost_e2':resultsA_star_cost2[env_n],'time': resultsA_star_time[env_n] ,'solution_found': 'Yes' if resultsA_star[env_n] is not None else 'No'})
        if env_n < len(resultsDFS_LIMIT):
            writer.writerow({'algorithm_name': 'DLS', 'env_n': env_n + 1, 'states_n': resultsDFS_LIMIT[env_n],'cost_e1' :resultsDFS_LIMIT_cost[env_n],'cost_e2':resultsDFS_LIMIT_cost2[env_n],'time': DFS_LIMIT_time[env_n] , 'solution_found': 'Yes' if resultsDFS_LIMIT[env_n] is not None else 'No'})
        else:
            writer.writerow({'algorithm_name': 'DLS', 'env_n': env_n + 1, 'states_n': limit ,'cost_e1': cost4,'cost_e2':e2_4,'time': None,'solution_found': 'No'})
