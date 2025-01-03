import time
import os


class BubbleSort():
    def __init__(self, array: list[int]) -> None:
        self.array = array

    def bubble_sort(self) -> list[int]:
        """Ordena uma lista de inteiros utilizando o algoritmo Bubble Sort

        Returns:
            list[int]: Lista de inteiros ordenada
        """
        arr = self.array
        n = len(arr)
        start = time.time()
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr, time.time() - start
