"""isualization
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
OBSTACLE_GAP = 200

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

    def update(self):
        """Update locations of the obstacle when the obstacle moves out of the screen
        """
        if self.x + self.width < 0:
            self.x = SCREEN_WIDTH - self.width
            self.height = random.randint(10, OBSTACLE_HEIGHT)
            self.y = SCREEN_HEIGHT - self.height
    
    def move(self):
        """Move the obstacle
        """
        self.x += self.speed

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
    if ball.x + ball.radius > obstacle.x and ball.x - ball.radius < obstacle.x + obstacle.width and ball.y + ball.radius > obstacle.y and ball.y - ball.radius < obstacle.y + obstacle.height:
            if ball.y < obstacle.y:
                return True
    else:
        return False

## TODO: Controll the ball's movement in NN
def ball_control(ball):
    """Control the movement of the ball

    Args:
        ball (Object Ball): Moving the ball in the x and y directions
    """
    ball.x += ball.speed_x
    ball.y += ball.speed_y


def main():
    # Initialize Pygame
    pygame.init()

    # Create the screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(type(screen))

    # Create the ball and obstacle
    ball = Ball(50, SCREEN_HEIGHT-50, BALL_RADIUS)
    obstacle1 = Obstacle(SCREEN_WIDTH, 200, OBSTACLE_WIDTH, OBSTACLE_HEIGHT, -OBSTACLE_VELOCITY)
    obstacle2 = Obstacle(obstacle1.x-obstacle1.width-OBSTACLE_GAP, 200, OBSTACLE_WIDTH, OBSTACLE_HEIGHT, -OBSTACLE_VELOCITY)

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
            ball.speed_y = -ball.speed_y

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