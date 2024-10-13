from instances.intance import Instance
import random

class TSP_AlgoritmoGenetico:
    def __init__(self, distancias, populacao_tamanho=10, geracoes=100, taxa_mutacao=0.1):
        self.distancias = distancias
        self.populacao_tamanho = populacao_tamanho
        self.geracoes = geracoes
        self.taxa_mutacao = taxa_mutacao
    
    def start(self):
        # Criando a população inicial
        populacao = self.criar_populacao(self.populacao_tamanho, len(self.distancias))

        # Algoritmo Genético
        for geracao in range(self.geracoes):
            nova_populacao = []
            fitnesses = []
            for individuo in populacao:
                distancia = self.calcular_distancia(individuo)
                if distancia == 0:
                    distancia += 1e-9  # Pequeno valor para evitar divisão por zero
                fitnesses.append(1 / distancia)
                
            for _ in range(self.populacao_tamanho):
                pai1 = self.selecao_roleta(populacao, fitnesses)
                pai2 = self.selecao_roleta(populacao, fitnesses)
                filho = self.crossover(pai1, pai2)
                self.mutacao(filho)
                nova_populacao.append(filho)
                
            populacao = nova_populacao

        # Melhor solução encontrada
        melhor_caminho = min(populacao, key=self.calcular_distancia)
        
        print('\n----------------------- Resultados com Algoritmo Genético ----------------------')
        print("\nRota:", [0] + melhor_caminho[1:] + [0])
        print("Custo total:", self.calcular_distancia(melhor_caminho)) 

    def calcular_distancia(self, caminho):
        distancia = sum(self.distancias[caminho[i-1]][caminho[i]] for i in range(len(caminho)))
        distancia += self.distancias[caminho[-1]][caminho[0]]  # Adiciona o custo de voltar à cidade inicial
        return distancia

    def criar_caminho(self, n):
        caminho = list(range(1, n))
        random.shuffle(caminho)
        return [0] + caminho

    def criar_populacao(self, tamanho, n):
        return [self.criar_caminho(n) for _ in range(tamanho)]

    def crossover(self, pai1, pai2):
        tamanho = len(pai1)
        ponto1, ponto2 = sorted(random.sample(range(1, tamanho), 2))
        filho = pai1[:ponto1] + [cidade for cidade in pai2 if cidade not in pai1[:ponto1]]
        return [0] + filho[1:]

    def mutacao(self, caminho):
        for _ in range(len(caminho)):
            if random.random() < self.taxa_mutacao:
                i, j = random.sample(range(1, len(caminho)), 2)
                caminho[i], caminho[j] = caminho[j], caminho[i]

    def selecao_roleta(self, populacao, fitnesses):
        soma_fitness = sum(fitnesses)
        pick = random.uniform(0, soma_fitness)
        atual = 0
        for i, fitness in enumerate(fitnesses):
            atual += fitness
            if atual > pick:
                #print(f"Selecionado: {populacao[i]} com fitness {fitness}")  # Debug
                return populacao[i]
        #print("Nenhuma seleção válida, retornando o último")  # Debug
        return populacao[-1]
