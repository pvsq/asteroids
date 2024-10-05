import pygame
import sys

from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from constants import *

def main():
    pygame.init()

    dt = 0
    clock = pygame.time.Clock()

    # groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    print('Starting asteroids!')
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')

    # screen: pygame.Surface
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # associate object classes with Groups
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    # game loop
    while (True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # prerender update
        for u in updatable:
            u.update(dt)

        # check for collisions
        for a in asteroids:
            if player.collides_with(a):
                print("Game over!")
                sys.exit()

        screen.fill(color=(0, 0, 0))
        for d in drawable:
            d.draw(screen)

        pygame.display.flip()

        # set framerate by pausing the game loop every 1/60 s
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()

