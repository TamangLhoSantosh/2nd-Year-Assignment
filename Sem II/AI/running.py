import pygame

# Initialize Pygame
pygame.init()

# Set the screen size
size = (1680, 920)
screen = pygame.display.set_mode(size)

# Load the running man image
man_image = pygame.image.load("Runningman.png")

# Set the starting position of the man
man_x = 0
man_y = 0

# Set the speed of the man
man_speed = 5

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Clear the screen
    screen.fill((255, 255, 255))
    
    # Move the man to the right
    man_x += man_speed
    
    # Check if the man has reached the edge of the screen
    if man_x > size[0]:
        man_x = 0
    
    # Draw the man on the screen
    screen.blit(man_image, (man_x, man_y))
    
    # Update the display
    pygame.display.flip()

# Exit Pygame
pygame.quit()