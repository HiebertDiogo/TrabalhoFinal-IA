from solutions.ProgramLinear.tsp_or import TSP_ProgramacaoLinear
from solutions.AlgoritmoGenetico.alg_gen import TSP_AlgoritmoGenetico
from solutions.SimulatedAnnealing.Simu_anneal import TSP_SimulatedAnnealing
from instances.intance import Instance
import time

def main():

    # intancia

    distancias = Instance().getAllDistances()
    
    print('=' * 100)
    print(' ' * 50 + 'Soluções' + (' ' * 30) )
    print('=' * 100)

    #programacao linear

    solucao_programacao_linear = TSP_ProgramacaoLinear(distancias)

    start_time = time.time()
    solucao_programacao_linear.start()
    end_time = time.time()
    print(f"Tempo de execucao: {end_time - start_time} seconds")

    #Algoritimo genetico

    solucao_algoritmo_genetico = TSP_AlgoritmoGenetico(distancias, 200, 10000, 0.4)

    start_time = time.time()
    solucao_algoritmo_genetico.start() 
    end_time = time.time()
    print(f"Tempo de execucao: {end_time - start_time} seconds")

    #Simulated Annealing

    initial_path = [i for i in range(len(distancias))]
  
    sa = TSP_SimulatedAnnealing(distancias)

    start_time = time.time()
    sa.start(initial_path)
    end_time = time.time()
    print(f"Tempo de execucao: {end_time - start_time} seconds")



main()