"""Result evaluation
"""
import os, json
import itertools
import numpy as np
import sys
import statistics
import math
import matplotlib.pyplot as plt

from landscape import create_landscape
from fitness import fitness_calculation, pop_fitness_calculation
from nn import Agent
import pandas as pd

from constants import NUMBER_OF_RUNNING
    
def read_file(path, name):
    """Read hyper parameters on current test
    
    Args:
        path (String): location of json file.
        name (String): name of the json file.
    """
    f = open(f"{path}/{name}")
    return json.load(f)

def draw_fitness_vs_generation(lst):
    """
    Args:
        lst (2D list): lst[0] is a list that saves the information of average fitness of each epoch for 1st parameter set
    """

  
  
if __name__ == "__main__":
    if len(sys.argv) == 0:
        print("Please assign test number for this test and run something like: python3 evaluation.py test1.")
        
    cur_dir = os.getcwd()
    main_path = f"{cur_dir}/test/{sys.argv[1]}"
    hyper_param = read_file(main_path, "hyper_parameters.json")
    param_combinations = list(itertools.product(*hyper_param.values()))
    num_combinations = len(param_combinations)
    epoch = hyper_param['epoch'][0]
    print(epoch)
    fitness_max = [[] for i in range(num_combinations)]
    fitness_mean = [[] for i in range(num_combinations)]
    for i in range(1, NUMBER_OF_RUNNING + 1, 1):
        base_path = f"{main_path}/test_{i}"
        for j in range(1, num_combinations + 1, 1):
            path = f"{base_path}/{j}"
            file_name = "output.json"
            if not os.path.exists(f"{path}/{file_name}"):
                print(f"Can not find output.json file in {path}.......")
                fitness_max[j - 1].append(120)
                fitness_mean[j - 1].append(120)
                continue
            data = read_file(path, file_name)
            fitness_max[j - 1].append(data["generated"][epoch - 1]["best fitness"])
            fitness_mean[j - 1].append(data["generated"][epoch - 1]["average fitness"])
    fitnessmax_mean = np.array([statistics.mean(i) for i in fitness_max])
    fitnessmax_std = np.array([math.sqrt(np.var(i)) for i in fitness_max])
    
    fitnessmean_mean = np.array([statistics.mean(i) for i in fitness_mean])
    fitnessmean_std = np.array([math.sqrt(np.var(i)) for i in fitness_mean])
    # Plot the data with error bars
    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
    ax1.errorbar(np.arange(1, num_combinations + 1), fitnessmax_mean, yerr=fitnessmax_std, fmt='o', capsize=4)

    # Add labels and title
    ax1.set_xlabel('Test set number')
    ax1.set_ylabel('Best fitness')
    ax1.set_title('Data with Error Bars')

    ax2.errorbar(np.arange(1, num_combinations + 1), fitnessmean_mean, yerr=fitnessmean_std, fmt='o', capsize=4)

    # Add labels and title
    ax2.set_xlabel('Test set number')
    ax2.set_ylabel('Mean fitness')
    ax2.set_title('Mean fitness with Error Bars')
    fig.suptitle('Max and Mean fitness plots')
    plt.show()

    

