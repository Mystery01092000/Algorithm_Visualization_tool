import random
import time

print("WELCOME TO SORTING VISUALIZER")

print("ALGORITHMS WE ARE DEALING WITH : ")
print('''
    1. Bubble sort
    2. Insertion sort
    3. Selection sort
    4. Merge sort
    5. Quick sort

''')


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