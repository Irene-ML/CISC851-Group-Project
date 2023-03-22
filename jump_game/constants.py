import numpy as np

# Define some constants
GRAVITY = 10
TIME_INTERVAL = 0.02

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

BALL_RADIUS = 10
BALL_COLOR = (255, 0, 0)
BALL_X = 100
BALL_VELOCITY_X = 30
BALL_VELOCITY_Y = 5

OBSTACLE_WIDTH = 50
OBSTACLE_HEIGHT = 150
OBSTACLE_COLOR = (0, 255, 0)
OBSTACLE_VELOCITY = 5
OBSTACLE_GAP = 200

HYPER_PARAMS = {"hidden_layer_nodes": [8, 9],
    "input_nodes": [4],
    "mut_rate": [0.2],
    "mutation_sigma": [0.5],
    "mutation_type": ['onestep'],
    "xover_rate": [0.5],
    "xover_exchange_rate": np.arange(0, 0.4, 0.2),
    "xover_type": ['sample'],
    "fitness_mode": ['median','mean'],
    "popsize": [20],
    "tournament_size": [4],
    "parent_selection_type": ["topK", "MPS", "tournament", "random_uniform"],
    "survival_selection_type": ["replacement", "mu_plus_lambda", "random_uniform"],
    "epoch": [500],
    "obstacle_number": [100],
    "landscape_size": [150]} 


