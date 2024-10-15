from solutions.ProgramLinear.tsp_or import TSP_ProgramacaoLinear
from solutions.AlgoritmoGenetico.alg_gen import TSP_AlgoritmoGenetico
from solutions.SimulatedAnnealing.Simu_anneal import TSP_SimulatedAnnealing
from solutions.AlgoritmoBusca.alg_busca import TSP_AStar
from solutions.RL.tsp_rl import TSP_RL
from solutions.BuscaLocal.buscalLocal import TSP_LocalSearch
import subprocess

from instances.intance import Instance

import time

def run_cpp_program():
    result = subprocess.run(['TrabalhoFinal-IA/src/solutions/BuscaLocal/main.exe'], 
                            stdout=subprocess.PIPE, 
                            stderr=subprocess.PIPE, 
                            text=True)
    
    if result.returncode == 0:
        print(result.stdout)  # Saída do programa C++
    else:
        print(result.stderr)


def main():

    # Intancia

    inst = Instance()

    #distancias = inst.getAllDistances()
    distancias =  inst.gerar_matrizes_tsp_teste(11, 1)[0]

   
    print('=' * 100)
    print(' ' * 50 + 'Soluções' + (' ' * 30) )
    print('=' * 100)

    # Programacao Linear

    solucao_programacao_linear = TSP_ProgramacaoLinear(distancias)

    start_time = time.time()
    solucao_programacao_linear.start()
    end_time = time.time()
    print(f"Tempo de execucao: {end_time - start_time} seconds")

    # Simulated Annealing

    sa = TSP_SimulatedAnnealing(distancias, 1000, 100000)

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

    #Busca Local

    solucao_busca_local = TSP_LocalSearch(distancias)
    
    start_time = time.time()
    solucao_busca_local.start()
    end_time = time.time()
    print(f"Tempo de execucao: {end_time - start_time} seconds")

    # Aprendizado com reforço

    distancias_treinamento = inst.gerar_matrizes_tsp_teste(11, 30)

    handle_rl = TSP_RL()

    start_time = time.time()
    agent = handle_rl.treinar(distancias_treinamento)
    end_time = time.time()
    treino_time = end_time - start_time
    

    start_time = time.time()
    handle_rl.start(agent, distancias)
    end_time = time.time()
    print(f"Tempo de execucao com modelo: {end_time - start_time} seconds")
    print(f"Tempo de execucao do treinamento: {treino_time} seconds")

    #Algoritimo Genetico

    solucao_algoritmo_genetico = TSP_AlgoritmoGenetico(distancias, 200, 10000, 0.4)

    start_time = time.time()
    solucao_algoritmo_genetico.start()
    end_time = time.time()
    print(f"Tempo de execucao: {end_time - start_time} seconds")


main()