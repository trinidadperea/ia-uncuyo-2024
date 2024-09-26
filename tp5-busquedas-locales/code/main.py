from environment import *
from hillClimbing import *
from simulatedAnnealing import *
from genetic import *
import csv
import time
import matplotlib.pyplot as plt

def main():
    sizes = [4,8,10]
    num_trials = 10
    total_trials = len(sizes) * num_trials #para ejecutar 30 veces cada uno
    results_hill = []
    results_sim_annealing = []
    results_genetic = []
    num_explored_hill = []
    num_explored_sim_annealing = []
    num_explored_genetic = []
    count_solution_hill = 0
    count_solution_sim_annealing = 0
    count_solution_genetic = 0
    results = []
    execution_time_hill = []
    execution_time_sim_annealing = []
    execution_time_genetic = []
    h_variation_hill_1 = []
    h_variation_sim_annealing_1 = []
    h_variation_genetic_1 = []
    hill_climbing_time = []
    genetic_time = []
    simulated_annealing_time = []

    startEjecucion = time.time()
    for size in sizes:

        for i in range(num_trials):
            start = initial_state(size)

            # Ejecutar los algoritmos
            start_time_hill = time.time()
            solution_hill, explored_states_hill, h_variation_hill = hill_climbing(100, start)
            end_time_hill = time.time()
            print("Time hill: ",end_time_hill - start_time_hill)

            start_time_sim_annealing = time.time()
            solution_sim_annealing, explored_states_sim_annealing, h_variation_sim_annealing = simulated_annealing(exponential, start,size)
            end_time_sim_annealing = time.time()
            print("Time simulated: ",end_time_hill - start_time_hill)

            start_time_genetic = time.time()
            solution_genetic, explored_states_genetic, h_variation_genetic = genetic(500, 10000,0.1, size)  # Algoritmo genético
            end_time_genetic = time.time()
            print("Time genetic: ",end_time_hill - start_time_hill)

            # Guardar resultados
            results_hill.append(heuristic(solution_hill))
            results_sim_annealing.append(heuristic(solution_sim_annealing))
            results_genetic.append(heuristic(solution_genetic))
            num_explored_states = [explored_states_hill, explored_states_sim_annealing, explored_states_genetic]
            num_explored_hill.append(explored_states_hill)
            num_explored_sim_annealing.append(explored_states_sim_annealing)
            num_explored_genetic.append(explored_states_genetic)

            # Comprobar si se encontró una solución
            found_solution_hill = heuristic(solution_hill) == 0
            found_solution_sim_annealing = heuristic(solution_sim_annealing) == 0
            found_solution_genetic = heuristic(solution_genetic) == 0
            found_solutions = [found_solution_hill, found_solution_sim_annealing, found_solution_genetic]  

            if found_solution_hill:
                count_solution_hill += 1
                execution_time_hill.append(end_time_hill - start_time_hill)
            if found_solution_sim_annealing:
                count_solution_sim_annealing += 1
                execution_time_sim_annealing.append(end_time_sim_annealing - start_time_sim_annealing)
            if found_solution_genetic:
                count_solution_genetic += 1
                execution_time_genetic.append(end_time_genetic - start_time_genetic)

            if i == int((num_trials - 1) / 2):
                h_variation_hill_1 = h_variation_hill
                h_variation_sim_annealing_1 = h_variation_sim_annealing
                h_variation_genetic_1 = h_variation_genetic

            # Guardar resultados individuales
            for j, algorithm in enumerate(['Hill Climbing', 'Simulated Annealing', 'Genetic']):
                if algorithm == 'Hill Climbing':
                    time_taken = end_time_hill - start_time_hill
                elif algorithm == 'Simulated Annealing':
                    time_taken = end_time_sim_annealing - start_time_sim_annealing
                elif algorithm == 'Genetic':
                    time_taken = end_time_genetic - start_time_genetic

                results.append({
                    'Algorithm_name': algorithm,
                    'reinas': size,
                    'env_n': i + 1,
                    'states_n': num_explored_states[j],
                    'solution_found': found_solutions[j],
                    'time': time_taken
                })
    endEjecucion = time.time()
    print("Tiempo del for: ",endEjecucion - startEjecucion)
    # Calculate mean and standard deviation
    mean_states_explored_hill = sum(num_explored_hill) / num_trials
    std_dev_states_explored_hill = (sum([(x - mean_states_explored_hill) ** 2 for x in num_explored_hill]) / num_trials) ** 0.5
    mean_execution_time_hill = sum(execution_time_hill) / num_trials
    std_dev_execution_time_hill = (sum([(x - mean_execution_time_hill) ** 2 for x in execution_time_hill]) / num_trials) ** 0.5
    percentage_solution_hill = count_solution_hill / num_trials

    mean_states_explored_sim_annealing = sum(num_explored_sim_annealing) / num_trials
    std_dev_states_explored_sim_annealing = (sum([(x - mean_states_explored_sim_annealing) ** 2 for x in num_explored_sim_annealing]) / num_trials) ** 0.5
    mean_execution_time_sim_annealing = sum(execution_time_sim_annealing) / num_trials
    std_dev_execution_time_sim_annealing = (sum([(x - mean_execution_time_sim_annealing) ** 2 for x in execution_time_sim_annealing]) / num_trials) ** 0.5
    percentage_solution_sim_annealing = count_solution_sim_annealing / num_trials

    mean_states_explored_genetic = sum(num_explored_genetic) / num_trials
    std_dev_states_explored_genetic = (sum([(x - mean_states_explored_genetic) ** 2 for x in num_explored_genetic]) / num_trials) ** 0.5
    mean_execution_time_genetic = sum(execution_time_genetic) / num_trials
    std_dev_execution_time_genetic = (sum([(x - mean_execution_time_genetic) ** 2 for x in execution_time_genetic]) / num_trials) ** 0.5
    percentage_solution_genetic = count_solution_genetic / num_trials

    # Guardar resultados en archivo csv
    with open('tp5-Nreinas.csv', 'w', newline='') as csvfile:
        fieldnames = ['Algorithm_name', 'reinas','env_n', 'states_n', 'solution_found','time']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)

    print("Hill Climbing")
    print("Estados explorados hasta llegar a la solucion optima ", mean_states_explored_hill)
    print("Desviacion estandar ", std_dev_states_explored_hill)
    print("Tiempo de ejecucion promedio ", mean_execution_time_hill)
    print("Desviacion estandar en tiempo de ejecucion ", std_dev_execution_time_hill)
    print("Porcentaje de soluciones encontradas ", percentage_solution_hill)
    print("")
    print("Simulated Annealing")
    print("Estados explorados hasta llegar a la solucion optima ", mean_states_explored_sim_annealing)
    print("Desviacion estandar ", std_dev_states_explored_sim_annealing)
    print("Tiempo de ejecucion promedio ", mean_execution_time_sim_annealing)
    print("Desviacion estandar en tiempo de ejecucion ", std_dev_execution_time_sim_annealing)
    print("Porcentaje de soluciones encontradas ", percentage_solution_sim_annealing)
    print("")
    print("Genetic")
    print("Estados explorados hasta llegar a la solucion optima ", mean_states_explored_genetic)
    print("Desviacion estandar ", std_dev_states_explored_genetic)
    print("Tiempo de ejecucion promedio ", mean_execution_time_genetic)
    print("Desviacion estandar en tiempo de ejecucion ", std_dev_execution_time_genetic)
    print("Porcentaje de soluciones encontradas ", percentage_solution_genetic)

    # Execution time boxplot
    plt.boxplot([execution_time_hill, execution_time_sim_annealing, execution_time_genetic],
                labels=['Hill Climbing', 'Simulated Annealing', 'Genetic'],
                showfliers=True)
    plt.ylabel('Execution time (s)')
    plt.xlabel('Algorithm')
    plt.title('Execution time boxplot')
    plt.show()

    # Dsitribución de la cantidad de estados previos visitados
    # Boxplot para la cantidad de estados visitados
    plt.boxplot([num_explored_hill, num_explored_sim_annealing, num_explored_genetic],
                labels=['Hill Climbing', 'Simulated Annealing', 'Genetic'],
                showfliers=True)
    plt.ylabel('States visited')
    plt.xlabel('Algorithm')
    plt.title('States visited boxplot')
    plt.show()


    # Heuristic variation plot
    plt.plot(h_variation_hill_1, label='Hill Climbing')
    plt.xlabel('Iteration')
    plt.ylabel('Heuristic')
    plt.title('Heuristic variation plot (Hill Climbing)')
    plt.legend()
    plt.show()

    #SA
    plt.plot(h_variation_sim_annealing_1, label='Simulated Annealing')
    plt.xlabel('Iteration')
    plt.ylabel('Heuristic')
    plt.title('Heuristic variation plot (Simulated Annealing)')
    plt.legend()
    plt.show()

    #GA
    plt.plot(h_variation_genetic_1, label='Genetic')
    plt.xlabel('Iteration')
    plt.ylabel('Heuristic')
    plt.title('Heuristic variation plot (Genetic)')
    plt.legend()
    plt.show()

    """ plt.plot(h_variation_hill_1, label='Hill Climbing')
    plt.plot(h_variation_sim_annealing_1, label='Simulated Annealing')
    plt.plot(h_variation_genetic_1, label='Genetic')
    plt.legend()
    plt.xlabel('Iteration')
    plt.ylabel('Heuristic')
    plt.title('Heuristic variation plot')
    plt.show() """

if __name__ == '__main__':
    main()