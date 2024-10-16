from docplex.mp.model import Model
# from instances.intance import Instance
# import numpy as np

class TSP_ProgramacaoLinear():
    def __init__(self, distances):
        self.distances = distances

    def start(self):

        distancias = self.distances

        n = len(distancias)
        modelo = Model('CaixeiroViajante')

        # Variáveis de decisão
        x = {(i, j): modelo.binary_var(name=f'x_{i}_{j}') for i in range(n) for j in range(n) if i != j}
        u = {i: modelo.continuous_var(name=f'u_{i}', lb=0, ub=n-1) for i in range(n)}

        # Função objetivo
        modelo.minimize(modelo.sum(distancias[i][j] * x[i, j] for i in range(n) for j in range(n) if i != j))

        # Restrições
        for i in range(n):
            modelo.add_constraint(modelo.sum(x[i, j] for j in range(n) if i != j) == 1)
            modelo.add_constraint(modelo.sum(x[j, i] for j in range(n) if i != j) == 1)

        # Restrições de sub-rotas
        for i in range(1, n):
            for j in range(1, n):
                if i != j:
                    modelo.add_constraint(u[i] - u[j] + n * x[i, j] <= n-1)

        solucao = modelo.solve()

        print('\n----------------------- Resultados com Programação Linear ----------------------\n')
        if solucao:
            solucao_rota = {(i, j): x[i, j].solution_value for i in range(n) for j in range(n) if i != j and x[i, j].solution_value > 0.5}
            
            # Um dicionário que mapeia a próxima cidade a partir de cada cidade
            next_city = {i: j for (i, j), val in solucao_rota.items() if val > 0.5}
            
            # Reconstroi a rota começando pela cidade de origem
            origem = 0
            rota = [origem]
            while len(rota) < n:
                proxima = next_city[rota[-1]]
                rota.append(proxima)
            
            # Retorna a origem
            rota.append(origem)

            print("Rota:", rota)
            print("Custo total:", modelo.objective_value)
        else:
            print("Nenhuma solução encontrada")