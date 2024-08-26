import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 1080, 760
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Radar Display")

# Colors
black = (0, 0, 0)
green = (0, 255, 0)

# Radar parameters
radar_center = (width // 2, height // 2)
max_range = min(width, height) // 2 - 20
angle = 0
angular_velocity = 0.5  # Adjust for a slower rotation
grid_spacing = 40

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(black)

    # Draw grid lines
    for r in range(grid_spacing, max_range + grid_spacing, grid_spacing):
        pygame.draw.circle(screen, green, radar_center, r, 1)

    # Draw the radar circle
    pygame.draw.circle(screen, green, radar_center, max_range, 2)

    # Calculate the position of the line
    x = radar_center[0] + max_range * math.cos(math.radians(angle))
    y = radar_center[1] - max_range * math.sin(math.radians(angle))

    # Draw the line
    pygame.draw.line(screen, green, radar_center, (x, y), 2)

    # Update the display
    pygame.display.flip()

    # Rotate the line
    angle += angular_velocity
    if angle >= 360:
        angle = 0

    # Control the frame rate to slow down the animation
    pygame.time.delay(10)  # Adjust the delay as needed for the desired speed

# Quit Pygame
pygame.quit()
sys.exit()