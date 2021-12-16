import pygame
import random

# SNAKE game by ludius0

# Constant values
h = 600 # height and width
c = 30 # constant

snake_c = (44, 62, 80) # Midnight blue color
apple_c = (255, 82, 82) # Fluorescent red color
back_c = (120, 224, 143) # Aurora green color
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Snake
class Snake():
    def __init__(self, snake_body, snake_c, direction):
        self.body = snake_body
        self.color = snake_c
        self.dir = direction


    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            keys = pygame.key.get_pressed()

            for key in keys:
                if keys[pygame.K_LEFT] and self.dir != "RIGHT" and not keys[pygame.K_UP] and not keys[pygame.K_DOWN]: # LEFT # make sure more keys can't be pressed
                    self.dir = "LEFT"
                elif keys[pygame.K_RIGHT] and self.dir != "LEFT" and not keys[pygame.K_UP] and not keys[pygame.K_DOWN]: # RIGHT
                    self.dir = "RIGHT"
                elif keys[pygame.K_UP] and self.dir != "DOWN" and not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]: # UP
                    self.dir = "UP"
                elif keys[pygame.K_DOWN] and self.dir != "UP" and not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]: # DOWN
                    self.dir = "DOWN"

        
        """
        Algorithm for moving snake:
        For every move, a square is added before the head in coresponding direction and the tail is deleted
        """
        a = self.body[-1]
        x, y = a[0], a[1]
        self.body.pop(0)
        if self.dir == "LEFT": self.body.append((x-c, y))
        elif self.dir == "RIGHT": self.body.append((x+c, y))
        elif self.dir == "UP": self.body.append((x, y-c))
        elif self.dir == "DOWN": self.body.append((x, y+c))

    def check_edges(self, i, x, y): # Checking edges
        if x == h: x = 0
        if x == 0-c: x = h
        if y == h: y = 0
        if y == 0-c: y = h
        self.body[i] = (x, y)

    def self_collision(self, i, j, x, y, screen):
        global status, end_status, score
        a = i + 1
        if (self.body[-1][0], self.body[-1][1]) == (x, y) and a != len(self.body) and (self.body[-2][0], self.body[-2][1]) != (x, y):  # If head isn't in place of part of body; if it is head; if it wasn't apple (after was added into the snake)
            score = len(self.body)
            end_status = "LOSE"
            status = False
        elif len(self.body) == h*h:
            end_status = "WIN"
            score = len(self.body)
            status = False

    def draw_and_check(self, screen):
        # Checking edges
        for i, j in enumerate(self.body):   # Drawing and checking for position of snake is in one pack of function, because of computation (for loop)
            x, y = j[0], j[1]
            self.self_collision(i, j, x, y, screen)
            self.check_edges(i, x, y)
            pygame.draw.rect(screen, self.color, (x, y, c+1, c+1))

def end_game(screen):
    global score, end_status
    screen.fill(BLACK)
    font = pygame.font.Font(None, 124)
    font2 = pygame.font.Font(None, 48)
    font3 = pygame.font.Font(None, 24)
    if end_status == "LOSE": text = font.render("GAME OVER", 1, WHITE)
    elif end_status == "WIN": text = font.render("YOU WIN!", 2, WHITE)
    text2 = font2.render(f"You ate {score-1} an apples.", 1, WHITE)
    text3 = font3.render("Press 'r' to play again", 1, WHITE)
    
    textpos, textpos2, textpos3 = text.get_rect(), text.get_rect(), text.get_rect()
    textpos.centerx = screen.get_rect().centerx
    
    x, y = h/1.5, h/2
    textpos2.center = (x, y-30)
    textpos3.center = (x+90, y+20)
    
    screen.blit(text, textpos), screen.blit(text2, textpos2), screen.blit(text3, textpos3)
            

def generate_apple(s):
    global apple_pos
    status = True
    while status:
        x, y = random.randrange(0, h, c), random.randrange(0, h, c)
        status = False
        for i in s.body:                    # won't generate on top of snake
            if x == i[0] and y == i[1]:
                status = True
        if status == False:
            apple_pos = (x, y)
            
def collision_with_apple(s):
    global apple_pos
    for i in s.body:
        if i == apple_pos:
            s.body.append((i[0], i[1]))
            apple_pos = None
            generate_apple(s)

def draw_grid(screen):
    x, y = 0, 0
    for _ in range(c):
        x, y = x+c, y+c
        pygame.draw.line(screen, BLACK, (x,0),(x,h))
        pygame.draw.line(screen, BLACK, (0,y),(h,y))


def main():
    global apple_pos, status
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((h, h))
    pygame.display.set_caption("SNAKE by ludius0")


    # Set a game
    status = True
    snake_body = [(c, c)]
    direction = "RIGHT"
    s = Snake(snake_body, snake_c, direction)
    apple_pos = ()
    generate_apple(s)

    clock = pygame.time.Clock()
    # Event loop
    while status:
        pygame.time.delay(40)
        clock.tick(20)

        # Snake
        collision_with_apple(s)
        s.move()
        
        # Draw on screen
        screen.fill(back_c)
        s.draw_and_check(screen)
        pygame.draw.rect(screen, apple_c, (apple_pos[0], apple_pos[1], c, c))       # Draw apple
        draw_grid(screen)                                                           # Draw grid

        if status == False:
            end_game(screen)
        pygame.display.update()

        
if __name__ == '__main__':
    main()
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            keys = pygame.key.get_pressed()

            for key in keys:
                if keys[pygame.K_r]:
                    main()
                    break
