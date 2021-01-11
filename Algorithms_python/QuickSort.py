from Algorithms_python.Algorithms import Algorithms


class QuickSort(Algorithms):

    def __init__(self):
        super().__init__("QuickSort")

    def algorithm(self, array=[], start=0, end=0):
        if array == []:
            array = self.array
            end = len(array) - 1
        if start < end:
            pivot = self.partition(array,start,end)
            self.algorithm(array,start,pivot-1)
            self.algorithm(array,pivot+1,end)

    def partition(self, array, start, end):
        x = array[end]
        i = start-1
        for j in range(start, end+1, 1):
            if array[j] <= x:
                i += 1
                if i < j:
                    array[i], array[j] = array[j], array[i]
                    self.update_display(array[i], array[j])
        return i