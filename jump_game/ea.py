"""
CISC 851 -- Group Project
 
"""

# imports
import statistics
import random

from fitness import fitness_calculation, pop_fitness_calculation
from crossover import crossover
from mutation import mutation
from parent_selection import ParentSelection
from survival_selection import survival_selection

from nn import Agent
from landscape import create_landscape
import obstacles
from constants import GRAVITY, TIME_INTERVAL
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from constants import BALL_COLOR, BALL_RADIUS, BALL_VELOCITY_X, BALL_VELOCITY_Y, BALL_X
from constants import OBSTACLE_GAP, OBSTACLE_HEIGHT, OBSTACLE_WIDTH, OBSTACLE_VELOCITY

from log import logging

params={"hidden_layer_nodes": 8, 
    "input_nodes": 4,
    "mut_rate": 0.2,
    "mutation_sigma":0.5,
    "mutation_type": 'onestep',
    "xover_rate": 0.5,
    "xover_exchange_rate": 0.2,
    "xover_type": 'sample',
    "fitness_mode": 'median',
    "popsize": 20,
    "tournament_size": 4,
    "parent_selection_type": "topK",
    "survival_selection_type": "replacement",
    "epoch": 500} 

def main(args):
    """Design the evolutionary algorithm
    Returns:
        np.ndarray: two np arrays which are the weights of the agent
    """
    hidden_layer_nodes, input_nodes, mut_rate, mutation_sigma, mutation_type, xover_rate, xover_exchange_rate, xover_type, fitness_mode, popsize, tournament_size, parent_selection_type, survival_selection_type, epoch = [v for k,v in args.items()]

    mating_pool_size = int(popsize*0.5)
    
    population = [Agent(input_nodes, hidden_layer_nodes, 2) for _ in range(popsize)]

    landscapes = [create_landscape(100) for _ in range(150)]
    for gen in range(epoch):
        pop_fitness = []
        for agent in population:
            agent.fitness = []
            for landscape in landscapes:
                agent.fitness.append(fitness_calculation(landscape, agent))
            pop_fitness.append(pop_fitness_calculation(fitness_mode, agent.fitness))
        # pick parents
        parents_index= ParentSelection(parent_selection_type, mating_pool_size, popsize, tournament_size, pop_fitness).selection()

        random.shuffle(parents_index)
        # reproduction
        offspring =[]
        offspring_fitness = []
        i = 0
        while len(offspring) < mating_pool_size:
        
            if random.random() < xover_rate:
                off1,off2 = crossover[xover_type](population[parents_index[i]], population[parents_index[i+1]], xover_exchange_rate)
            else:
                off1 = Agent(population[parents_index[i]].n_feature, population[parents_index[i]].n_hidden, population[parents_index[i]].n_out)
                off1.w_ih = population[parents_index[i]].w_ih
                off1.w_ho = population[parents_index[i]].w_ho
                off2 = Agent(population[parents_index[i]].n_feature, population[parents_index[i]].n_hidden, population[parents_index[i]].n_out)
                off2.w_ih = population[parents_index[i + 1]].w_ih
                off2.w_ho = population[parents_index[i + 1]].w_ho
            sigma = mutation_sigma / (gen + 1)
            mutation[mutation_type](off1, sigma)
            mutation[mutation_type](off2, sigma)

            off1.fitness = []
            off2.fitness = []
            for landscape in landscapes:
                off1.fitness.append(fitness_calculation(landscape, off1))
                off2.fitness.append(fitness_calculation(landscape, off2))
            offspring.append(off1)
            offspring.append(off2)
            offspring_fitness.append(pop_fitness_calculation(fitness_mode, off1.fitness))
            offspring_fitness.append(pop_fitness_calculation(fitness_mode, off2.fitness))

        population, pop_fitness = survival_selection[survival_selection_type](population, pop_fitness, offspring, offspring_fitness)
        logging.info(f"generation {gen} : best fitness {max(pop_fitness)}, average fitness {sum(pop_fitness)/len(pop_fitness)}")      
    
    logging.info("ea done..............")
    return 0

main(params)

