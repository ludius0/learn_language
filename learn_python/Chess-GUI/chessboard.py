import pygame
import pieces as p

# Unicode
pieces_dict_b = {"K": "\u265A", "Q":"\u265B", "R":"\u265C", "B":"\u265D", "KN":"\u265E", "P":"\u265F"}
pieces_list_b = ["\u265A", "\u265B", "\u265C", "\u265D", "\u265E", "\u265F"]
#pieces_power_list_b = ["K", "Q", "R", "B", "KN", "P"]

pieces_dict_w = {"k": "\u2654", "q": "\u2655","r":"\u2656", "b":"\u2657", "kn":"\u2658", "p":"\u2659"}
pieces_list_w = ["\u2654", "\u2655", "\u2656", "\u2657", "\u2658", "\u2659"]
#pieces_power_list_w = ["k", "q", "r", "b", "kn", "p"]



class Chessboard():
    def __init__(self):
        self.generate_board()
        self.set_up_board()
        #self.print_board()

    def generate_board(self):
        self.board = []
        for i in range(8):
            row = []
            self.board.append(row)
            for j in range(8):
                self.board[i].append(0)

    def looking_for_pos(self, piece):
        for iy, i in enumerate(self.board):
            for ix, j in enumerate(i):
                if j == piece:
                    x = ix
                    y = iy
                    return (x, y)

    def check_pawn_special_move(self):
        for y, i in enumerate(self.board):
            for j in i:
                if j != 0 and (j.power == "\u2659" or j.power == "\u265F"):
                    if y < 4 and j.side == "white":
                        j.pawn_special_move = False
                    elif y > 3 and j.side == "black":
                        j.pawn_special_move = False
                
    def swapping(self, x0, y0, x1, y1, opponent_side, own_side, king, pawn, rook=None, special_case=False):
        player_side = opponent_side                                                         # Black player is playing next round

        self.board[y0][x0], self.board[y1][x1] = self.board[y1][x1], self.board[y0][x0]     # Swap
        deleted_piece = self.board[y1][x1]
        self.board[y1][x1] = 0                                                              # Delete swapped second piece
        
        # Get pos of king
        x, y = self.looking_for_pos(king)
        
        # Check if white has still check; if yes than move was invalid
        if king.check_for_checks(self, x, y) == True:                                # If white king has still check; than that move won't count
            player_side = own_side
            self.board[y0][x0], self.board[y1][x1] = deleted_piece, self.board[y0][x0]                                                            # Swap back
            
        # Support code
        # Upgrade Pawn
        if y0 == 0 and self.board[y0][x0].power == pawn:                  
                self.board[y0][x0].ask_for_upgrade(self, self.board[y0][x0], x0, y0)
        else:   # If move was valid; check if pawn special move can be valid
            self.check_pawn_special_move()
        return player_side

    def swapping_king_and_rook(self, x0, y0, x1, y1, opponent_side, own_side, king, rook):
            player_side = opponent_side                                                         
            self.board[y1][x1], self.board[y0][x0] = king, rook
            x, y = self.looking_for_pos(king)
            king.first_move = True
            rook.first_move = True
            if king.check_for_checks(self, x, y) == True:                                
                player_side = own_side
                king.first_move = False
                rook.first_move = False
            else:
                self.check_pawn_special_move()
            return player_side

    def swap_pos(self, x0, y0, x1, y1, player_side):
        a = self.board[y1][x1]      # First piece
        b = self.board[y0][x0]      # Second piece
        
        # White
        if player_side == "white":                                         
            if a.power in pieces_list_w and (b == 0 or b.side != "white"):                              # If first selected piece is white and replacing piece is black
                if a.possible_moves(self, x0, y0, x1, y1) == True:                                      # If move is valid (check in pieces.py)
                    player_side = self.swapping(x0, y0, x1, y1, "black", "white", self.w_king, "\u2659")
                    
            # Special move with swapping with rock and king
            elif a.power == "\u2654" and b.power == "\u2656":
                if self.board[7][1] == 0 and self.board[7][2] == 0 and self.board[7][3] == 0:
                    if self.w_king.first_move == None and self.w_rock1.first_move == None:
                        player_side = "black"
                        self.board[7][0], self.board[7][4] = 0, 0
                        x0, y0, x1, y1 = 2, 7, 1, 7
                        player_side = self.swapping_king_and_rook(x0, y0, x1, y1, "black", "white", self.w_king, self.w_rock1)
                        if player_side == "white":
                            self.board[7][0], self.board[7][4], self.board[y1][x1], self.board[y0][x0] = self.w_rock1, self.w_king, 0, 0
                elif self.board[7][5] == 0 and self.board[7][6] == 0:
                    if self.w_king.first_move == None and self.w_rock2.first_move == None:
                        player_side = "black"
                        self.board[7][7], self.board[7][4] = 0, 0
                        x0, y0, x1, y1 = 5, 7, 6, 7
                        player_side = self.swapping_king_and_rook(x0, y0, x1, y1, "black", "white", self.w_king, self.w_rock1)
                        if player_side == "white":
                            self.board[7][7], self.board[7][4], self.board[y1][x1], self.board[y0][x0] = self.w_rock2, self.w_king, 0, 0
                            return player_side

        # Black
        if player_side == "black":
            if a.power in pieces_list_b and (b == 0 or b.side != "black"):
                if a.possible_moves(self, x0, y0, x1, y1) == True:
                    player_side = self.swapping(x0, y0, x1, y1, "white", "black", self.b_king, "\u265F")
                    
            elif a.power == "\u265A" and b.power == "\u265C":
                if self.board[0][1] == 0 and self.board[0][2] == 0 and self.board[0][3] == 0:
                    if self.b_king.first_move == None and self.b_rock1.first_move == None:
                        player_side = "white"
                        self.board[0][0], self.board[0][4] = 0, 0
                        x0, y0, x1, y1 = 2, 0, 1, 0
                        player_side = self.swapping_king_and_rook(x0, y0, x1, y1, "white", "black", self.b_king, self.b_rock1)
                        if player_side == "black":
                            self.board[0][0], self.board[0][4], self.board[y1][x1], self.board[y0][x0] = self.b_rock1, self.b_king, 0, 0
                elif self.board[0][5] == 0 and self.board[0][6] == 0:
                    if self.b_king.first_move == None and self.b_rock2.first_move == None:
                        player_side = "white"
                        self.board[0][7], self.board[0][4] = 0, 0
                        x0, y0, x1, y1 = 5, 0, 6, 0
                        player_side = self.swapping_king_and_rook(x0, y0, x1, y1, "white", "black", self.b_king, self.b_rock2)
                        if player_side == "black":
                            self.board[0][7], self.board[0][4], self.board[y1][x1], self.board[y0][x0] = self.b_rock2, self.b_king, 0, 0
        return player_side

    def print_board(self):
        for i in self.board:
            print(i)
    
    def set_up_board(self):
        # BLACK SIDE
        self.b_rock1 = p.Rock("black", pieces_dict_b["R"], 0, 0)
        self.b_knight1 = p.Knight("black", pieces_dict_b["KN"], 0, 1)
        self.b_bishop1 = p.Bishop("black", pieces_dict_b["B"], 0, 2)
        self.b_queen = p.Queen("black", pieces_dict_b["Q"], 0, 3)
        self.b_king = p.King("black", pieces_dict_b["K"], 0, 4)
        self.b_bishop2 = p.Bishop("black", pieces_dict_b["B"], 0, 5)
        self.b_knight2 = p.Knight("black", pieces_dict_b["KN"], 0, 6)
        self.b_rock2 = p.Rock("black", pieces_dict_b["R"], 0, 7)

        self.b_pawn1 = p.Pawn("black", pieces_dict_b["P"], 1, 0)
        self.b_pawn2 = p.Pawn("black", pieces_dict_b["P"], 1, 1)
        self.b_pawn3 = p.Pawn("black", pieces_dict_b["P"], 1, 2)
        self.b_pawn4 = p.Pawn("black", pieces_dict_b["P"], 1, 3)
        self.b_pawn5 = p.Pawn("black", pieces_dict_b["P"], 1, 4)
        self.b_pawn6 = p.Pawn("black", pieces_dict_b["P"], 1, 5)
        self.b_pawn7 = p.Pawn("black", pieces_dict_b["P"], 1, 6)
        self.b_pawn8 = p.Pawn("black", pieces_dict_b["P"], 1, 7)

        self.b_list = [self.b_rock1, self.b_knight1, self.b_bishop1, self.b_queen, self.b_king, self.b_bishop2, self.b_knight2,
                       self.b_pawn1, self.b_pawn2, self.b_pawn3, self.b_pawn4, self.b_pawn5, self.b_pawn6, self.b_pawn7, self.b_pawn8]
        
        self.board[0][0] = self.b_rock1
        self.board[0][1] = self.b_knight1
        self.board[0][2] = self.b_bishop1
        self.board[0][3] = self.b_queen
        self.board[0][4] = self.b_king
        self.board[0][5] = self.b_bishop2
        self.board[0][6] = self.b_knight2
        self.board[0][7] = self.b_rock2
        
        self.board[1][0] = self.b_pawn1
        self.board[1][1] = self.b_pawn2
        self.board[1][2] = self.b_pawn3
        self.board[1][3] = self.b_pawn4
        self.board[1][4] = self.b_pawn5
        self.board[1][5] = self.b_pawn6
        self.board[1][6] = self.b_pawn7
        self.board[1][7] = self.b_pawn8

        # WHITE SIDE
        self.w_rock1 = p.Rock("white", pieces_dict_w["r"], 7, 0)
        self.w_knight1 = p.Knight("white", pieces_dict_w["kn"], 7, 1)
        self.w_bishop1 = p.Bishop("white", pieces_dict_w["b"], 7, 2)
        self.w_queen = p.Queen("white", pieces_dict_w["q"], 7, 3)
        self.w_king = p.King("white", pieces_dict_w["k"], 7, 4)
        self.w_bishop2 = p.Bishop("white", pieces_dict_w["b"], 7, 5)
        self.w_knight2 = p.Knight("white", pieces_dict_w["kn"], 7, 6)
        self.w_rock2 = p.Rock("white", pieces_dict_w["r"], 7, 7)

        self.w_pawn1 = p.Pawn("white", pieces_dict_w["p"], 6, 0)
        self.w_pawn2 = p.Pawn("white", pieces_dict_w["p"], 6, 1)
        self.w_pawn3 = p.Pawn("white", pieces_dict_w["p"], 6, 2)
        self.w_pawn4 = p.Pawn("white", pieces_dict_w["p"], 6, 3)
        self.w_pawn5 = p.Pawn("white", pieces_dict_w["p"], 6, 4)
        self.w_pawn6 = p.Pawn("white", pieces_dict_w["p"], 6, 5)
        self.w_pawn7 = p.Pawn("white", pieces_dict_w["p"], 6, 6)
        self.w_pawn8 = p.Pawn("white", pieces_dict_w["p"], 6, 7)

        self.w_list = [self.w_rock1, self.w_knight1, self.w_bishop1, self.w_queen, self.w_king, self.w_bishop2, self.w_knight2,
                       self.w_pawn1, self.w_pawn2, self.w_pawn3, self.w_pawn4, self.w_pawn5, self.w_pawn6, self.w_pawn7, self.w_pawn8]
        
        self.board[-1][0] = self.w_rock1
        self.board[-1][1] = self.w_knight1
        self.board[-1][2] = self.w_bishop1
        self.board[-1][3] = self.w_queen
        self.board[-1][4] = self.w_king
        self.board[-1][5] = self.w_bishop2
        self.board[-1][6] = self.w_knight2
        self.board[-1][7] = self.w_rock2

        self.board[-2][0] = self.w_pawn1
        self.board[-2][1] = self.w_pawn2
        self.board[-2][2] = self.w_pawn3
        self.board[-2][3] = self.w_pawn4
        self.board[-2][4] = self.w_pawn5
        self.board[-2][5] = self.w_pawn6
        self.board[-2][6] = self.w_pawn7
        self.board[-2][7] = self.w_pawn8
