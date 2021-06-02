# libs
import numpy as np
import math
import pygame
from sys import exit


# define CUBE in 3D space (# middle for rotation is [0, 0, 0])
vertexes = []
vertexes.append(np.matrix([-1, -1, 1], dtype=float))
vertexes.append(np.matrix([1, -1, 1], dtype=float))
vertexes.append(np.matrix([1, 1, 1], dtype=float))
vertexes.append(np.matrix([-1, 1, 1], dtype=float))
vertexes.append(np.matrix([-1, -1, -1], dtype=float))
vertexes.append(np.matrix([1, -1, -1], dtype=float))
vertexes.append(np.matrix([1, 1, -1], dtype=float))
vertexes.append(np.matrix([-1, 1, -1], dtype=float))

projection_cube = np.matrix([
    [1, 0, 0], 
    [0, 1, 0],
    [0, 0, 1]
])

# variables
SCALE= 100
ANGLE = 0.
SIZE = (700, 700)
MOVE = (SIZE[0]//2, SIZE[1]//2) # center of screen
BG_C = (0, 0, 0) # black
LINES_C = (255, 255, 255) # white
VERTX_C = (11, 232, 129) # some green

# Init pygame
pygame.display.set_caption("Beautiful 3D cube")
screen = pygame.display.set_mode(SIZE)

# draw
def draw_lines(i, j, vertexes):
    pygame.draw.line(screen, LINES_C, (vertexes[i][0], vertexes[i][1]), (vertexes[j][0], vertexes[j][1]))

clock = pygame.time.Clock()
while 1:
    # default pygame settings
    clock.tick(60)
    screen.fill(BG_C)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            break
    
    # compute rotation
    ANGLE += 0.01
    rotation_x = np.matrix([
        [1, 0, 0],
        [0, math.cos(ANGLE), -math.sin(ANGLE)],
        [0, math.sin(ANGLE), math.cos(ANGLE)]
    ], dtype=float)
    rotation_y = np.matrix([
        [math.cos(ANGLE), 0, math.sin(ANGLE)],
        [0, 1, 0],
        [-math.sin(ANGLE), 0, math.sin(ANGLE)]
    ], dtype=float)
    rotation_z = np.matrix([
        [math.cos(ANGLE), -math.sin(ANGLE), 0],
        [math.sin(ANGLE), math.cos(ANGLE), 0],
        [0, 0, 1]
    ], dtype=float)

    projections = []
    for idx, vertex_row in enumerate(vertexes):
        # multiplay vertexes with a rotation
        rotated = np.dot(rotation_x, vertex_row.T)
        rotated = np.dot(rotation_y, rotated)
        rotated = np.dot(rotation_z, rotated)

        # get new rotated cube
        projected2d = np.dot(projection_cube, rotated)

        # ignore z
        x = int(projected2d[0][0] * SCALE + MOVE[0])
        y = int(projected2d[1][0] * SCALE + MOVE[1])

        # save
        projections.append((x, y))
        
        # draw small blue circles around vertexes
        pygame.draw.circle(screen, VERTX_C, (x, y), 5)
    
    # draw lines based on rotation
    for p in range(4):
        draw_lines(p, (p+1) % 4, projections)
        draw_lines(p+4, ((p+1) % 4) + 4, projections)
        draw_lines(p, (p+4), projections) 


    #ANGLE = 0 if ANGLE >= math.pi*2 else ANGLE
    
    pygame.display.update()

