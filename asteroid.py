from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        color = (255, 255, 255)
        pygame.draw.circle(screen, color, self.position, self.radius, width=2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        child_1 = Asteroid(self.position.x, self.position.y, new_radius)
        child_2 = Asteroid(self.position.x, self.position.y, new_radius)
        child_1.velocity = self.velocity.rotate(random_angle) * 1.2
        child_2.velocity = self.velocity.rotate(-random_angle) * 1.2