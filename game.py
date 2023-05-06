import pygame
import scene
from constatnts import SCREEN_H, SCREEN_W
# Initialize Pygame
pygame.init()

# Set up the display
screen_width = SCREEN_W
screen_height = SCREEN_H
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Game")

# Set up the clock
clock = pygame.time.Clock()

# Game loop
running = True


sprites = pygame.sprite.Group()
gra = scene.Scene(sprites)

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            gra.move(event)
            if event.key == pygame.K_q:
                running = False
        if event.type == pygame.KEYUP:
            gra.stop(event)

    # Update game state

    # Draw to the screen
    screen.fill((255, 255, 255))  # Fill the screen with white
    # Draw game objects here
    gra.render(screen)


    # Update the display
    pygame.display.flip()

    # Wait for the next frame
    clock.tick(60)  # Limit the frame rate to 60 FPS

# Clean up
pygame.quit()
