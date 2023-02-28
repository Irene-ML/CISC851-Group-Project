"""Create landscapes
"""
from obstacles import Obstacle
from obstacles import Obstacle
from constants import GRAVITY, TIME_INTERVAL
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from constants import BALL_COLOR, BALL_RADIUS, BALL_VELOCITY_X, BALL_VELOCITY_Y, BALL_X
from constants import OBSTACLE_GAP, OBSTACLE_HEIGHT, OBSTACLE_WIDTH, OBSTACLE_VELOCITY
def create_landscapes(n):
    """
    Args:
        n (int): how many landscapes to be generated
    """
    return [Obstacle(BALL_X + OBSTACLE_GAP + OBSTACLE_GAP, OBSTACLE_WIDTH, OBSTACLE_HEIGHT, 0) for _ in range(n)]
