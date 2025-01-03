import time
import os


class InsertionSort():
    def __init__(self, array: list[int]) -> None:
        self.array = array

    def insertion_sort(self) -> list[int]:
        """Ordena uma lista de inteiros utilizando o algoritmo Insertion Sort

        Returns:
            list[int]: Lista de inteiros ordenada
        """
        arr = self.array
        n = len(arr)
        start = time.time()
        for i in range(1, n):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr, time.time() - start
