import numpy as np
import sys
import random


class TSP_LocalSearch:
    def __init__(self, distance_matrix):
        self.distance_matrix = distance_matrix
        


    def calculate_cost(self, tour):
        cost = 0.0
        for i in range(len(tour) - 1):
            cost += self.distance_matrix[tour[i]][tour[i + 1]]
        cost += self.distance_matrix[tour[-1]][tour[0]]
        return cost

    def cheapest_insertion(self, tour):
        n = len(self.distance_matrix)
        visited = [False] * n  # Marcar nós visitados

        tour.append(0)  # Começa no nó 0
        visited[0] = True

        # Encontrar o nó mais próximo ao inicial
        nearest_node = -1
        min_distance = float('inf')
        for i in range(1, n):
            if self.distance_matrix[0][i] < min_distance:
                min_distance = self.distance_matrix[0][i]
                nearest_node = i

        tour.append(nearest_node)
        visited[nearest_node] = True

        while len(tour) < n:
            best_node = -1
            best_cost = float('inf')
            best_position = -1

            for node in range(n):
                if not visited[node]:
                    for i in range(len(tour)):
                        next_node = (i + 1) % len(tour)
                        cost_increase = self.distance_matrix[tour[i]][node] + self.distance_matrix[node][tour[next_node]] - self.distance_matrix[tour[i]][tour[next_node]]

                        if cost_increase < best_cost:
                            best_cost = cost_increase
                            best_node = node
                            best_position = next_node

            # Inserir o nó na melhor posição
            tour.insert(best_position, best_node)
            visited[best_node] = True

        return tour

    def VND(self, best_solution, best_cost):
        improvement = True

        while improvement:
            improvement = False
            k = 0

            while k < 2:
                new_cost = best_cost

                if k == 0:  # Estrutura de vizinhança Swap
                    new_cost = self.swap(new_cost, best_solution)
                elif k == 1:  # Estrutura de vizinhança Reinsertion
                    new_cost = self.reinsertion(new_cost, best_solution)

                # Se a nova solução for melhor, atualiza a solução atual
                if new_cost < best_cost:
                    best_cost = new_cost
                    improvement = True  # Encontra melhoria, reinicia o ciclo de vizinhança
                    k = 0  # Voltar para a primeira vizinhança
                else:
                    k += 1  # Passar para a próxima vizinhança

        return best_cost


    def swap(self, best_cost, best_solution):
        swap_cost = 0
        best_i = 0
        best_j = 0
        temp_solution = best_cost

        for i in range(len(best_solution) - 1):
            for j in range(i + 1, len(best_solution)):
                swap_cost = temp_solution

                swap_cost -= self.distance_matrix[best_solution[i]][best_solution[i + 1]]

                if j != i + 1:  # Não adjacentes
                    swap_cost -= self.distance_matrix[best_solution[j - 1]][best_solution[j]]
                    swap_cost += self.distance_matrix[best_solution[j]][best_solution[i + 1]]
                    swap_cost += self.distance_matrix[best_solution[j - 1]][best_solution[i]]
                else:
                    swap_cost += self.distance_matrix[best_solution[j]][best_solution[i]]

                if i > 0:
                    swap_cost -= self.distance_matrix[best_solution[i - 1]][best_solution[i]]
                    swap_cost += self.distance_matrix[best_solution[i - 1]][best_solution[j]]

                if j < len(best_solution) - 1:
                    swap_cost -= self.distance_matrix[best_solution[j]][best_solution[j + 1]]
                    swap_cost += self.distance_matrix[best_solution[i]][best_solution[j + 1]]

                if i == 0 and j == len(best_solution) - 1:  # OK
                    swap_cost -= self.distance_matrix[best_solution[j]][best_solution[i]]
                    swap_cost += self.distance_matrix[best_solution[i]][best_solution[j]]
                elif i == 0 and j < len(best_solution) - 1:  # OK
                    swap_cost -= self.distance_matrix[best_solution[len(best_solution) - 1]][best_solution[i]]
                    swap_cost += self.distance_matrix[best_solution[len(best_solution) - 1]][best_solution[j]]
                elif i > 0 and j == len(best_solution) - 1:  # OK
                    swap_cost -= self.distance_matrix[best_solution[j]][best_solution[0]]
                    swap_cost += self.distance_matrix[best_solution[i]][best_solution[0]]

                if swap_cost < best_cost:
                    best_cost = swap_cost
                    best_i = i
                    best_j = j

        # Realiza o swap
        best_solution[best_i], best_solution[best_j] = best_solution[best_j], best_solution[best_i]

        return best_cost

    def reinsertion(self, best_cost, best_solution):
        best_i, best_j = 0, 0
        temp_solution = best_cost

        for i in range(len(best_solution) - 2):
            for j in range(i + 2, len(best_solution)):
                reinsertion_cost = temp_solution

                reinsertion_cost -= self.distance_matrix[best_solution[i]][best_solution[i + 1]]
                reinsertion_cost += self.distance_matrix[best_solution[j]][best_solution[i]]

                if i > 0:
                    reinsertion_cost -= self.distance_matrix[best_solution[i - 1]][best_solution[i]]
                    reinsertion_cost += self.distance_matrix[best_solution[i - 1]][best_solution[i + 1]]

                if j < len(best_solution) - 1:
                    reinsertion_cost -= self.distance_matrix[best_solution[j]][best_solution[j + 1]]
                    reinsertion_cost += self.distance_matrix[best_solution[i]][best_solution[j + 1]]

                if i == 0 and j == len(best_solution) - 1:
                    reinsertion_cost -= self.distance_matrix[best_solution[j]][best_solution[i]]
                    reinsertion_cost += self.distance_matrix[best_solution[i]][best_solution[i + 1]]
                elif i == 0 and j < len(best_solution) - 1:
                    reinsertion_cost -= self.distance_matrix[best_solution[-1]][best_solution[i]]
                    reinsertion_cost += self.distance_matrix[best_solution[-1]][best_solution[i + 1]]
                elif i > 0 and j == len(best_solution) - 1:
                    reinsertion_cost -= self.distance_matrix[best_solution[j]][best_solution[0]]
                    reinsertion_cost += self.distance_matrix[best_solution[i]][best_solution[0]]

                if reinsertion_cost < best_cost:
                    best_cost = reinsertion_cost
                    best_i, best_j = i, j

        node = best_solution[best_i]
        return_solution = best_cost

        best_solution.insert(best_j + 1, node)
        best_solution.pop(best_i)  # Remove o elemento no índice best_i

        return return_solution

    def perturbacao(self, copia, swap_cost):
        i, j = -1, -1

        # Gera i e j diferentes
        while i == j and i > j:
            i = random.randint(0, len(copia) - 2)
            j = random.randint(0, len(copia) - 1)

        swap_cost -= self.distance_matrix[copia[i]][copia[i + 1]]

        if j != i + 1:  # Não adjacentes
            swap_cost -= self.distance_matrix[copia[j - 1]][copia[j]]
            swap_cost += self.distance_matrix[copia[j]][copia[i + 1]]
            swap_cost += self.distance_matrix[copia[j - 1]][copia[i]]
        else:
            swap_cost += self.distance_matrix[copia[j]][copia[i]]

        if i > 0:
            swap_cost -= self.distance_matrix[copia[i - 1]][copia[i]]
            swap_cost += self.distance_matrix[copia[i - 1]][copia[j]]

        if j < len(copia) - 1:
            swap_cost -= self.distance_matrix[copia[j]][copia[j + 1]]
            swap_cost += self.distance_matrix[copia[i]][copia[j + 1]]

        if i == 0 and j == len(copia) - 1:  # OK
            swap_cost -= self.distance_matrix[copia[j]][copia[i]]
            swap_cost += self.distance_matrix[copia[i]][copia[j]]
        elif i == 0 and j < len(copia) - 1:  # OK
            swap_cost -= self.distance_matrix[copia[len(copia) - 1]][copia[i]]
            swap_cost += self.distance_matrix[copia[len(copia) - 1]][copia[j]]
        elif i > 0 and j == len(copia) - 1:  # OK
            swap_cost -= self.distance_matrix[copia[j]][copia[0]]
            swap_cost += self.distance_matrix[copia[i]][copia[0]]

        # Realiza o swap
        copia[i], copia[j] = copia[j], copia[i]

        return swap_cost


    def ILS(self, best_solution, best_cost):
        s_ILS = 0.0
        s_VND = 0.0
        s_perturbacao = 0.0
        contador = 0
        nao_melhorou = 0
        copia = []

        # Inicializa a solução usando VND
        s_VND = self.VND(best_solution, best_cost)

        # Copia a solução atual para a solução de backup
        copia = best_solution.copy()

        while contador < 100 and nao_melhorou < 7:
            # Aplica a perturbação à solução copiada
            s_perturbacao = self.perturbacao(copia, s_VND)
            # Executa o VND na solução perturbada
            s_ILS = self.VND(copia, s_perturbacao)

            # Verifica se a nova solução é melhor
            if s_ILS < s_VND:
                s_VND = s_ILS
                nao_melhorou = 0
            else:
                nao_melhorou += 1
            
            contador += 1

        return s_VND


    def start(self):
        solution = []

        self.cheapest_insertion(solution)

        solution_value = self.calculate_cost(solution)
        
        solution_value = self.ILS(solution, solution_value)

        print("\n----------------------- Resultados com Busca Local ----------------------")
        print("Rota: ", end="")
        print(" ".join(map(str, solution)))
        print(f"Custo total: {solution_value:.3f}")
