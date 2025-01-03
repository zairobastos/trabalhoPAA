import os
import time
import sys


class QuickSort():
    def __init__(self, array: list[int]) -> None:
        self.array = array

    def quick_sort(self) -> list[int]:
        """Ordena uma lista de inteiros utilizando o algoritmo Quick Sort

        Returns:
            list[int]: Lista de inteiros ordenada
        """
        arr = self.array
        start = time.time()
        self.quick_sort_recursive(arr, 0, len(arr) - 1)
        return arr, time.time() - start

    def quick_sort_recursive(self, arr: list[int], low: int, high: int) -> None:
        sys.setrecursionlimit(10**9)
        if low < high:
            pi = self.partition(arr, low, high)

            self.quick_sort_recursive(arr, low, pi - 1)
            self.quick_sort_recursive(arr, pi + 1, high)

    def partition(self, arr: list[int], low: int, high: int) -> int:
        i = low - 1
        pivot = arr[high]

        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
