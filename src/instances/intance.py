import numpy as np
import os

class Instance():


    # Retona a matriz com tamanho n = qtd
    def getDistancesSize(self, qtd: int):
        
        
        matriz = self.getAllDistances()
        max = min(qtd, len(matriz))

        #to do

        return matriz
    
    # Função para ler o arquivo e criar a matriz
    def getAllDistances(self):

        file = self.getPath('./data/distances.txt')
       
        with open(file, 'r') as file:
            matriz = [list(map(float, line.split())) for line in file]
            return np.array(matriz)

    def gerar_matrizes_tsp_teste(self, num_cidades, num_matrizes):
        matrizes = []
        for _ in range(num_matrizes):
            matriz = np.random.randint(1, 100, size=(num_cidades, num_cidades))
            np.fill_diagonal(matriz, 0)  # Distância zero para a mesma cidade
            matrizes.append(matriz)
        return matrizes
        

    def getPath(self, path: str):

        current_dir = os.path.dirname(os.path.abspath(__file__))

        return os.path.abspath(os.path.join(current_dir, path))