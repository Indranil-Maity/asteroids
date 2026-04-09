import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 
        else:
            log_event("asteroid_split")
            ang = random.uniform(20, 50)
            
            v1 = self.velocity.rotate(ang)
            v2 = self.velocity.rotate(-ang)
            
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            
            first_ast = Asteroid(self.position.x, self.position.y, new_radius)
            second_ast = Asteroid(self.position.x, self.position.y, new_radius)
            
            first_ast.velocity = v1 * 1.2
            second_ast.velocity = v2 * 1.2
