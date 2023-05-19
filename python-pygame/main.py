import pygame
from itertools import repeat

from assets.src.player import Player
from assets.src.constants import Input, SCREEN_SIZE


pygame.init()

screen = pygame.display.set_mode([SCREEN_SIZE.x, SCREEN_SIZE.y])

player = Player()

all_actors = pygame.sprite.Group()
all_actors.add(player)

clock = pygame.time.Clock()

# Main Game Loop
running = True
while running:
    # Input
    for event in pygame.event.get():
        if event.type == Input.KEYDOWN:
            if event.key == Input.K_ESCAPE:
                running = False
        elif event.type == pygame.QUIT:
            running = False
    pressed_keys = pygame.key.get_pressed()

    # Update Physics
    player.update(pressed_keys)

    # Render Frame
    screen.fill((0, 0, 0))
    for actor in all_actors:
        screen.blit(actor.surface, actor.rect)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()