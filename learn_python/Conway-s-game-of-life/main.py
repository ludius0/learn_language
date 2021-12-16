"""
Programmed by @ludius0
"""
# MODULES
import pygame

import board
import values as v

# CONSTANTS
H = v.H
W = v.W
C = v.C


# DRAWING
def draw_grid(screen, color):
    x, y = 0, 0
    for _ in range(H):
        x, y = x+C, y+C
        pygame.draw.line(screen, color, (x,0),(x,W))
        pygame.draw.line(screen, color, (0,y),(H,y))

def draw_rect(screen, x, y, color):
    pygame.draw.rect(screen, color, (x,y, C+1, C+1))

def draw_rect_from_board(screen, color, b):
    for i in b:
        x, y = i
        pygame.draw.rect(screen, color, (x,y, C+1, C+1))
    

# POSITIONS
def get_pos():
    x, y = pygame.mouse.get_pos()
    x, y = round_pos(x, y)
    return (x, y)

def round_pos(x, y):
    if x > round(x, -1):
        x = round(x,-1)
    elif x < round(x, -1):
        x = x - 5
        x = round(x, -1)
    if y > round(y, -1):
        y = round(y,-1)
    elif y < round(y, -1):
        y = y - 5
        y = round(y, -1)
    return (x, y)


# GAME
def game(screen):
    global World
    while True:
        screen.fill(v.BG)
 
        # End simulation
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                        pygame.quit()
                        
            pressed_key = pygame.key.get_pressed()
            if pressed_key[pygame.K_SPACE]:
                World.back_up_initiate()
                draw_rect_from_board(screen, v.RECT, World.board)
                pygame.display.update()
                return
            
        World.play_the_game()
        
        draw_rect_from_board(screen, v.RECT, World.board)
        draw_grid(screen, v.LINES)
        pygame.display.update()


def main():
    global World
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((H, W))
    pygame.display.set_caption("Conway's Game of Life by ludius0")
    screen.fill(v.BG)

    World = board.Board()

    clock = pygame.time.Clock()
    while True:
        pygame.time.delay(40)
        clock.tick(20)
        # Event
        for event in pygame.event.get():
            pressed_key = pygame.key.get_pressed()
            pressed_mouse = pygame.mouse.get_pressed()
            
            if event.type == pygame.QUIT:
                        pygame.quit()
            if pressed_mouse[0]:
                """
                Draw rect
                """
                x, y = get_pos()
                
                World.add_to_board(x, y)
                
                draw_rect(screen, x, y, v.RECT)
            if pressed_mouse[2]:
                """
                Delete rect
                """
                x, y = get_pos()

                World.remove_from_board(x, y)
                
                draw_rect(screen, x, y, v.BG)
            if pressed_key[pygame.K_SPACE]:
                """
                Play the game
                """
                World.back_up()
                game(screen)
        # Draw
        draw_grid(screen, v.LINES)
        pygame.display.update()
main()
