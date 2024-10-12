from solutions.ProgramLinear.tsp_or import TSP_ProgramacaoLinear
from solutions.AlgoritmoGenetico.alg_gen import TSP_AlgoritmoGenetico
from instances.intance import Instance
import numpy as np

def main():

    # Exemplo de uso
    # distancias = np.array([
    #     [0, 2, 9, 10],
    #     [1, 0, 6, 4],
    #     [15, 7, 0, 8],
    #     [6, 3, 12, 0]
    # ])

    distancias = Instance().getAllDistances()

    solucao_programacao_linear = TSP_ProgramacaoLinear()
    tsp = TSP_AlgoritmoGenetico(distancias, 100, 10000, 0.2)
    

    print('========================================================')
    print('                      Soluções                          ')
    print('========================================================')

    solucao_programacao_linear.start()
    tsp.start()


main()