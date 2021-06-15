### libs
import pygame
import sys
import math

## defined pendulum
mass1 = 10
mass2 = 10
lenght1 = 150
lenght2 = 150
angle1 = math.pi * 3 / 4
angle2 = math.pi * 3 / 4
# velocity
angle1_vel = 0 
angle2_vel = 0

## physic
G = 1

## sims predefined variables
size = 700
posx = size // 2
posy= size // 2 
wsize = (size, size)
radius = 10
stroke = 4
FPS = 60

## init pygame stuff
pygame.init()
screen = pygame.display.set_mode(wsize)
pygame.display.set_caption("Pendulum")
clock = pygame.time.Clock()

# colors
LENGHT = (255, 255, 255)
POINT = (255, 0, 0)

# computing functions
# source: https://www.myphysicslab.com/pendulum/double-pendulum-en.html
def Angle1Acc(a1, a2, m1, m2, L1, L2, G, v1, v2):
    num1 = -G * (2 * m1 + m2) * math.sin(a1)
    num2 = -m2 * G * math.sin(a1 - 2 * a2)
    num3 = -2 * math.sin(a1 - a2)
    num4 =  m2 * ((v2 * v2) * L2 + (v1 * v1) * L1 * math.cos(a1 - a2))
    numerator = num1 + num2 + (num3 * num4)
    denominator = L1 * (2 * m1 + m2 - m2 * math.cos(2 * a1 - 2 * a2))
    return numerator / denominator

def Angle2Acc(a1, a2, m1, m2, L1, L2, G, v1, v2):
    num1 = 2 * math.sin(a1 - a2)
    num2 = (v1 * v1) * L1 * (m1 + m2) + G * (m1 + m2) * math.cos(a1)
    num3 = (v2 * v2) * L2 * m2 * math.cos(a1 - a2)
    numerator = num1 * (num2 + num3)
    denominator = L2 * (2 * m1 + m2 - m2 * math.cos(2 * a1 - 2 * a2))
    return numerator / denominator

## event loop (for pygame)
while 1:
    clock.tick(FPS)

    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    ## physic stuff
    # position of first and second joint
    x1 = posx + math.sin(angle1) * lenght1
    y1 = posy + math.cos(angle1) * lenght1
    x2 = x1 + math.sin(angle2) * lenght2
    y2 = y1 + math.cos(angle2) * lenght2

    # angle acceleration & velocity & update
    angle1_acc = Angle1Acc(angle1, angle2, mass1, mass2, lenght1, lenght2, G, angle1_vel, angle2_vel)
    angle2_acc = Angle2Acc(angle1, angle2, mass1, mass2, lenght1, lenght2, G, angle1_vel, angle2_vel)

    angle1_vel += angle1_acc
    angle1 += angle1_vel

    angle2_vel += angle2_acc
    angle2 += angle2_vel

    # pygame draw functions
    pos0 = (posx, posy)
    pos1 = (x1, y1)
    pos2 = (x2, y2)

    pygame.draw.circle(screen, POINT, pos0, radius)
    pygame.draw.line(screen, LENGHT, pos0, pos1, stroke)
    pygame.draw.circle(screen, POINT, pos1, radius)
    pygame.draw.line(screen, LENGHT, pos1, pos2, stroke)
    pygame.draw.circle(screen, POINT, pos2, radius)
    
    pygame.display.flip()