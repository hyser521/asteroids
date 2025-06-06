import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from astroidfield import AsteroidField
from shot import Shot

def main():
    #Init import(s)
    pygame.init()
    
    #pygame groups/objects/variables
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroid = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    #Player
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    Shot.containers = (updatable, shots, drawable)
    #Asteroid
    Asteroid.containers = (asteroid, drawable, updatable)
    #Asteroid Field
    AsteroidField.containers = (updatable)
    AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)
        for collision in asteroid:
            if(collision.check_collision(player)):
                print("Game over!")
                exit()
        for collision in asteroid:
            for opportunity in shots:
                if(collision.check_collision(opportunity)):
                    collision.kill()
                    opportunity.kill()
                    
        pygame.Surface.fill(screen, (0,0,0))
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()