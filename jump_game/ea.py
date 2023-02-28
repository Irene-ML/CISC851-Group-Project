"""
CISC 851 -- Group Project
 
"""

# imports
import statistics
import random

import fitness
import crossover
import mutation
import parent_selection
import survival_selection

from nn import Agent
from landscape import create_landscape
import obstacles
from constants import GRAVITY, TIME_INTERVAL
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from constants import BALL_COLOR, BALL_RADIUS, BALL_VELOCITY_X, BALL_VELOCITY_Y, BALL_X
from constants import OBSTACLE_GAP, OBSTACLE_HEIGHT, OBSTACLE_WIDTH, OBSTACLE_VELOCITY


def main():
    """Design the evolutionary algorithm

    Args:
        args (_type_): _description_

    Returns:
        np.ndarray: two np arrays which are the weights of the agent
    """
    hidden_layer_nodes = 8
    input_nodes = 4
    mut_rate = 0.2
    fitness_mode = 'median'
    popsize = 20
    mating_pool_size = int(popsize*0.5) # has to be even
    tournament_size = 4
    population = [Agent(input_nodes, hidden_layer_nodes, 2) for _ in range(popsize)]
    

    for gen in range(4):
        landscapes = [create_landscape(100) for _ in range(5)]
        pop_fitness = []
        for agent in population:
            agent.fitness = []
            for landscape in landscapes:
                agent.fitness.append(fitness.fitness_calculation(landscape, agent))
            pop_fitness.append(statistics.median(agent.fitness))
        # pick parents
        # parents_index = parent_selection.MPS(pop_fitness, mating_pool_size)
        parents_index = parent_selection.tournament(pop_fitness, mating_pool_size, tournament_size)
        # parents_index = parent_selection.random_uniform(popsize, mating_pool_size)
        random.shuffle(parents_index)
        print(parents_index)
        # reproduction
        offspring =[]
        offspring_fitness = []
        
    print("ea done..............")
    return 0

main()

