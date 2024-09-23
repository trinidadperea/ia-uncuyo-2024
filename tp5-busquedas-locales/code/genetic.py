from environment import *
import random



def genetic(population_size: int, iterations: int, mutation_rate: float, size: int):

    population = get_population(population_size, size)
    sum_fitness, best_state = get_population_fitness(population, size)
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


def get_population(population_size: int, size: int):
    population = []
    for i in range(population_size):
        population.append(random_state(size))
    return population


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
