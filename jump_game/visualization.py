"""_description_
"""

import random
import pygame, sys

# Define some constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

BALL_RADIUS = 10
BALL_COLOR = (255, 0, 0)
BALL_VELOCITY_X = 3
BALL_VELOCITY_Y = 5

OBSTACLE_WIDTH = 50
OBSTACLE_HEIGHT = 200
OBSTACLE_COLOR = (0, 255, 0)
OBSTACLE_VELOCITY = 5


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
        self.speed_x = random.randint(0, BALL_VELOCITY_X)
        self.speed_y = random.randint(0, BALL_VELOCITY_Y)

    def draw(self, screen):
        """Draw the ball as a circle on Surface

        Args:
            screen (pygame.Surface): the screen to display the game
        """
        pygame.draw.circle(screen, BALL_COLOR, (int(self.x), int(self.y)), self.radius)

    def move():
        return


class Obstacle:
    """Create Obstacle object
    """
    def __init__(self, x, y, width, height, speed):
        """Initialize the Ball

        Args:
            x (int): location of the obstacle at x axis
            y (int): location of the obstacle at y axis
            width (int): the width of the obstacle
            height (int): the height of the obstacle
            speed (int): the moving speed of the obstacle
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed

    def draw(self, screen):
        """Draw Obstacle as rectangular on Surface

        Args:
            screen (pygame.Surface): the screen to display the game
        """
        pygame.draw.rect(screen, OBSTACLE_COLOR, (self.x, self.y, self.width, self.height))
   

def main():
    # Initialize Pygame
    pygame.init()

    # Create the screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(type(screen))

    # Create the ball and obstacle
    ball = Ball(50, SCREEN_HEIGHT-50, BALL_RADIUS)
    obstacle = Obstacle(300, 200, OBSTACLE_WIDTH, OBSTACLE_HEIGHT, -OBSTACLE_VELOCITY)

    # Start the game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Move the ball
        ball.x += ball.speed_x
        ball.y += ball.speed_y

        # Move the obstacle
        obstacle.x += obstacle.speed

        # Check for collision with obstacle
        if ball.x + ball.radius > obstacle.x and ball.x - ball.radius < obstacle.x + obstacle.width and ball.y + ball.radius > obstacle.y and ball.y - ball.radius < obstacle.y + obstacle.height:
            if ball.y < obstacle.y:
                ball.speed_y = -ball.speed_y

        # Bounce the ball if it hits the screen edges
        if ball.x + ball.radius > SCREEN_WIDTH or ball.x - ball.radius < 0:
            ball.speed_x = -ball.speed_x
        if ball.y + ball.radius > SCREEN_HEIGHT or ball.y - ball.radius < 0:
            ball.speed_y = -ball.speed_y

        # If obstacle goes out of screen, reset its position
        if obstacle.x + obstacle.width < 0:
            obstacle.x = SCREEN_WIDTH - obstacle.width

        # Draw the screen
        screen.fill((0, 0, 0))
        ball.draw(screen)
        obstacle.draw(screen)
        pygame.display.update()

if __name__ == '__main__':
    main()