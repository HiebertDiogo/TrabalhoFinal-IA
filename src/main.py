from solutions.ProgramLinear.tsp_or import TSP_ProgramacaoLinear
from solutions.AlgoritmoGenetico.alg_gen import TSP_AlgoritmoGenetico

def main():

    solucao_programacao_linear = TSP_ProgramacaoLinear()
    solucao_algoritimo_genetico = TSP_AlgoritmoGenetico()

    print('========================================================')
    print('                      Soluções                          ')
    print('========================================================')

    solucao_programacao_linear.start()
    solucao_algoritimo_genetico.start()


main()