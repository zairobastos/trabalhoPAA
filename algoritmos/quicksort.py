import os
import time
import sys


class QuickSort():
    def __init__(self, vetor: list[int]) -> None:
        self.vetor = vetor

    def quick_sort(self) -> list[int]:
        vetor = self.vetor
        tempoinicial = time.time()
        self.quick_sort_recursivo(vetor, 0, len(vetor) - 1)
        return vetor, time.time() - tempoinicial

    def quick_sort_recursivo(self, vetor: list[int], piso: int, teto: int) -> None:
        sys.setrecursionlimit(10**9)
        if piso < teto:
            pi = self.particionar(vetor, piso, teto)

            self.quick_sort_recursivo(vetor, piso, pi - 1)
            self.quick_sort_recursivo(vetor, pi + 1, teto)

    def particionar(self, vetor: list[int], piso: int, teto: int) -> int:
        i = piso - 1
        pivot = vetor[teto]

        for j in range(piso, teto):
            if vetor[j] < pivot:
                i += 1
                vetor[i], vetor[j] = vetor[j], vetor[i]

        vetor[i + 1], vetor[teto] = vetor[teto], vetor[i + 1]
        return i + 1
