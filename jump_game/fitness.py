"""calculate fitness
"""
from nn import Agent
from ball import Ball

from obstacles import Obstacle
from constants import GRAVITY, TIME_INTERVAL
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from constants import BALL_COLOR, BALL_RADIUS, BALL_VELOCITY_X, BALL_VELOCITY_Y, BALL_X
from constants import OBSTACLE_GAP, OBSTACLE_HEIGHT, OBSTACLE_WIDTH, OBSTACLE_VELOCITY
from visualizatoin import is_collision, ball_control

def fitness_calculation(landscape, agent):
    """
    Args:
        landscape (list): a list of obstacles
        agent (nn): neural network model
    """
    cur_obstacle_id = 0
    ball = Ball(BALL_X, SCREEN_HEIGHT - BALL_RADIUS, BALL_RADIUS)

    while True
        ball_control(ball, landscape[cur_obstacle_id:], agent)
        landscape[cur_obstacle_id].speed = - ball.speed_x
        landscape[cur_obstacle_id].move()
        if is_collision(ball, landscape[cur_obstacle_id]):
            return cur_obstacle_id
            
        if obstacles[0].x + OBSTACLE_WIDTH <= ball.x - ball.radius:
            cur_obstacle_id += 1
        if cur_obstacle_id == len(landscape):
            return cur_obstacle_id
