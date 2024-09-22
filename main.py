import pygame
from player import Player
from constants import *

def main():
    pygame.init()

    dt = 0
    clock = pygame.time.Clock()

    # groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    print('Starting asteroids!')
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')

    # screen: pygame.Surface
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # game loop
    while (True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # prerender update
        for u in updatable:
            u.update(dt)

        screen.fill(color=(0, 0, 0))
        for d in drawable:
            d.draw(screen)

        pygame.display.flip()

        # set framerate by pausing the game loop every 1/60 s
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()

