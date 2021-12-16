from tkinter import *

class Piece():
    def __init__(self, color, representive, row, column, first_move=None):
        self.side = color
        self.power = representive
        self.row = row
        self.column = column
        self.first_move = first_move
        self.pawn_special_move = True


class King(Piece):
    def possible_moves(self, board, x0, y0, x1, y1):
        # Special move (change with rock)
        for i in range(-1, 2):
            for j in range(-1, 2):
                if y1+i<0 or y1+i>7 or x1+j<0 or x1+j>7: continue
                if (x1+j, y1+i) == (x0, y0):
                    self.first_move == True
                    return True
                    

    def check_for_checks(self, board, x, y):
        # Loop through possible_moves of all opposite side pieces; if at least one is True; It's check
        for iy, i in enumerate(board.board):
            for ix, j in enumerate(i):
                if j != 0 and j.side != self.side:               # If it is piece of opponent than check for possible moves and if one is correct (it's check)
                    if j.possible_moves(board, ix, iy, x, y) == True:
                        print(f"check: {self.side}")
                        return True
                        # Than check if king can move; if not; it's checkmate


class Queen(Piece):
    def possible_moves(self, board, x0, y0, x1, y1):
        # Horizontal and vertical
        def up():
            n = 1
            for _ in range(0, 8):
                if y1-n < 0: return False                                                           # Break if it is out of index return False
                if board.board[y1-n][x1] != 0 and (x1, y1-n) != (x0, y0):  return False             # If There is piece before target place (isn't empty or isn't position of targeting place) return False
                if (x1, y1-n) == (x0, y0): return True                                              # If position is same as targeting position return True
                n = n + 1
        def down():
            n = 1
            for _ in range(0, 8):
                if y1+n > 7: return False
                if board.board[y1+n][x1] != 0 and (x1, y1+n) != (x0, y0): return False
                if (x1, y1+n) == (x0, y0): return True
                n = n + 1
        def right():
            n = 1
            for _ in range(0, 8):
                if x1+n > 7: return False
                if board.board[y1][x1+n] != 0 and (x1+n, y1) != (x0, y0): return False
                if (x1+n, y1) == (x0, y0): return True
                n = n + 1
        def left():
            n = 1
            for _ in range(0, 8):
                if x1-n < 0: return False
                if board.board[y1][x1-n] != 0 and (x1-n, y1) != (x0, y0): return False
                if (x1-n, y1) == (x0, y0): return True
                n = n + 1
        # Diagonal
        def left_up():
            n = 1
            for _ in range(0, 8):
                if x1-n < 0 or y1-n < 0: return False                                                       
                if board.board[y1-n][x1-n] != 0 and (x1-n, y1-n) != (x0, y0):  return False         
                if (x1-n, y1-n) == (x0, y0): return True 
                n = n + 1
        def left_down():
            n = 1
            for _ in range(0, 8):
                if x1+n < 0 or y1+n > 7: return False
                if board.board[y1+n][x1-n] != 0 and (x1-n, y1+n) != (x0, y0): return False
                if (x1-n, y1+n) == (x0, y0): return True
                n = n + 1
        def right_up():
            n = 1
            for _ in range(0, 8):
                if y1-n < 0 or  x1+n > 7: return False
                if board.board[y1-n][x1+n] != 0 and (x1+n, y1-n) != (x0, y0): return False
                if (x1+n, y1-n) == (x0, y0): return True
                n = n + 1
        def right_down():
            n = 1
            for _ in range(0, 8):
                if x1+n > 7 or y1+n > 7: return False
                if board.board[y1+n][x1+n] != 0 and (x1+n, y1+n) != (x0, y0): return False
                if (x1+n, y1+n) == (x0, y0): return True
                n = n + 1

        response = []
        commands = [up(), down(), right(), left(),
                    left_up(), left_down(), right_up(), right_down()]
        for i in commands:
            response.append(i)
        if True in response:
            return True
        return False


class Rock(Piece):
    def possible_moves(self, board, x0, y0, x1, y1):
        def up():
            n = 1
            for _ in range(0, 8):
                if y1-n < 0: return False                                                           # Break if it is out of index return False
                if board.board[y1-n][x1] != 0 and (x1, y1-n) != (x0, y0):  return False             # If There is piece before target place (isn't empty or isn't position of targeting place) return False
                if (x1, y1-n) == (x0, y0):                                                          # If position is same as targeting position return True
                    self.first_move = True
                    return True 
                n = n + 1
        def down():
            n = 1
            for _ in range(0, 8):
                if y1+n > 7: return False
                if board.board[y1+n][x1] != 0 and (x1, y1+n) != (x0, y0): return False
                if (x1, y1+n) == (x0, y0): 
                    self.first_move = True
                    return True 
                n = n + 1
        def right():
            n = 1
            for _ in range(0, 8):
                if x1+n > 7: return False
                if board.board[y1][x1+n] != 0 and (x1+n, y1) != (x0, y0): return False
                if (x1+n, y1) == (x0, y0):
                    self.first_move = True
                    return True 
                n = n + 1
        def left():
            n = 1
            for _ in range(0, 8):
                if x1-n < 0: return False
                if board.board[y1][x1-n] != 0 and (x1-n, y1) != (x0, y0): return False
                if (x1-n, y1) == (x0, y0):
                    self.first_move = True
                    return True 
                n = n + 1

        response = []
        # Y-axix
        response.append(up())
        response.append(down())
        # X-axis
        response.append(right())
        response.append(left())

        if True in response:
            return True
        return False
                


class Bishop(Piece):
    def possible_moves(self, board, x0, y0, x, y):
        def left_up():
            n = 1
            for _ in range(0, 8):
                if x-n < 0 or y-n < 0: return False                                             # Break if it is out of index return False
                if board.board[y-n][x-n] != 0 and (x-n, y-n) != (x0, y0):  return False         # If There is piece before target place (isn't empty or isn't position of targeting place) return False
                if (x-n, y-n) == (x0, y0): return True                                          # If position is same as targeting position return True
                n = n + 1
        def left_down():
            n = 1
            for _ in range(0, 8):
                if x+n < 0 or y+n > 7: return False
                if board.board[y+n][x-n] != 0 and (x-n, y+n) != (x0, y0): return False
                if (x-n, y+n) == (x0, y0): return True
                n = n + 1
        def right_up():
            n = 1
            for _ in range(0, 8):
                if y-n < 0 or  x+n > 7: return False
                if board.board[y-n][x+n] != 0 and (x+n, y-n) != (x0, y0): return False
                if (x+n, y-n) == (x0, y0): return True
                n = n + 1
        def right_down():
            n = 1
            for _ in range(0, 8):
                if x+n > 7 or y+n > 7: return False
                if board.board[y+n][x+n] != 0 and (x+n, y+n) != (x0, y0): return False
                if (x+n, y+n) == (x0, y0): return True
                n = n + 1

        response = []
        response.append(left_up())
        response.append(left_down())
        response.append(right_up())
        response.append(right_down())
        if True in response:
            return True
        return False
        
            


class Knight(Piece):
    def possible_moves(self, board, x0, y0, x1, y1):
        #Left side
        if x1-1 == x0 and y1-2 == y0: return True
        elif x1-2 == x0 and y1-1 == y0: return True
        elif x1-1 == x0 and y1+2 == y0: return True
        elif x1-2 == x0 and y1+1 == y0: return True
        #Right Side
        elif x1+1 == x0 and y1-2 == y0: return True
        elif x1+2 == x0 and y1-1 == y0: return True
        elif x1+1 == x0 and y1+2 == y0: return True
        elif x1+2 == x0 and y1+1 == y0: return True
        return False


class Pawn(Piece):
    def possible_moves(self, board, x0, y0, x1, y1):
        # Check for special movement
        
        if self.first_move == None: self.first_move = False
        # White (UP)
        if self.side == "white":
            if y1-2 == y0 and x1 == x0 and board.board[y1-1][x1] == 0 and self.first_move == False:   # Two move up if it is first move and if it replacing rect for empty ("0")
                self.first_move = True
                return True
            elif y1-1 == y0 and x1 == x0 and board.board[y1-1][x1] == 0:              # One move up if replacing rect is empty ("0")
                self.first_move = True
                return True
            try: # Diagonal taking opponent piece
                if y1-1 == y0 and x1-1 == x0 and board.board[y0][x0].side == "black": # One move up and left if replacing rect is black piece
                    self.first_move = True
                    return True
                if y1-1 == y0 and x1+1 == x0 and board.board[y0][x0].side == "black": # One move up and left if replacing rect is black piece
                    self.first_move = True
                    return True
            except:
                pass
        
        # Black (DOWN)
        if self.side == "black":
            if y1+2 == y0 and x1 == x0 and board.board[y1+1][x1] == 0 and self.first_move == False:   
                self.first_move = True
                return True
            elif y1+1 == y0 and x1 == x0 and board.board[y1+1][x1] == 0:          
                self.first_move = True
                return True
            try:
                if y1+1 == y0 and x1+1 == x0 and board.board[y0][x0].side == "white":         
                    self.first_move = True
                    return True
                if y1+1 == y0 and x1-1 == x0 and board.board[y0][x0].side == "white":         
                    self.first_move = True
                    return True
            except:
                pass
        return False


    def ask_for_upgrade(self, board, a, x, y):
        
        def get_choice(board, x, y):        # After choosing, the piece will be upgraded
            representive = str(v.get())
            if representive == "\u2655" or representive == "\u265B": n = Queen(color, representive, y, x)
            elif representive == "\u2656" or representive == "\u265C": n = Rock(color, representive, y, x)
            elif representive == "\u2657" or representive == "\u265D": n = Bishop(color, representive, y, x)
            elif representive == "\u2658" or representive == "\u265E": n = Knight(color, representive, y, x)
            master.destroy()
            board.board[y][x] = n
            return

        # Set up choices based on side
        color = a.side
        if color == "white":
            MODES = [("Queen", "\u2655"),
                     ("Rock", "\u2656"),
                     ("Bishop", "\u2657"),
                     ("Knight", "\u2658")
                     ]
        elif color == "black":
            MODES = [("Queen", "\u265B"),
                     ("Rock", "\u265C"),
                     ("Bishop", "\u265D"),
                     ("Knight", "\u265E")
                     ]
        
        master = Tk()
        xn = 100
        yn = 100
        master.minsize(xn, yn)
        master.maxsize(xn, yn)
        
        v = StringVar()
        for text, mode in MODES:
            b = Radiobutton(master, text=text, variable=v, value=mode, indicatoron=0, command=lambda:get_choice(board, x, y))
            b.pack(ipadx=44)
        master.mainloop()
    
