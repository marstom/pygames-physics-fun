import pygame
import scene

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
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
        elif event.type in [pygame.KEYDOWN, pygame.KEYUP]:
            gra.move(event)

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
