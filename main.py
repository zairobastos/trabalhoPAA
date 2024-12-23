from data import BaseDados
from bublesort import BubbleSort
from insertionsort import InsertionSort
from mergesort import MergeSort
from quicksort import QuickSort

import os
import time


def menu() -> None:
    while True:
        print(" Menu ".center(28, '='))
        print("1. Gerar arquivo de lista")
        print("2. Ordenar lista")
        print("3. Listar arquivos de lista")
        print("4. Sair")
        opcao = int(input('Escolha uma opção: '))
        if opcao == 4:
            os.system('clear')
            break
        if opcao == 1:
            n = int(input('Digite o tamanho da lista: '))
            BaseDados().arquivo_de_lista(n)
            time.sleep(3)
            os.system('clear')
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
            os.system('clear')
            print(f"Base de dados selecionada: {arquivos[opcao2 - 1]}")
            print("Escolha um algoritmo de ordenação:")
            print("1. BubbleSort")
            print("2. InsertionSort")
            print("3. MergeSort")
            print("4. QuickSort")

            opcao3 = int(input('Escolha uma opção: '))
            if opcao3 == 1:
                ordenado_buble, tempo_buble = BubbleSort(
                    lista).bubble_sort()
                print(f"Tempo de execução no BubbleSort: {
                      tempo_buble} segundos")
            if opcao3 == 2:
                ordenado_insertion, tempo_insertion = InsertionSort(
                    lista).insertion_sort()
                print(f"Tempo de execução no InsertionSort: {
                      tempo_insertion} segundos")
            if opcao3 == 3:
                ordenado_merge, tempo_merge = MergeSort(
                    lista).merge_sort()
                print(f"Tempo de execução no MergeSort: {
                      tempo_merge} segundos")
            if opcao3 == 4:
                ordenado_quick, tempo_quick = QuickSort(
                    lista).quick_sort()
                print(f"Tempo de execução no QuickSort: {
                      tempo_quick} segundos")


menu()
