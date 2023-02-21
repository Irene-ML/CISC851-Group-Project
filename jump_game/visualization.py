"""Visualization
"""

import random
import pygame, sys
import math

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
        self.speed_x = 0
        self.speed_y = -30

    def draw(self, screen):
        """Draw the ball as a circle on Surface

        Args:
            screen (pygame.Surface): the screen to display the game
        """
        pygame.draw.circle(screen, BALL_COLOR, (int(self.x), int(self.y)), self.radius)



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
    if ball.x > obstacle.x and ball.x < obstacle.x + obstacle.width:
        if (obstacle.y - ball.y <= ball.radius):
            print("collision condition 3 triggered......")
            return True
    return False


## TODO: Controll the ball's movement in NN
def ball_control(ball):
    """Control the movement of the ball

    Args:
        ball (Object Ball): Moving the ball in the x and y directions
    """
    ball.x += (ball.speed_x * TIME_INTERVAL)
    if ball.speed_y != 0:
        ball.y = min(SCREEN_HEIGHT - BALL_RADIUS, ball.y + ball.speed_y * TIME_INTERVAL + 0.5 * GRAVITY * TIME_INTERVAL * TIME_INTERVAL)
        if ball.y == SCREEN_HEIGHT - BALL_RADIUS:
            ball.speed_y = 0
        else:
            ball.speed_y += (GRAVITY * TIME_INTERVAL)
    else:
        ball.y = SCREEN_HEIGHT - BALL_RADIUS
        ball.speed_y = -15 * BALL_VELOCITY_Y
    

def main():
    # Initialize Pygame
    pygame.init()

    # Create the screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(type(screen))

    # Create the ball and obstacle
    ball = Ball(50, SCREEN_HEIGHT - BALL_RADIUS, BALL_RADIUS)
    h1 = 10
    h2 = 20
    obstacle1 = Obstacle(SCREEN_WIDTH, SCREEN_HEIGHT - h1, OBSTACLE_WIDTH, h1, -1.5 * OBSTACLE_VELOCITY * TIME_INTERVAL)
    obstacle2 = Obstacle(obstacle1.x-obstacle1.width-OBSTACLE_GAP, SCREEN_HEIGHT - h2, OBSTACLE_WIDTH, h2, -1.5 * OBSTACLE_VELOCITY * TIME_INTERVAL)

    # Start the game loop
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Move the ball
        ball_control(ball)

        # Move the obstacles
        obstacle1.move()
        obstacle2.move() 

        # Check for collision with obstacle
        if is_collision(ball, obstacle1):
            break;
        
        if is_collision(ball, obstacle2):
            break
        # Bounce the ball if it hits the screen edges
        if ball.x + ball.radius > SCREEN_WIDTH or ball.x - ball.radius < 0:
            ball.speed_x = -ball.speed_x
        if ball.y + ball.radius > SCREEN_HEIGHT or ball.y - ball.radius < 0:
            ball.speed_y = -ball.speed_y

        # If obstacle goes out of screen, reset its position
        obstacle1.update()
        obstacle2.update()

        # Draw the screen
        screen.fill((0, 0, 0))
        ball.draw(screen)
        obstacle1.draw(screen)
        obstacle2.draw(screen)
        pygame.display.update()

if __name__ == '__main__':
    main()
