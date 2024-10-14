import gym
from gym import spaces
import numpy as np

class DeliveryEnvironment(gym.Env):
    def __init__(self, distancias):
        super(DeliveryEnvironment, self).__init__()
        self.distancias = np.array(distancias)
        self.num_cidades = len(distancias)
        self.action_space = spaces.Discrete(self.num_cidades)
        self.observation_space = spaces.Tuple((
            spaces.Discrete(self.num_cidades),
            spaces.MultiBinary(self.num_cidades)
        ))
        self.state = None
        self.visited = None
        self.current_city = None
        self.route = []
        self.done = False

    def reset(self):
        self.visited = np.zeros(self.num_cidades, dtype=int)
        self.current_city = 0
        self.visited[self.current_city] = 1
        self.route = [self.current_city]
        self.state = (self.current_city, self.visited.copy())
        self.done = False
        return self.encode_state(self.state)
    
    def step(self, action):
        if self.done:
            return self.encode_state(self.state), 0.0, self.done, {}
        
        if self.visited[action] == 1 or action == self.current_city:
            return self.encode_state(self.state), -10.0, self.done, {}
        
        previous_city = self.current_city
        self.current_city = action
        self.visited[self.current_city] = 1
        self.route.append(self.current_city)
        
        reward = -self.distancias[previous_city, self.current_city]
        penalty = len(self.route)  # Penalização pelo comprimento da rota
        
        if np.sum(self.visited) == self.num_cidades:
            reward -= self.distancias[self.current_city, 0]
            penalty = len(self.route) * 2  # Penalização aumentada pelo comprimento total
            self.done = True
            self.route.append(0)
            reward += 100  # Recompensa bônus por completar a rota
        
        reward -= penalty
        self.state = (self.current_city, self.visited.copy())
        return self.encode_state(self.state), reward, self.done, {}
    
    def render(self):
        print(f"Current city: {self.current_city}")
        print(f"Visited: {self.visited}")
        
    def encode_state(self, state):
        current_city, visited = state
        return current_city * (2 ** self.num_cidades) + int("".join(str(int(b)) for b in visited), 2)
    
    def get_route(self):
        return [int(x) for x in self.route]

    def get_custo(self):
        _path = self.route
        #mat = self.distancias
        return sum(self.distancias[_path[i-1]][_path[i]] for i in range(len(_path)))