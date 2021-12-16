import logic as l


### GENERATE BOARD AND FIRST NUMBER ###
print("Welcome in game 2048!\nPlayable moves:\n'a' -> LEFT\n'd' -> RIGHT\n'w' -> UP\n's' -> DOWN\n" + "-"*20)
board = [[0 for i in range(4)] for i in range(4)]
board = l.generate_number(board)
l.p_board(board)


### GAME LOOP
while l.game:
    user_input = input()
    if user_input == "a":      # LEFT
        board = l.compress(board)
        board = l.merge(board)
        board = l.compress(board)
        board = l.generate_number(board)
        l.p_board(board)
    elif user_input == "d":    # RIGHT
        board = l.reverse(board)
        board = l.compress(board)
        board = l.merge(board)
        board = l.compress(board)
        board = l.reverse(board)
        board = l.generate_number(board)
        l.p_board(board)
    elif user_input == "w":    # UP
        board = l.transp(board)
        board = l.compress(board)
        board = l.merge(board)
        board = l.compress(board)
        board = l.transp(board)
        board = l.generate_number(board)
        l.p_board(board)
    elif user_input == "s":    # DOWN
        board = l.transp(board)
        board = l.reverse(board)
        board = l.compress(board)
        board = l.merge(board)
        board = l.compress(board)
        board = l.reverse(board)
        board = l.transp(board)
        board = l.generate_number(board)
        l.p_board(board)
    elif user_input == "help":
        print("Welcome in game 2048!\nPlayable moves:\n'a' -> LEFT\n'd' -> RIGHT\n'w' -> UP\n's' -> DOWN")
    else:
        print("Error in input...\nTry again.")
