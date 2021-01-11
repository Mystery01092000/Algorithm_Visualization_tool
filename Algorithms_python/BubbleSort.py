from Algorithms_python.Algorithms import Algorithms


class BubbleSort(Algorithms):

    def __init__(self):
        super().__init__("BubbleSort")


    def algorithm(self):
        for i in range(len(self.array)):
            for j in range(len(self.array)-1-i):
                if self.array[j] > self.array[j+1]:
                    self.array[j], self.array[j+1] = self.array[j+1], self.array[j]

            self.update_display(self.array[j], self.array[j+1])
