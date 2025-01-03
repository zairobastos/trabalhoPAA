import os
import time

class MergeSort():
    def __init__(self, array: list[int]) -> None:
        self.array = array

    def merge_sort(self) -> list[int]:
        """Ordena uma lista de inteiros utilizando o algoritmo Merge Sort

        Returns:
            list[int]: Lista de inteiros ordenada
        """
        arr = self.array
        start = time.time()
        self.merge_sort_recursive(arr)
        return arr, time.time() - start

    def merge_sort_recursive(self, arr: list[int]) -> None:
        if len(arr) > 1:
            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]

            self.merge_sort_recursive(left)
            self.merge_sort_recursive(right)

            i = j = k = 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1