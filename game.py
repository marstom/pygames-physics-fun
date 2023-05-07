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


group_objects = pygame.sprite.Group()
gra = scene.Scene(group_objects)

# draw background
bg = pygame.image.load("assets/bg.jpeg")
bg = pygame.transform.scale(bg, (SCREEN_W, SCREEN_H))

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            print("keydown...")
            gra.key_down(event)
            if event.key == pygame.K_q:
                running = False
        if event.type == pygame.KEYUP:
            print("keyup...")
            gra.key_up(event)

    # get currently pressed and holded key
    # key = pygame.key.get_pressed()
    # print(key[pygame.K_w])

    # Update game state

    # Draw to the screen
    screen.fill((255, 255, 255))  # Fill the screen with white
    screen.blit(bg, (0,0))
    # Draw game objects here
    gra.render(screen)


    # Update the display
    pygame.display.flip()

    # Wait for the next frame
    clock.tick(60)  # Limit the frame rate to 60 FPS

# Clean up
pygame.quit()
