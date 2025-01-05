import os
import time

class MergeSort():
    def __init__(self, vetor: list[int]) -> None:
        self.vetor = vetor

    def merge_sort(self) -> list[int]:
        vetor = self.vetor
        tempoinicial = time.time()
        self.merge_sort_recursivo(vetor)
        return vetor, time.time() - tempoinicial

    def merge_sort_recursivo(self, vetor: list[int]) -> None:
        if len(vetor) > 1:
            meio = len(vetor) // 2
            esq = vetor[:meio]
            dir = vetor[meio:]

            self.merge_sort_recursivo(esq)
            self.merge_sort_recursivo(dir)

            i = j = k = 0

            while i < len(esq) and j < len(dir):
                if esq[i] < dir[j]:
                    vetor[k] = esq[i]
                    i += 1
                else:
                    vetor[k] = dir[j]
                    j += 1
                k += 1

            while i < len(esq):
                vetor[k] = esq[i]
                i += 1
                k += 1

            while j < len(dir):
                vetor[k] = dir[j]
                j += 1
                k += 1