

```py
import pygame

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Game")

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("Space bar pressed")

    # Update game state

    # Draw to the screen
    screen.fill((255, 255, 255))  # Fill the screen with white
    # Draw game objects here

    # Update the display
    pygame.display.flip()

# Clean up
pygame.quit()
```