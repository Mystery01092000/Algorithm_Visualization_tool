class MergeSort:

    def algorithm(self, array):
        if len(array) < 2:
            return array

        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        return merge(left, right)


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

        result += left[i:]
        result += right[j:]

        return result
