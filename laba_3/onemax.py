import numpy as np
import random
import matplotlib.pyplot as plt

n = 20
population_size = 100
mutation_rate = 0.001
max_generations = 1000


def create_population(size, n):
    return [np.random.randint(2, size=n).tolist() for _ in range(size)]


def fitness(individual):
    return sum(individual)


def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

def mutate(individual, mutation_rate):
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            individual[i] = 1 - individual[i]
    return individual

def select_parents(population):
    fitness_values = [fitness(ind) for ind in population]
    total_fitness = sum(fitness_values)
    selection_probs = [f / total_fitness for f in fitness_values]
    parent1 = population[np.random.choice(len(population), p=selection_probs)]
    parent2 = population[np.random.choice(len(population), p=selection_probs)]
    return parent1, parent2

def genetic_algorithm(n, population_size, mutation_rate, max_generations):
    population = create_population(population_size, n)
    max_fitness_history = []

    for generation in range(max_generations):
        population_fitness = [fitness(ind) for ind in population]
        max_fitness = max(population_fitness)
        max_fitness_history.append(max_fitness)
        if max_fitness == n:
            print(f"Оптимальное решение найдено в поколении {generation}")
            break

        new_population = []

        while len(new_population) < population_size:
            parent1, parent2 = select_parents(population)
            child1, child2 = crossover(parent1, parent2)
            child1 = mutate(child1, mutation_rate)
            child2 = mutate(child2, mutation_rate)
            new_population.append(child1)
            new_population.append(child2)

        population = new_population[:population_size]

    return max_fitness_history

max_fitness_history = genetic_algorithm(n, population_size, mutation_rate, max_generations)

plt.plot(max_fitness_history)
plt.xlabel('Поколение')
plt.ylabel('Максимальная приспособленность')
plt.title('Эволюция максимальной приспособленности')
plt.grid(True)
plt.show()
