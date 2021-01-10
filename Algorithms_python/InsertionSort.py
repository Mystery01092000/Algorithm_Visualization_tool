class InsertionSort:

    def algorithm(self, array):
        for i in range(len(array)):
            cur = array[i]
            idx = i

            while idx > 0 and array[idx-1] > cur:
                array[idx] = array[idx-1]
                idx -= 1

            array[idx] = cur

        return array