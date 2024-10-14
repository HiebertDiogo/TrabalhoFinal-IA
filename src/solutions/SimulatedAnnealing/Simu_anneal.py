import random
from math import exp

class TSP_SimulatedAnnealing:
    def __init__(self, distancias, Tm=1000, iter_max=10000, cooling_factor=0.999):
        self.distancias = distancias
        self.Tm = Tm
        self.iter_max = iter_max
        self.cooling_factor = cooling_factor
        self.intermediate_costs = []
        self.intermediate_tempr = []
        self.x = 0
    
    def start(self):
        path = [i for i in range(len(self.distancias))]
        # path = initial_path.copy()
        cost = self.tour_cost(path)
        self.intermediate_costs.append(cost)
        self.intermediate_tempr.append(self.Tm)
        n = len(path)
        
        for i in range(1, self.iter_max):
            two_indices = random.sample(range(1, n), 2)
            next_path = path.copy()
            # Reverte a sublista (vizinhança)
            next_path[two_indices[0]:two_indices[1]+1] = next_path[two_indices[0]:two_indices[1]+1][::-1]
            next_cost = self.tour_cost(next_path)
            dE = cost - next_cost  # Delta Energia
            T = self.Tm * (self.cooling_factor ** i)  # Resfriamento exponencial
            
            if T <= 1e-6:
                break
            
            try:
                pb = 1 / (1 + exp(-dE / T))
            except OverflowError:
                pb = 0
            
            if dE > 0:
                path = next_path.copy()
                cost = next_cost
            else:
                if random.random() < pb:
                    path = next_path.copy()
                    cost = next_cost
            
            self.intermediate_costs.append(cost)
            self.intermediate_tempr.append(T)
            self.x += 1

        print('\n----------------------- Resultados com Simulated Annealing ----------------------')
        print("\nRota:", path + [0])
        print("Custo total:", self.tour_cost(path))

        return 
    
    def tour_cost(self, path):
        _path = path + [0]
        return sum(self.distancias[_path[i-1]][_path[i]] for i in range(len(_path))) 