import pygame
import time

import sorting_algorithms as sa
import values as v

pygame.init()
screen = pygame.display.set_mode((v.width, v.height))
pygame.display.set_caption("Sorting visualiser by ludius0")

def check(still_continue=None):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if still_continue == True:
            keys = pygame.key.get_pressed()
            for key in keys:
                if keys[pygame.K_SPACE]:
                    main()
                    break
        elif still_continue == False:
            keys = pygame.key.get_pressed()
            for key in keys:
                if keys[pygame.K_SPACE]:
                    sa.status_continue = False
                    break
        
def update_screen(alg, a, b):
    SORTING = True
    pygame.display.set_caption(f"Sorting visualiser by ludius0     Algorithm: {alg.name}     Time: {time.time() - alg.start_time} seconds")
    screen.fill(v.WHITE)
    color = v.BLACK
    j = int(v.width/len(alg.array))
    for i in range(len(alg.array)):
        if a == alg.array[i]: color = v.GREEN
        elif b == alg.array[i]: color = v.RED
        else: color = v.BLACK
        pygame.draw.rect(screen, color, (i*j, v.height-j, j, alg.array[i]*-1))
    check(False)             # Without it; program could crash
    pygame.display.update()

def show_info():
    pygame.font.init()
    myfont_ = pygame.font.SysFont("Times New Roman", 30)
    textsurface_ = myfont_.render("Press 'space' to go to menu", False, v.BLACK)
    screen.blit(textsurface_,(10, 10))

class Panel():
    def __init__(self, x, y, x0, y0, name):
        self.x = x
        self.y = y
        self.x0 = x0
        self.y0 = y0
        self.name = name
        self.create_panel()

    def create_panel(self):
        # Draw Panel
        pygame.draw.rect(screen, v.WHITE, (self.x,self.y, self.x0, self.y0))

        #Draw Text
        pygame.font.init()
        myfont = pygame.font.SysFont("Times New Roman", 30)
        textsurface = myfont.render(f"{self.name}", False, v.BLACK)
        screen.blit(textsurface,(int(self.x+self.x0/4),int(self.y+self.y0/4)))

def main():
    global SORTING
    screen.fill(v.BLACK)
    SORTING = False

    # Create panels and call sorting functions
    # Right Side
    bubble_sort = Panel(int(v.width-450), 90, 300, 70,"BubbleSort")
    quick_sort = Panel(int(v.width-450),190,300,70,"QuickSort")
    insertion_sort = Panel(int(v.width-450),290,300,70,"InsertionSort")
    bogo_sort = Panel(int(v.width-450),390,300,70,"BogoSort")
    # Left side
    cocktail_sort = Panel(int(v.width/6-100), 90, 300, 70, "CocktailSort")
    shell_sort = Panel(int(v.width/6-100), 190, 300, 70, "ShellSort")
    gnome_sort = Panel(int(v.width/6-100), 290, 300, 70, "GnomeSort")
    radix_sort = Panel(int(v.width/6-100), 390, 300, 70, "RadixSort")

    alg = {"BubbleSort": sa.BubbleSort(),
           "QuickSort": sa.QuickSort(),
           "InsertionSort": sa.InsertionSort(),
           "BogoSort": sa.BogoSort(),
           "CocktailSort": sa.CocktailSort(),
           "ShellSort": sa.ShellSort(),
           "GnomeSort": sa.GnomeSort(),
           "RadixSort": sa.RadixSort()}

    # Choosing sorting function
    flag = True
    while flag:
        sa.status_continue = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and SORTING == False:
                # PANELS FUNCTIONS
                if pygame.mouse.get_pos()[0] >= bubble_sort.x and pygame.mouse.get_pos()[0] <= bubble_sort.x + bubble_sort.x0: 
                    if pygame.mouse.get_pos()[1] >= bubble_sort.y and pygame.mouse.get_pos()[1] <= bubble_sort.y + bubble_sort.y0:
                        alg["BubbleSort"].play()
                        flag = False
                if pygame.mouse.get_pos()[0] >= quick_sort.x and pygame.mouse.get_pos()[0] <= quick_sort.x + quick_sort.x0: 
                    if pygame.mouse.get_pos()[1] >= quick_sort.y and pygame.mouse.get_pos()[1] <= quick_sort.y + quick_sort.y0:
                        alg["QuickSort"].play()
                        flag = False
                if pygame.mouse.get_pos()[0] >= insertion_sort.x and pygame.mouse.get_pos()[0] <= insertion_sort.x + insertion_sort.x0: 
                    if pygame.mouse.get_pos()[1] >= insertion_sort.y and pygame.mouse.get_pos()[1] <= insertion_sort.y + insertion_sort.y0:
                        alg["InsertionSort"].play()
                        flag = False
                if pygame.mouse.get_pos()[0] >= bogo_sort.x and pygame.mouse.get_pos()[0] <= bogo_sort.x + bogo_sort.x0: 
                    if pygame.mouse.get_pos()[1] >= bogo_sort.y and pygame.mouse.get_pos()[1] <= bogo_sort.y + bogo_sort.y0:
                        alg["BogoSort"].play()
                        flag = False
                if pygame.mouse.get_pos()[0] >= cocktail_sort.x and pygame.mouse.get_pos()[0] <= cocktail_sort.x + cocktail_sort.x0: 
                    if pygame.mouse.get_pos()[1] >= cocktail_sort.y and pygame.mouse.get_pos()[1] <= cocktail_sort.y + cocktail_sort.y0:
                        alg["CocktailSort"].play()
                        flag = False
                if pygame.mouse.get_pos()[0] >= shell_sort.x and pygame.mouse.get_pos()[0] <= shell_sort.x + shell_sort.x0: 
                    if pygame.mouse.get_pos()[1] >= shell_sort.y and pygame.mouse.get_pos()[1] <= shell_sort.y + shell_sort.y0:
                        alg["ShellSort"].play()
                        flag = False
                if pygame.mouse.get_pos()[0] >= gnome_sort.x and pygame.mouse.get_pos()[0] <= gnome_sort.x + gnome_sort.x0: 
                    if pygame.mouse.get_pos()[1] >= gnome_sort.y and pygame.mouse.get_pos()[1] <= gnome_sort.y + gnome_sort.y0:
                        alg["GnomeSort"].play()
                        flag = False
                if pygame.mouse.get_pos()[0] >= radix_sort.x and pygame.mouse.get_pos()[0] <= radix_sort.x + radix_sort.x0: 
                    if pygame.mouse.get_pos()[1] >= radix_sort.y and pygame.mouse.get_pos()[1] <= radix_sort.y + radix_sort.y0:
                        alg["RadixSort"].play()
                        flag = False

        pygame.display.update()

if __name__ == "__main__":
    main()
    # If user still want use program, than press "space"
    while 1:
        check(True)
