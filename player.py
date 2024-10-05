import pygame
from circleshape import CircleShape
from constants import (
    PLAYER_RADIUS,
    PLAYER_TURN_SPEED,
    PLAYER_SPEED,
    PLAYER_SHOOT_SPEED,
    PLAYER_SHOOT_COOLDOWN,
    SHOT_RADIUS
)
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)

        self.x = x
        self.y = y
        self.rotation = 0
        self.timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen: pygame.Surface):
        #                           color (white), list of pts, line width
        pygame.draw.polygon(screen, (255,255,255), self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]: # turn left
            self.rotate(-dt)
        if keys[pygame.K_d]: # turn right
            self.rotate(dt)
        if keys[pygame.K_w]: # move upwards
            self.move(dt)
        if keys[pygame.K_s]: # move downwards
            self.move(-dt)
        if keys[pygame.K_SPACE]: # shoot
            self.shoot()

        self.timer -= dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.timer <= 0.0:
            shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
            shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation)
            shot.velocity *= PLAYER_SHOOT_SPEED
            self.timer = PLAYER_SHOOT_COOLDOWN

