import pygame

print("WELCOME TO SORTING VISUALIZER")

print("ALGORITHMS WE ARE DEALING WITH : ")
print('''
    1. Bubble sort
    2. Insertion sort
    3. Selection sort
    4. Merge sort
    5. Quick sort

''')

dimensions = [1024, 512]

pygame.init()
display = pygame.display.set_mode((dimensions[0], dimensions[1]))

display.fill(pygame.Color("#a48be0"))

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.display.flip()


def visualizer():
    print("Select an algorithm")


if __name__ == "__main__":
    visualizer()