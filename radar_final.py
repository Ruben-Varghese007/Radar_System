import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 1080, 960
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Radar Display")

# Colors
black = (0, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)

# Radar parameters
radar_center = (width // 2, height // 2)
max_range = min(width, height) // 2 - 80
angle = 0
angular_velocity = 0.5
grid_spacing = 40

# Font for degree labels
font = pygame.font.Font(None, 36)

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

    # Draw radial lines and angle labels on the outer ring
    if max_range > 80:
        for degrees in range(0, 360, 30):
            radian_angle = math.radians(degrees)
            label_x = radar_center[0] + (max_range + 20) * math.cos(radian_angle)
            label_y = radar_center[1] - (max_range + 20) * math.sin(radian_angle)
            line_start = radar_center
            line_end = (label_x, label_y)
            degree_text = font.render(str(degrees) + "°", True, white)
            text_rect = degree_text.get_rect(center=(label_x, label_y))
            screen.blit(degree_text, text_rect)
            pygame.draw.line(screen, green, line_start, line_end, 2)

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














