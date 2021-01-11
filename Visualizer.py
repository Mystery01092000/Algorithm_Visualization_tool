import sys
from datetime import time
import pygame

from Algorithms_python import Algorithms
from Algorithms_python.BubbleSort import BubbleSort
from Algorithms_python.InsertionSort import InsertionSort
from Algorithms_python.MergeSort import MergeSort
from Algorithms_python.QuickSort import QuickSort
from Algorithms_python.SelectionSort import SelectionSort

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

algorithms = {"SelectionSort": SelectionSort(), "BubbleSort": BubbleSort(), "InsertionSort": InsertionSort(), "MergeSort": MergeSort(), "QuickSort": QuickSort()}


if len(sys.argv) > 1:
    if sys.argv[1] == "list":
        for key in algorithms.keys(): print(key, end=" ")
        print("")
        sys.exit(0)

pygame.init()
display = pygame.display.set_mode((dimensions[0], dimensions[1]))

display.fill(pygame.Color("#a48be0"))



def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit();
            sys.exit();

def update(algorithm, swap1=None, swap2=None, display=display):
    display.fill(pygame.Color("#a48be0"))
    pygame.display.set_caption("Sorting Visualizer     Algorithm: {}     Time: {:.3f}      Status: Sorting...".format(algorithm.name, time.time() - algorithm.start_time)) # Display on title bar
    k = int(dimensions[0]/len(algorithm.array))
    for i in range(len(algorithm.array)):
        colour = (80, 0, 255)
        if swap1 == algorithm.array[i]:
            colour = (0,255,0)
        elif swap2 == algorithm.array[i]:
            colour = (255,0,0)
        pygame.draw.rect(display, colour, (i*k,dimensions[1],k,-algorithm.array[i]))
    check_events()
    pygame.display.update()

def keep_open(algorithm, display, time):
    pygame.display.set_caption("Sorting Visualizer     Algorithm: {}     Time: {:.3f}      Status: Done!".format(algorithm.name, time))
    while True:
        check_events()
        pygame.display.update()

def visualizer():
    if len(sys.argv) < 2:
        print("Please select a sorting algorithm.")
    else:
        try:
            algorithm = algorithms[sys.argv[1]]  # Pass the algorithm selected
            try:
                time_elapsed = algorithm.run()[1]
                keep_open(algorithm, display, time_elapsed)
                pass
            except:
                pass
        except:
            print("Error.")

if __name__ == "__main__":
    visualizer()