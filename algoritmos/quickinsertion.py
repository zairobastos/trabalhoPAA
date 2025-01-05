import time


class QuickInsertion:
    def __init__(self, vetor: list[int]) -> None:
        self.vetor = vetor

    def insertion_sort(self, vetor, esq, dir):
        for i in range(esq + 1, dir + 1):
            chave = vetor[i]
            j = i - 1
            while j >= esq and vetor[j] > chave:
                vetor[j + 1] = vetor[j]
                j -= 1
            vetor[j + 1] = chave

    def quickinsertion_sort(self, vetor, esq, dir, limite):
        if esq < dir:
            if (dir - esq + 1) > limite:
                pivo = self.particionar(vetor, esq, dir)
                self.quickinsertion_sort(vetor, esq, pivo - 1, limite)
                self.quickinsertion_sort(vetor, pivo + 1, dir, limite)
            else:
                self.insertion_sort(vetor, esq, dir)

    def particionar(self, vetor, esq, dir):
        pivo = vetor[dir]
        i = esq - 1
        for j in range(esq, dir):
            if vetor[j] <= pivo:
                i += 1
                vetor[i], vetor[j] = vetor[j], vetor[i]
        vetor[i + 1], vetor[dir] = vetor[dir], vetor[i + 1]
        return i + 1

    # Função principal para ordenar o array
    def algoritmo_sort(self, limite=10):
        vetor = self.vetor
        tempoinicial = time.time()
        self.quickinsertion_sort(vetor, 0, len(vetor) - 1, limite)
        return vetor, time.time() - tempoinicial
