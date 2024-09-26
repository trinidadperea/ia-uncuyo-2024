from environment import *
import random



def genetic(population_size: int, iterations: int, mutation_rate: float, size: int):

    population = get_population(population_size, size)
    sum_fitness, best_state = get_population_fitness(population, size)

    # c) estrategia de reemplazo -------------------------------------------------------------------------------
    # Después de generar una nueva población (a través de cruce y mutación), la nueva generación reemplaza a la población anterior. Sin embargo, hay una estrategia de "elitismo" en la que un porcentaje fijo de los mejores individuos de la población actual se conserva para la siguiente generación. Esto está controlado por la variable elite_size, que asegura que los mejores individuos no se pierdan.
    elite_size = int(population_size * 0.1)
    h_variation = []

    if fitness(best_state, size) == 0:
        return best_state, 0, [0]

    i = 0
    while iterations > 0:
        selected = selection(population, sum_fitness, size)
        new_population = crossover(selected)
        new_population = mutate(new_population, mutation_rate, size)
        offspring = sorted(new_population, key=lambda x: fitness(x, size))[:population_size - elite_size]
        elites = sorted(population, key=lambda x: fitness(x, size))[:elite_size]  
        new_population = elites + offspring
        sum_fitness, best_state = get_population_fitness(new_population, size)

        h_variation.append(fitness(best_state, size))
        if fitness(best_state, size) == 0:
            return best_state, i, h_variation

        population = new_population
        iterations -= 1
        i += 1
    return best_state, i, h_variation


def get_population_fitness(population, size):
    sum_fitness = 0
    best_fitness = float('inf')
    best_state = None
    for state in population:
        state_fitness = fitness(state, size)
        sum_fitness += state_fitness
        if state_fitness < best_fitness:
            best_fitness = state_fitness
            best_state = state
    return sum_fitness, best_state


#a) Definición de los Individuos de la población --------------------------------------------------------------------------------

#Individuos: Cada individuo en la población está representado por un estado que es una lista generada por random_state(size) en la función get_population(). Los estados representan posibles soluciones para el problema de las N-reinas.
#Por ejemplo, si size = 8 (8 reinas), cada individuo sería una lista de 8 números, donde cada número indica la fila de una reina en una columna específica.

def get_population(population_size: int, size: int):
    population = []
    for i in range(population_size):
        population.append(random_state(size))
    return population


# B) Estrategia de selección -----------------------------------------------------------
#La función selection() implementa una forma de selección basada en la aptitud (fitness). La probabilidad de seleccionar un individuo es inversamente proporcional a su valor de fitness. Los estados con menor fitness tienen mayor probabilidad de ser seleccionados para la reproducción (ya que menor fitness indica una mejor solución en este caso).


def fitness(state, size):
    return heuristic(state) 


def selection(population, sum_fitness, size):
    selected = []
    for state in population:
        pr = fitness(state, size) / sum_fitness
        if random.random() < pr:
            selected.append(state)
    return selected


def crossover(selected):
    new_population = []
    for i in range(len(selected)):
        for j in range(len(selected)):
            if i != j:
                new_population.append(crossover_states(selected[i], selected[j]))
    return new_population

# d) Operadores: crossover, mutación -----------------------------------------------------------

# crossover(): combina dos individuos seleccionados para crear nuevos individuos. Esto se hace cortando los estados por la mitad y mezclando sus partes.

# mutate(): altera aleatoriamente el estado de los individuos con una probabilidad definida por mutation_rate. Esto introduce variabilidad en la población

def crossover_states(state1, state2):
    cross_point = int(len(state1)/2)
    new_state = []
    if random.random() < 0.5:
        for i in range(len(state1)):
            if i < cross_point:
                new_state.append(state1[i])
            else:
                new_state.append(state2[i])
    else:
        for i in range(len(state1)):
            if i < cross_point:
                new_state.append(state2[i])
            else:
                new_state.append(state1[i])
    return new_state


def mutate(population, mutation_rate, size):
    new_population = []
    for state in population:
        for i in range(len(state)):
            if random.random() < mutation_rate:
                state[i] = random.randint(0, size - 1)
        new_population.append(state)
    return new_population
