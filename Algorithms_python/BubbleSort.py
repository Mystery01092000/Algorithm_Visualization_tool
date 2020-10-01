# BUBBLE SORT ------------------------------------------------------------------------------------
def bubble_sort(arr, n):
    for i in range(0,n-1):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# INSERTION SORT ----------------------------------------------------------------------------------
def insertion_sort(arr, n):
    for i in range(1, len(arr)):

        key = arr[i]

        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# SELECTION SORT ----------------------------------------------------------------------------------
def selection_sort(arr, n):
    for i in range(len(A)):

        min_idx = i

        for j in range(i + 1, len(A)):

            if A[min_idx] > A[j]:

                min_idx = j

        A[i], A[min_idx] = A[min_idx], A[i]
