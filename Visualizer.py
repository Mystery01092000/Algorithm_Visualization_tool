from visual_quicksort import quicksort

import pygame
import random

pygame.font.init()

# Total window
screen = pygame.display.set_mode(
    (900, 650)
)

# Title and Icon
pygame.display.set_caption("SORTING VISUALISER")
run = True

# Window size and some initials
width = 900
length = 600
array = [0] * 151
arr_clr = [(0, 204, 102)] * 151
clr_ind = 0
clr = [(0, 204, 102), (255, 0, 0), \
       (0, 0, 153), (255, 102, 0)]
fnt = pygame.font.SysFont("comicsans", 30)
fnt1 = pygame.font.SysFont("comicsans", 20)


def generate_arr():
    for i in range(1, 151):
        arr_clr[i] = clr[0]
        array[i] = random.randrange(1, 100)

    # Intially generate a array


generate_arr()



def draw():
    # Text should be rendered
    txt = fnt.render("SORT : PRESS 'ENTER'", \
                     1, (0, 0, 0))

    # Position where text is placed
    screen.blit(txt, (20, 20))
    txt1 = fnt.render("NEW ARRAY : PRESS 'R'", \
                      1, (0, 0, 0))
    screen.blit(txt1, (20, 40))
    txt2 = fnt1.render("ALGORITHM USED: QUICK SORT", \
                       1, (0, 0, 0))
    screen.blit(txt2, (600, 60))
    element_width = (width - 150) // 150
    boundry_arr = 900 / 150
    boundry_grp = 550 / 100
    pygame.draw.line(screen, (0, 0, 0), \
                     (0, 95), (900, 95), 6)

    # Drawing the array values as lines
    for i in range(1, 151):
        pygame.draw.line(screen, \
                         arr_clr[i], (boundry_arr * i - 3, 100), \
                         (boundry_arr * i - 3, \
                          array[i] * boundry_grp + 100), \
                         element_width)

    # Program should be run

if __name__ == "__main__":
    print("WELCOME TO SORTING VISUALIZER")

    print("ALGORITHMS WE ARE DEALING WITH : ")
    print('''
        1. Bubble sort
        2. Insertion sort
        3. Selection sort
        4. Merge sort
        5. Quick sort

    ''')
    while run:
        # background
        screen.fill((255, 255, 255))

        # Event handler stores all event
        for event in pygame.event.get():

            # If we click Close button in window
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    generate_arr()
                if event.key == pygame.K_RETURN:
                    quicksort(array, 1, len(array) - 1)
        draw()
        pygame.display.update()

    pygame.quit()
