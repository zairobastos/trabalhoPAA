import random
import os


class BaseDados:
    def gerador_de_lista(self, n: int) -> list[int]:
        """Gera uma lista de 'n' números aleatórios

        Args:
            n (int): Tamanho da lista

        Returns:
            list[int]: Lista de 'n' números aleatórios
        """
        return random.sample(range(0, 100000000), n)


    def arquivo_de_lista(self,n: int) -> None:
        """Cria um arquivo com uma lista de 'n' números aleatórios

        Args:
            n (int): Tamanho da lista
        """
        if not os.path.exists('data'):
            os.makedirs('data')

        caminho_arquivo = f'data/{n}.txt'

        if not os.path.exists(caminho_arquivo):
            with open(caminho_arquivo, 'w') as f:
                lista = self.gerador_de_lista(n)
                f.write(str(lista))
            if os.path.exists(caminho_arquivo):
                print(f"Arquivo '{caminho_arquivo}' criado com sucesso!")
        else:
            print(f"O arquivo '{caminho_arquivo}' já existe!")
