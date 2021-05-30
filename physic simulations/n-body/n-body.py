# libs
import pygame
import math
import sys
from random import randrange, seed
from numbers import Real

# simulation settings
G = 1
sum_mass = 50.0
softening = 100 # also function as speed component
seed(1)
# additional settings
COLLIS_MERGE = True
ACTIVE_BORDERS = False

# world objects
NBODIES = 150
BODIES = []

# pygame settings
COLOR = (255, 192, 64)
min_size = 0
wsize = (700, 700)

# init pygame
pygame.init()
screen = pygame.display.set_mode(wsize)


# support functions
def check_borders(body, min=min_size, max=wsize[0]):
    for index, (p, v) in enumerate(zip(body.pos, body.vel)):
        if p+v <= 0:
            b.vel[index] = -v
        elif p+v >= wsize[1]:
            b.vel[index] = -v

def create_rand_vec3(min=min_size, max=500, regulate=1):
    return [randrange(min, max) / regulate, randrange(min, max) / regulate, randrange(min, max) / regulate]

# physic object
class Body:
    def __init__(self, mass: float, position: list, velocity: list):
        assert isinstance(mass, Real) and isinstance(position, list) and isinstance(velocity, list)
        assert len(position) == 3 and len(velocity) == 3

        self.mass = mass
        self.pos = position
        self.vel = velocity
        self.dvel = [0., 0., 0.]
        self.collision = False
        self.volume = 5
        self.radius = 1.06
    
    def fg(self, other):
        assert isinstance(other, Body)

        # distance between two bodies
        x_ = other.pos[0] - self.pos[0]
        y_ = other.pos[1] - self.pos[1]
        z_ = other.pos[2] - self.pos[2]
        distance = [x_, y_, z_]
        r = math.sqrt(x_**2 + y_**2 + z_**2)

        # collision
        error = abs(x_)+abs(y_)+abs(z_)
        if error <= 1:
            print("Collision!")
            other.collision = True

        # compute Newton law based on distance F=G*(m1*m2)/r (with some regulation for each axis)
        for index in range(3):
            f = (G * self.mass * other.mass / r**2) * distance[index] #/ r * softening
            self.dvel[index] = self.dvel[index] + f / self.mass
    
    def comp_radius(self, other):
        self.volume += other.volume
        self.radius = (self.volume * 3 / 4 * math.pi)**(1/3)
    
    def update(self):
        # Velocity and delta velocity
        self.vel = [self.vel[0]+self.dvel[0], self.vel[1]+self.dvel[1], self.vel[2]+self.dvel[2]]
        self.dvel = [0., 0., 0.]

        x = self.pos[0] + self.vel[0]
        y = self.pos[1] + self.vel[1]
        z = self.pos[2] + self.vel[2]
        self.pos = [x, y, z]

# generate bodies
mass = sum_mass / NBODIES
for n in range(NBODIES):
    BODIES.append(Body(mass, create_rand_vec3(min=min_size+100, max=wsize[0]-100), create_rand_vec3(min=-1, max=1, regulate=10)))

# Event loop
while 1:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            break
    
    # update simulation
    for b1 in BODIES:
        for index, b2 in enumerate(BODIES):
            # if b1 and b2 are same than ignore
            if b1 == b2:
                continue
            # calculate Newton law
            b1.fg(b2)
            # check for collision
            if b2.collision == True and COLLIS_MERGE == True:
                # delete one body and update velocity & mass of second one
                b1.mass += b2.mass
                b1.vel = [b1.vel[0]+b2.vel[0], b1.vel[1]+b2.vel[1], b1.vel[2]+b2.vel[2]]
                b1.comp_radius(b2)
                BODIES.remove(b2)

    # update every pos
    for b in BODIES:
        if ACTIVE_BORDERS == True:
            check_borders(b)
        b.update()
    
    # draw with pygame
    for b in BODIES:
        pygame.draw.circle(screen, COLOR, (b.pos[0], b.pos[1]), b.radius)
    pygame.display.update()
    pygame.display.flip()
pygame.quit()
