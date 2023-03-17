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
OBSTACLE_HEIGHT = 200
OBSTACLE_COLOR = (0, 255, 0)
OBSTACLE_VELOCITY = 5
OBSTACLE_GAP = 200



params={"hidden_layer_nodes": 8, 
    "input_nodes": 4,
    "mut_rate": 0.2,
    "xover_rate": 0.5,
    "xover_exchange_rate": 0.2,
    "fitness_mode": 'median',
    "popsize": 20,
    "tournament_size": 4,
    "mutation_sigma":0.5,
    "epoch": 500,
    "parent_selection_type": "topK",
    "survival_selection_type": "replacement"
    }


