# libs
from random import randint, uniform
from sys import exit
import math
import pygame

# simulation settings
GRAVITY = 0.05
generate_circles = 40
MAX_RADIUS = 40

# pygame & simulation limitation settings
FPS_LIM = 60
SIZE = 700
WSIZE = (SIZE, SIZE)

# init pygame
pygame.init()
pygame.display.set_caption("Bouncing balls!")
screen = pygame.display.set_mode(WSIZE)
clock = pygame.time.Clock()

class Circle:
    def __init__(self):
        self.radius = randint(10, MAX_RADIUS)
        self.pos = (randint(MAX_RADIUS, SIZE-MAX_RADIUS), randint(MAX_RADIUS, SIZE-MAX_RADIUS))
        self.vel = (uniform(0, 0.1), uniform(0, 0.1))
        self.color = (randint(32, 255), randint(32, 255), randint(32, 255))
    
    def collision(self, other):
        # source https://www.petercollingridge.co.uk/tutorials/pygame-physics-simulation/collisions/
        dx = other.pos[0] - self.pos[0]
        dy = other.pos[1] - self.pos[1]
        distance = math.hypot(dx, dy) # --> math.sqrt(dx**2 + dy**2)

        if distance < self.radius+other.radius:
            #print("collision!")
            tangent = math.atan2(dy, dx) # angle of vector
            angle = (0.5 * math.pi + tangent) # get shifted angle by 90 degrees
            
            self_x, self_y = self.vel
            other_x, other_y = other.vel

            # move vectors based on new angle
            self_x -= math.sin(angle)
            self_y += math.cos(angle)
            other_x += math.sin(angle)
            other_y -= math.cos(angle)

            self.vel = (self_x, self_y)
            self.update_pos()
            other.vel = (other_x, other_y)
            other.update_pos()

    def update_vel(self, vector):
        x,y = self.vel
        self.vel = (x+vector[0], y+vector[1])

    def update_pos(self):
        px, py = self.pos
        x, y = self.vel[0]+px, self.vel[1]+py
        self.pos = (x, y)

# generate circles

balls = [Circle() for _ in range(generate_circles)]
    
FPS = FPS_LIM
while 1:
    clock.tick(FPS)

    # pygame event (closing window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: # slow down sim
                FPS -= 10
                FPS == FPS_LIM if FPS <= 0 else FPS
    
    # update circles (physic)
    for b1 in balls:
        for b2 in balls:
            if b1 == b2: continue
            # bounce out of collision
            b1.collision(b2)

        # move down by gravity
        b1.update_vel((0, GRAVITY))

        # update pos
        b1.update_pos()

        # pos
        x, y = b1.pos

        # bounce of walls
        vx, vy = b1.vel
        if x+b1.radius > SIZE and vx != abs(vx) * -1: vx *= -1
        elif x-b1.radius < 0  and vx == abs(vx) * -1: vx *= -1
        if y+b1.radius > SIZE and vy != abs(vy) * -1: vy *= -1
        elif y-b1.radius < 0  and vy == abs(vy) * -1: vy *= -1
        b1.vel = (vx, vy)

        # update pos
        b1.update_pos()
        
    # draw circles and update display
    screen.fill((0, 0, 0))
    for b in balls:
        pygame.draw.circle(screen, b.color, b.pos, b.radius)
    pygame.display.flip()
