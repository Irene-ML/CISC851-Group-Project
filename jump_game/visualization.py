"""Visualization
"""

import random
import pygame, sys
import math
import numpy as np

from nn import Agent
from obstacles import Obstacle
from constants import GRAVITY, TIME_INTERVAL
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from constants import BALL_COLOR, BALL_RADIUS, BALL_VELOCITY_X, BALL_VELOCITY_Y
from constants import OBSTACLE_GAP, OBSTACLE_HEIGHT, OBSTACLE_WIDTH, OBSTACLE_VELOCITY


class Ball:
    """Create Ball object
    """
    def __init__(self, x, y, radius):
        """Initialize the Ball

        Args:
            x (int): location of the ball at x axis
            y (int): location of the ball at y axis
            radius (int): the radius of the ball
        """
        self.x = x
        self.y = y
        self.radius = radius
        self.speed_x = BALL_VELOCITY_X
        self.speed_y = -30

    def draw(self, screen):
        """Draw the ball as a circle on Surface

        Args:
            screen (pygame.Surface): the screen to display the game
        """
        pygame.draw.circle(screen, BALL_COLOR, (self.x, self.y), self.radius)



## TODO: Adding constraints for the collision state
def is_collision(ball, obstacle):
    """Define the condition when the ball and the obstacle have collisions

    Args:
        ball (Object Ball): A moving ball
        obstacle (Object Obstacle): A moving obstacle
    Returns:
        True if the ball hits the obstacle
        False otherwise
    """

    if ball.x >= obstacle.x - ball.radius and ball.x < obstacle.x:
        if ball.y - obstacle.y >= 0:
            print("collision condition 1 triggered......")
            return True
        else:
            if math.sqrt(math.pow(ball.x - obstacle.x, 2) + math.pow(ball.y - obstacle.y, 2)) <= ball.radius:
                print("collision condition 2 triggered......")
                return True
    elif ball.x > obstacle.x and ball.x < obstacle.x + obstacle.width:
        if (obstacle.y - ball.y <= ball.radius):
            print("collision condition 3 triggered......")
            return True
    elif ball.x >= obstacle.x + obstacle.width and ball.x < obstacle.x + obstacle.width + ball.radius:
        if math.sqrt(math.pow(ball.x - (obstacle.x + obstacle.width), 2) + math.pow(ball.y - obstacle.y, 2)) <= ball.radius:
            print("collision condition 4 triggered......")
            return True
        
    return False


## TODO: Controll the ball's movement in NN
def ball_control(ball, obstacles, agent):
    """Control the movement of the ball

    Args:
        ball (Object Ball): Moving the ball in the x and y directions
    """
    
    #ball.x += (ball.speed_x * TIME_INTERVAL)
    ball.y = min(SCREEN_HEIGHT - ball.radius, ball.y + ball.speed_y * TIME_INTERVAL + 0.5 * GRAVITY * TIME_INTERVAL * TIME_INTERVAL)

    if ball.y < SCREEN_HEIGHT - ball.radius:
        ball.speed_y += (GRAVITY * TIME_INTERVAL)
    else:
        features = []
        features.append(obstacles[0].height)
        features.append(obstacles[0].x - ball.x)
        features.append(-obstacles[0].speed)
        features.append(1)
        delta_v = agent.prediction(np.array(features))
        ball.speed_y = - delta_v[1]
        ball.spped_x = ball.speed_x + delta_v[0]
        obstacles[0].speed = -ball.speed_x
        obstacles[1].speed = -ball.speed_x
        #print(delta_v)

def main():
    # Initialize Pygame
    pygame.init()

    # Create the screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(type(screen))

    # Create the ball and obstacle and player
    ball = Ball(50, SCREEN_HEIGHT - BALL_RADIUS, BALL_RADIUS)
    obstacle1 = Obstacle(SCREEN_WIDTH, OBSTACLE_WIDTH, OBSTACLE_HEIGHT, -ball.speed_x)
    obstacle2 = Obstacle(obstacle1.x-obstacle1.width-OBSTACLE_GAP, OBSTACLE_WIDTH, OBSTACLE_HEIGHT, -ball.speed_x)
    agent = Agent(4, 8, 2)
    obstacles = [obstacle2, obstacle1]
    # Start the game loop
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        # find the next obstacle
        obstacle = obstacles[0]
        # Move the ball
        ball_control(ball, obstacles, agent)

        # Move the obstacles
        obstacle1.move()
        obstacle2.move()

        # If obstacle goes out of screen, reset its position
        obstacle1.update()
        obstacle2.update()
        if obstacles[0].x + OBSTACLE_WIDTH <= ball.x - ball.radius:
            tmp = obstacles[0]
            obstacles[0] = obstacles[1]
            obstacles[1] = tmp
        
        # Draw the screen
        screen.fill((0, 0, 0))
        ball.draw(screen)
        obstacle1.draw(screen)
        obstacle2.draw(screen)
        pygame.display.update()
        # Check for collision with obstacle
        if is_collision(ball, obstacle1):
            break
        if is_collision(ball, obstacle2):
            break

if __name__ == '__main__':
    main()
