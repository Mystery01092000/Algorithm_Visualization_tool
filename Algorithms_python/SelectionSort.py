from Algorithms_python.Algorithms import Algorithms


class SelectionSort(Algorithms):

    def __init__(self):
        super().__init__("SelectionSort")

    def algorithm(self, array):
        for i in range(len(self.array)):
            idx = i
            for j in range(i+1, len(array)):
                if self.array[j] < self.array[idx]:
                    idx = j

            self.array[i], self.array[idx] = self.array[idx], self.array[i]
            self.update_display(self.array[i] , self.array[idx])
