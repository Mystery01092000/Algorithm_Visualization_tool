from Algorithms_python.Algorithms import Algorithms


class InsertionSort(Algorithms):

    def __init__(self):
        super().__init__("InsertionSort")

    def algorithm(self):
        for i in range(len(self.array)):
            cur = self.array[i]
            idx = i

            while idx > 0 and self.array[idx-1] > cur:
                self.array[idx] = self.array[idx-1]
                idx -= 1

            self.array[idx] = cur
            self.update_display(self.array[idx], self.array[i])
