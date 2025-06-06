from circleshape import CircleShape
from constants import *
import pygame
import random

class Asteroid(CircleShape):
    containers = ()
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        rotate1 = pygame.Vector2(0, 1).rotate(random_angle)
        rotate2 = pygame.Vector2(0, 1).rotate(-random_angle)
        radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, radius)
        asteroid1.velocity = rotate1 * 1.2
        asteroid2.velocity = rotate2 * 1.2
