from solutions.ProgramLinear.tsp_or import TSP_ProgramacaoLinear
from solutions.AlgoritmoGenetico.alg_gen import TSP_AlgoritmoGenetico
from instances.intance import Instance

def main():

    distancias = Instance().getAllDistances()

    solucao_programacao_linear = TSP_ProgramacaoLinear(distancias)
    solucao_algoritmo_genetico = TSP_AlgoritmoGenetico(distancias, 100, 10000, 0.2)
    

    print('=' * 100)
    print(' ' * 50 + 'Soluções' + (' ' * 30) )
    print('=' * 100)

    solucao_programacao_linear.start()
    solucao_algoritmo_genetico.start() 


main()