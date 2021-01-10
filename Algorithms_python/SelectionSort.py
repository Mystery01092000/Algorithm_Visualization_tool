class SelectionSort:

    def algorithm(self, array):
        for i in range(len(array)):
            idx = i
            for j in range(i+1, len(array)):
                if array[j] < array[idx]:
                    idx = j

            array[i], array[idx] = array[idx], array[i]

        return array