import pygame
from player import Player
from constants import *

def main():
    pygame.init()

    dt = 0
    clock = pygame.time.Clock()

    print('Starting asteroids!')
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')

    # screen: pygame.Surface
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # game loop
    while (True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # prerender update
        player.update(dt)

        screen.fill(color=(0, 0, 0))
        player.draw(screen)

        pygame.display.flip()

        # set framerate by pausing the game loop every 1/60 s
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()

