import pygame
from time import sleep

import values as v

H = v.H
C = v.C

"""
RULES
1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
2. Any live cell with two or three live neighbours lives on to the next generation.
3. Any live cell with more than three live neighbours dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
"""

class Board:
    def __init__(self):
        # storage of alive cells
        self.board = []

    def add_to_board(self, x, y):
        if (x, y) in self.board:
            return
        self.board.append((x, y))
        self.board = sorted(self.board)
        #print(self.board)

    def remove_from_board(self, x, y):
        for n, i in enumerate(self.board):
            if i == (x, y):
                self.board.pop(n)
                #print(self.board)
                return

    def back_up(self):
        self.board_back_up = self.board

    def back_up_initiate(self):
        self.board = self.board_back_up
    

    def check_rules(self, cell, nc):
        cell_alive = False

        # Find if cell is alive or not
        if cell in self.board:
            cell_alive = True

        # if cell is alive (rule: 1, 2, 3)
        if nc == 3 and cell_alive == False:                 # Rule four
            self.new_cells.append(cell)
        elif nc < 2 and cell_alive == True:                 # Rule one
            self.dead_cells.append(cell)
        elif (nc == 2 or nc == 3) and cell_alive == True:   # Rule two
            pass
        elif nc > 3 and cell_alive == True:                 # Rule three
            self.dead_cells.append(cell)
        return
            
    def check_neighbours(self, cell):
        x, y = cell
        n_cells = 0
        
        self.neighbours = [
            (x-C, y-C), (x, y-C), (x+C, y-C),
            (x-C, y), (x+C, y),
            (x-C, y+C), (x, y+C), (x+C, y+C)
            ]

        for i in self.neighbours:
            if i in self.board:
                n_cells += 1

        self.check_rules(cell, n_cells)
                    
    def play_the_game(self):
        self.new_cells = []
        self.dead_cells = []

        # Check all cells
        for i in range(0, H, C):
            for j in range(0, H, C):
                cell = (j, i)
                
                self.check_neighbours(cell)


        # Delete cells
        for j in self.dead_cells:
            self.board.remove(j)

        # Add cells
        for i in self.new_cells:
            self.board.append(i)

        self.board = sorted(self.board)
