import pygame
from constants import *

def main():
    #Init import(s)
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        pygame.Surface.fill(screen, (255,255,255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            pygame.display.flip()


if __name__ == "__main__":
    main()