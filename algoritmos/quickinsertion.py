import time


class QuickInsertion:
    def __init__(self, array: list[int]) -> None:
        self.array = array

    def insertion_sort(self, arr, left, right):
        for i in range(left + 1, right + 1):
            key = arr[i]
            j = i - 1
            while j >= left and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

    def hybrid_quick_sort(self, arr, left, right, threshold):
        if left < right:
            # Use Quick Sort for larger partitions
            if (right - left + 1) > threshold:
                pivot_index = self.partition(arr, left, right)
                self.hybrid_quick_sort(arr, left, pivot_index - 1, threshold)
                self.hybrid_quick_sort(arr, pivot_index + 1, right, threshold)
            else:
                # Use Insertion Sort for smaller partitions
                self.insertion_sort(arr, left, right)

    def partition(self, arr, left, right):
        pivot = arr[right]
        i = left - 1
        for j in range(left, right):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[right] = arr[right], arr[i + 1]
        return i + 1

    # Função principal para ordenar o array
    def hybrid_sort(self, threshold=10):
        arr = self.array
        inicio = time.time()
        self.hybrid_quick_sort(arr, 0, len(arr) - 1, threshold)
        return arr, time.time() - inicio
