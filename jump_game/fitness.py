"""calculate fitness
"""
from nn import Agent
from nn import Agent
from obstacles import Obstacle
from constants import GRAVITY, TIME_INTERVAL
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from constants import BALL_COLOR, BALL_RADIUS, BALL_VELOCITY_X, BALL_VELOCITY_Y, BALL_X
from constants import OBSTACLE_GAP, OBSTACLE_HEIGHT, OBSTACLE_WIDTH, OBSTACLE_VELOCITY

def fitness_calculation(landscape, agent):
    """
    Args:
        landscape (list): a list of obstacles
        agent (nn): neural network model
    """
