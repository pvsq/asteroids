import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface):
        #                          color (white), center (x, y), radius, line width
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        if self.radius > ASTEROID_MIN_RADIUS:
            random_angle = random.uniform(20, 50)
            rvec = self.velocity.rotate(random_angle)
            lvec = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            asteroid_r = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_l = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_r.velocity = rvec * 1.2
            asteroid_l.velocity = lvec * 1.2
        self.kill()

