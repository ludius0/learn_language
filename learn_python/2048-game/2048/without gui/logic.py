import random
status = True
game = True

"""
MOVES:
    LEFT:
        1. Compress
        2. Merge
        3. Compress

    RIGHT:
        1. Reverse
        2. Compress
        3. Merge
        4. Compress
        5. Reverse

    UP:
        1. Transpose
        2. Compress
        3. Merge
        4. Compress
        5. Transpose
        
    DOWN:
        1. Transpose
        2. Reverse
        3. Compress
        4. Merge
        5. Compress
        6. Reverse
        7. Transpose
"""

### LOGIC
def compress(b):  # Compress all numbers to left  ### before and after merge function (before: so it can merge next to it; after: so it won't leave blank spots)
    global status
    a = [[0 for i in range(4)] for i in range(4)]     
    for i in range(4):
        pos = 0                             # "pos" get reset to zero after every cycle of "i"
        for j in range(4):                  # if number isn't 0, it will rewrite number depending on "pos"; every time "j" isn't number 0 -> "pos" move to next in those 4 available places in row
            if b[i][j] != 0:
                a[i][pos] = b[i][j]
                if j != pos:
                    status = True
                pos += 1
    return a

def merge(b):     # Merge number if it same (from right to left) ### This function must be called after compress function
    global status
    for i in range(4):
        for j in range(3):
            if b[i][j] == b[i][j+1] and b[i][j] != 0:
                b[i][j] += b[i][j]
                b[i][j+1] = 0
                status = True
    return b

def reverse(b):   # Return reverse matrix
    for i in range(4):
        b[i].reverse()
    return b

def transp(b):    # Swap rows and columns
    a = [[0 for i in range(4)] for i in range(4)]
    for i in range(4):
        for j in range(4):
            a[i][j] = b[j][i]
    return a


### PRINT
def p_board(b):
    global status
    score = sum(b[0]) + sum(b[1]) + sum(b[2]) + sum(b[3])
    if game == True:
        if status == True:
            for i in range(4):
                print(b[i])
            print(f"Score: {score}")
            print("-"*20)
    else:
        print("You lost!")


### GENERATE NUMBER
def generate_number(b):
    global status, game
    if status:                                                                      # Make sure it should generate
        if min(b[0]) == 0 or min(b[1]) == 0 or min(b[2]) == 0 or min(b[3]) == 0:    # Make sure there is somewhere 0
            while True:                                                             # Looping until find thata position to write number 2
                x, y = random.randint(0, 3), random.randint(0, 3)
                j = random.randint(1, 10)                                            # Add 10% chance for 4
                if b[x][y] == 0:
                    if j == 10:
                        b[x][y] = 4
                    else:
                        b[x][y] = 2
                    break
        else:
            game = False                                                            # End game loop
    status = False
    return b
