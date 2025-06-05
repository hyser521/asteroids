import pygame
from constants import *

def main():
    #Init import(s)
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        pygame.Surface.fill(screen, (0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            pygame.display.flip()
            dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()