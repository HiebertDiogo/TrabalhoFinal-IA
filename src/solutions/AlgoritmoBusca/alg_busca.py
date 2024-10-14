import heapq

class TSP_AStar:
    def __init__(self, distancias):
        self.distancias = distancias
        self.n = len(distancias)
        self.path = []
        self.cost = float('inf')
    
    def heuristica(self, cidade_atual, visitada):
        """
        Heurística usada: Soma das distâncias mínimas para cada cidade não visitada
        mais a distância mínima para retornar ao ponto de partida.
        """
        naoVisitada = set(range(self.n)) - set(visitada)
        if not naoVisitada:
            return self.distancias[cidade_atual][0]  # Retorno ao início

        min_naoVisitada = min([self.distancias[cidade_atual][cidade] for cidade in naoVisitada])
        
        # Soma das distâncias mínimas entre todas as cidades não visitadas
        min_entre_naoVisitada = 0
        if len(naoVisitada) > 1:
            # Para eficiência, consideramos apenas a distância mínima de cada cidade não visitada
            min_entre_naoVisitada = sum([min([self.distancias[cidade][other] for other in naoVisitada if other != cidade]) for cidade in naoVisitada])
        
        min_returno = min([self.distancias[cidade][0] for cidade in naoVisitada])
        
        return min_naoVisitada + min_entre_naoVisitada + min_returno

    def start(self):
        # Representação do Estado: (f, g, cidade_atual, path)
        estado_inicial = (self.heuristica(0, [0]), 0, 0, [0])
        open_set = []
        heapq.heappush(open_set, estado_inicial)
        
        visitada_states = set()

        while open_set:
            f, g, cidade_atual, path = heapq.heappop(open_set)
            
            if len(path) == self.n:
                custo_total = g + self.distancias[cidade_atual][0]
                if custo_total < self.cost:
                    self.cost = custo_total
                    self.path = path + [0]
                continue
 
            state_id = (cidade_atual, tuple(sorted(path)))
            if state_id in visitada_states:
                continue
            visitada_states.add(state_id)
            
            for prox_cidade in range(self.n):
                if prox_cidade not in path:
                    new_g = g + self.distancias[cidade_atual][prox_cidade]
                    new_path = path + [prox_cidade]
                    h = self.heuristica(prox_cidade, new_path)
                    new_f = new_g + h
                    heapq.heappush(open_set, (new_f, new_g, prox_cidade, new_path))
        
        print('\n----------------------- Resultados com A* ----------------------')
        print("\nRota:", self.path)
        print("Custo total:", self.cost)