import random
import time

from matplotlib import animation

import Algorithms_python
import matplotlib.pyplot as plt
from Algorithms_python.BubbleSort import bubble_sort

print("WELCOME TO SORTING VISUALIZER")

print("ALGORITHMS WE ARE DEALING WITH : ")
print('''
    1. Bubble sort
    2. Insertion sort
    3. Selection sort
    4. Merge sort
    5. Quick sort

''')

def swap(A, i, j):

    if i != j:
        A[i], A[j] = A[j], A[i]

def bubblesort(A):

    if len(A) == 1:
        return

    swapped = True
    for i in range(len(A) - 1):
        if not swapped:
            break
        swapped = False
        for j in range(len(A) - 1 - i):
            if A[j] > A[j + 1]:
                swap(A, j, j + 1)
                swapped = True
            yield A



if __name__ == "__main__":

    # Take number of integers element
    n = int(input("Enter the number of elements: "))
    #print(n)
    #Create an list of integer elements from 1 to n
    arr = [i+1 for i in range(n)]
    #print(arr)
    #Generate a random number k
    random.seed(time.time())

    #list is then shuffled k times
    k = random.randint(0,5) + 1
    #print(k)
    for i in range(k):
        random.shuffle(arr)
        #print(arr)
    #print(arr)

    start = time.process_time()
    generator = bubblesort(arr)
    print(time.process_time() - start )


    fig, ax = plt.subplots()
    ax.set_title("BubbleSort")

    bar_rects = ax.bar(range(len(arr)), arr, align="edge")


    ax.set_xlim(0,n)
    ax.set_ylim(0, int(1.07 * n))

    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

    iteration = [0]


    def update_fig(A, rects, iteration):
        for rect, val in zip(rects, A):
            rect.set_height(val)
        iteration[0] += 1
        text.set_text("# of operations: {}".format(iteration[0]))


    anim = animation.FuncAnimation(fig, func=update_fig,
                                   fargs=(bar_rects, iteration), frames=generator, interval=1,
                                   repeat=False)
    plt.show()