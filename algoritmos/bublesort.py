import time
import os


class BubbleSort():
    def __init__(self, vetor: list[int]) -> None:
        self.vetor = vetor

    def bubble_sort(self) -> list[int]:
        vetor = self.vetor
        n = len(vetor)
        tempoinicial = time.time()
        for i in range(n):
            for j in range(0, n - i - 1):
                if vetor[j] > vetor[j + 1]:
                    vetor[j], vetor[j + 1] = vetor[j + 1], vetor[j]
        return vetor, time.time() - tempoinicial
