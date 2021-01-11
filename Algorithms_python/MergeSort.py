from Algorithms_python.Algorithms import Algorithms


class MergeSort(Algorithms):

    def __init__(self):
        super().__init__("MergeSort")

    def algorithm(self, array=[]):
        if array == []:
            array = self.array
        if len(array) < 2:
            return array
        mid = len(array) // 2
        left = self.algorithm(array[:mid])
        right = self.algorithm(array[mid:])
        return self.merge(left, right)

    def merge(self, left, right):
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
            self.update_display()
        result += left[i:]
        result += right[j:]
        self.array = result
        self.update_display()
        return result