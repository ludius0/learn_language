"""
Programmed by @ludius0
"""
#MODULES
import pygame

#SCRIPTS
import chessboard as ch

# COLORS
WHITE = (255, 255, 255)
BLACK = (32, 32, 32)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)


def draw_board(s):
    x, y = 0, 0
    index_color = 0
    for i in range(8):
        for j in range(8):
            if (index_color % 2) == 0 or index_color == 0:
                pygame.draw.rect(s, WHITE,(x, y, 100, 100))
            else:
                pygame.draw.rect(s, BLACK,(x, y, 100, 100))
            index_color += 1
            x += 100
        index_color += 1
        y += 100
        x = 0
    

def draw_pieces(s):
    pygame.font.init()
    myfont = pygame.font.Font("segoe-ui-symbol.ttf", 82, Bold=True)
    x, y = 10, 0
    for i in chessboard.board:
        for j in i:
            if j != 0:
                if j.power in ch.pieces_list_b:
                    textsurface = myfont.render(f"{j.power}", True, RED)
                    screen.blit(textsurface,(x, y))
                elif j.power in ch.pieces_list_w:
                    textsurface = myfont.render(f"{j.power}", True, BLUE)
                    screen.blit(textsurface,(x, y))
            x += 100
        y += 100
        x = 10
    pygame.display.update()

def round_pos(x, y):
    if x > round(x, -2):
        x = round(x,-2)
    elif x < round(x, -2):
        x = x - 50
        x = round(x, -2)
    if y > round(y, -2):
        y = round(y,-2)
    elif y < round(y, -2):
        y = y - 50
        y = round(y, -2)
    return (x, y)
            
chessboard = ch.Chessboard()

pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("CHESS by ludius0")

selected_piece = None

player_playable_side = "white"

draw_board(screen)
draw_pieces(screen)

while 1:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            # SELECTING PIECE (GREEN RECT)
            if event.type == pygame.MOUSEBUTTONDOWN and selected_piece == None:
                # Get pos
                x, y = pygame.mouse.get_pos()
                x, y = round_pos(x, y)
                # Check if piece is on board
                if chessboard.board[int(y/100)][int(x/100)] != 0:
                    selected_piece = (int(x/100), int(y/100))
                    # Draw
                    draw_board(screen)
                    pygame.draw.rect(screen, GREEN,(x, y, 100, 100))
                    draw_pieces(screen)
                    pygame.display.update()
            
            # SELECTING PLACE & PLAYING MOVE               
            elif event.type == pygame.MOUSEBUTTONDOWN and selected_piece != None:
                # Get pos in board
                x0, y0 = pygame.mouse.get_pos()
                x0, y0 = round_pos(x0, y0)
                x0, y0 = int(x0/100), int(y0/100)
                x, y = (selected_piece)
                selected_piece = None
                # Swap
                player_playable_side = chessboard.swap_pos(x0, y0, x, y, player_playable_side)
                # Draw
                draw_board(screen)
                draw_pieces(screen)
                pygame.display.update()



