import time
import os


class InsertionSort():
    def __init__(self, vetor: list[int]) -> None:
        self.vetor = vetor

    def insertion_sort(self) -> list[int]:
        vetor = self.vetor
        tam_vetor = len(vetor)
        tempoinicial = time.time()
        for i in range(1, tam_vetor):
            chave = vetor[i]
            j = i - 1
            while j >= 0 and chave < vetor[j]:
                vetor[j + 1] = vetor[j]
                j -= 1
            vetor[j + 1] = chave
        return vetor, time.time() - tempoinicial
