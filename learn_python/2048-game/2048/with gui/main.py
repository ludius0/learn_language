import tkinter as tk
from tkinter import Frame
from tkinter import ttk
import logic as l
import values as v

class Board(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        parent = tk.Frame(self)

        self.size = self.get_size()
        self.board = l.generate_board()
        self.end_status = False

        self.createWidgets()

        self.bind("<Key>", self.key_down)

        
    def createWidgets(self):
        for i in range(4):
            for j in range(4):
                if self.board[i][j] != 0:
                    self.n = tk.Label(self, text=self.board[i][j], font=v.FONT, fg="white", bg=v.CELL_COLOR_DICT[self.board[i][j]])
                    self.n.grid(row=i, column=j, padx=2, pady=2, sticky="nsew")
                else:
                    self.n = tk.Label(self, text=" ", font=v.FONT, fg="white", bg=v.EMPTY_CELL, width=5, height=3)
                    self.n.grid(row=i, column=j, padx=2, pady=2, sticky="nsew")

        self.score = sum(self.board[0]) + sum(self.board[1]) + sum(self.board[2]) + sum(self.board[3])
        self.m = tk.Label(self, text=f"Score:\n{self.score}", font=v.FONT, fg="black").grid(row=0, column=4, rowspan=5, sticky="e")

                   
    def get_size(self):
        x = int(v.SIZE / 9)
        y = x
        return (x, y) 

    def key_down(self, event): # add check for ending game
        key = repr(event.char)
        if key == v.KEY_LEFT:
            self._left()
            self.createWidgets()
        elif key == v.KEY_RIGHT:
            self._right()
            self.createWidgets()
        elif key == v.KEY_UP:
            self._up()
            self.createWidgets()
        elif key == v.KEY_DOWN:
            self._down()
            self.createWidgets()
        elif key == v.KEY_RESTART:
            self.board = l.generate_board()
            l.status = True
            self.n.grid_remove()
            self.createWidgets()
            self.end_status = False
        elif key == v.KEY_ESCAPE:
            game.destroy()

    def _left(self):
        self.board = l.compress(self.board)
        self.board = l.merge(self.board)
        self.board = l.compress(self.board)
        self.board = l.generate_number(self.board)

    def _right(self):
        self.board = l.reverse(self.board)
        self.board = l.compress(self.board)
        self.board = l.merge(self.board)
        self.board = l.compress(self.board)
        self.board = l.reverse(self.board)
        self.board = l.generate_number(self.board)

    def _up(self):
        self.board = l.transp(self.board)
        self.board = l.compress(self.board)
        self.board = l.merge(self.board)
        self.board = l.compress(self.board)
        self.board = l.transp(self.board)
        self.board = l.generate_number(self.board)

    def _down(self):
        self.board = l.transp(self.board)
        self.board = l.reverse(self.board)
        self.board = l.compress(self.board)
        self.board = l.merge(self.board)
        self.board = l.compress(self.board)
        self.board = l.reverse(self.board)
        self.board = l.transp(self.board)
        self.board = l.generate_number(self.board)
        


class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        tk.Tk.wm_title(self, "2048 by ludius0")
        tk.Tk.geometry(self, "980x820")
        tk.Tk.configure(self, background=v.BACKGROUND)
        
        root = tk.Frame(self)
        root.pack(expand=True)
        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)

        self.frames = {}
        frame = Board(root, self)
        self.frames[Board] = frame
        frame.pack()
        self.show_frame(Board)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.focus_set()
        frame.tkraise


if __name__ == "__main__":
    game = App()
    game.mainloop()
