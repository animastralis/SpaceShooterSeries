import pygame
from pygame import Vector2

from assets.src.constants import Input, SCREEN_SIZE

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surface = pygame.image.load("assets/art/player_ship.png")
        self.surface = pygame.transform.rotate(self.surface, -90)
        self.rect = self.surface.get_rect()

        self.velocity = 10.0
    
    def update(self, pressed_keys: dict) -> None:
        # Handle movement
        move_dir = Vector2(0, 0)
        if pressed_keys[Input.K_LEFT]:
            move_dir.x -= 1
        if pressed_keys[Input.K_RIGHT]:
            move_dir.x += 1
        if pressed_keys[Input.K_UP]:
            move_dir.y -= 1
        if pressed_keys[Input.K_DOWN]:
            move_dir.y += 1

        if move_dir != Vector2(0, 0):
            self.move(move_dir)
        
        # Keep player in bounds
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 400:
            self.rect.right = 400
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_SIZE.y:
            self.rect.bottom = SCREEN_SIZE.y

    
    def move(self, move_dir: Vector2) -> None:
        movement = move_dir * self.velocity
        self.rect.move_ip(movement.x, movement.y)
