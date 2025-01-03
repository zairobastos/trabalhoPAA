from data import BaseDados
from algoritmos.bublesort import BubbleSort
from algoritmos.insertionsort import InsertionSort
from algoritmos.mergesort import MergeSort
from algoritmos.quicksort import QuickSort
from algoritmos.quickinsertion import QuickInsertion

import os
import time


def menu() -> None:
    while True:
        print(" Menu ".center(28, '='))
        print("1. Gerar arquivo de lista")
        print("2. Ordenar lista")
        print("3. Sair")
        opcao = int(input('Escolha uma opção: '))
        if opcao == 3:
            os.system('clear')
            break
        if opcao == 1:
            n = int(input('Digite o tamanho da lista: '))
            BaseDados().arquivo_de_lista(n)
            time.sleep(3)
        if opcao == 2:
            print("Escolha um arquivo de lista:")
            arquivos = os.listdir('data')
            for i, arquivo in enumerate(arquivos):
                print(f'{i + 1}. {arquivo}')
            opcao2 = int(input('Escolha uma opção: '))
            caminho_arquivo = f'data/{arquivos[opcao2 - 1]}'

            with open(caminho_arquivo, 'r') as f:
                lista = eval(f.read())

            time.sleep(1)
            print(f"Base de dados selecionada: {arquivos[opcao2 - 1]}")
            print("Escolha um algoritmo de ordenação:")
            print("1. BubbleSort")
            print("2. InsertionSort")
            print("3. MergeSort")
            print("4. QuickSort")
            print("5. QuickInsertionSort")

            opcao3 = int(input('Escolha uma opção: '))
            if opcao3 == 1:
                ordenado_buble, tempo_buble = BubbleSort(
                    lista).bubble_sort()
                print(f"Tempo de execução no BubbleSort: {
                      tempo_buble} segundos")
            elif opcao3 == 2:
                ordenado_insertion, tempo_insertion = InsertionSort(
                    lista).insertion_sort()
                print(f"Tempo de execução no InsertionSort: {
                      tempo_insertion} segundos")
            elif opcao3 == 3:
                ordenado_merge, tempo_merge = MergeSort(
                    lista).merge_sort()
                print(f"Tempo de execução no MergeSort: {
                      tempo_merge} segundos")
            elif opcao3 == 4:
                ordenado_quick, tempo_quick = QuickSort(
                    lista).quick_sort()
                print(f"Tempo de execução no QuickSort: {
                      tempo_quick} segundos")
            elif opcao3 == 5:
                ordenado_quick_insertion, tempo_quick_insertion = QuickInsertion(
                    lista).hybrid_sort()
                print(f"Tempo de execução no QuickInsertion: {
                      tempo_quick_insertion} segundos")
            else:
                print("Opção inválida")
            time.sleep(3)


menu()
