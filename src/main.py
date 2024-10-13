from solutions.ProgramLinear.tsp_or import TSP_ProgramacaoLinear
from solutions.AlgoritmoGenetico.alg_gen import TSP_AlgoritmoGenetico
from solutions.SimulatedAnnealing.Simu_anneal import TSP_SimulatedAnnealing
from solutions.AlgoritmoBusca.alg_busca import TSP_AStar
from instances.intance import Instance
import time

def main():

    # Intancia
    distancias = Instance().getAllDistances()
    
    print('=' * 100)
    print(' ' * 50 + 'Soluções' + (' ' * 30) )
    print('=' * 100)

    # Programacao Linear

    solucao_programacao_linear = TSP_ProgramacaoLinear(distancias)

    start_time = time.time()
    solucao_programacao_linear.start()
    end_time = time.time()
    print(f"Tempo de execucao: {end_time - start_time} seconds")

    #Algoritimo Genetico

    solucao_algoritmo_genetico = TSP_AlgoritmoGenetico(distancias, 200, 10000, 0.4)

    start_time = time.time()
    solucao_algoritmo_genetico.start() 
    end_time = time.time()
    print(f"Tempo de execucao: {end_time - start_time} seconds")

    # Simulated Annealing

    sa = TSP_SimulatedAnnealing(distancias)

    start_time = time.time()
    sa.start()
    end_time = time.time()
    print(f"Tempo de execucao: {end_time - start_time} seconds")


    # Algoritimo de busca A*

    tsp_astar = TSP_AStar(distancias)

    start_time = time.time()
    tsp_astar.start()
    end_time = time.time()
    print(f"Tempo de execucao: {end_time - start_time} seconds")


main()