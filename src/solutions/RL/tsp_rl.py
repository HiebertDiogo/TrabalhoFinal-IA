from solutions.RL.DeliveryEnvironment import DeliveryEnvironment
from solutions.RL.QAgent import QAgent
import numpy as np

class TSP_RL:
    def __init__(self):
        pass

    def treinar(self, matrizes):
        # distancias_exemplos = [
        #     [
        #         [0, 2, 9, 10],
        #         [1, 0, 6, 4],
        #         [15, 7, 0, 8],
        #         [6, 3, 12, 0]
        #     ],
        #     [
        #         [0, 3, 4, 2],
        #         [3, 0, 1, 5],
        #         [4, 1, 0, 6],
        #         [2, 5, 6, 0]
        #     ],
        #     [
        #         [0, 5, 8, 3],
        #         [5, 0, 4, 6],
        #         [8, 4, 0, 7],
        #         [3, 6, 7, 0]
        #     ],
        #     [
        #         [0, 2, 7, 4],
        #         [2, 0, 6, 3],
        #         [7, 6, 0, 5],
        #         [4, 3, 5, 0]
        #     ],
        #     [
        #         [0, 6, 3, 2],
        #         [6, 0, 1, 7],
        #         [3, 1, 0, 4],
        #         [2, 7, 4, 0]
        #     ]
        # ]

        env = DeliveryEnvironment(matrizes[0])
        states_size = env.num_cidades * (2 ** env.num_cidades)
        actions_size = env.action_space.n
        agent = QAgent(states_size=states_size, actions_size=actions_size)

        num_episodios = 1000
        for episodio in range(num_episodios):
            for distancias in matrizes:
                env = DeliveryEnvironment(distancias)
                env, agent, episodio_recompensa, rota, custo = self.run_episode(env, agent, verbose=0)

        return agent

    def start(self, agent, distancias):
        env = DeliveryEnvironment(distancias)
        env, agent, episodio_recompensa, rota, custo = self.run_episode(env, agent, verbose=0)

        print('\n----------------------- Resultados Aprendizado com reforço ----------------------')
        print("\nRota:", rota)
        print("Custo total:", custo)
        print(f"Recompensa do episódio final: {episodio_recompensa}")


    def run_episode(self, env, agent, verbose=1):
        s = env.reset()
        max_step = env.num_cidades
        episode_reward = 0

        i = 0
        while i < max_step:
            valid_actions = np.where(env.visited == 0)[0]
            if len(valid_actions) == 0:
                break
            a = agent.act(s, valid_actions)
            s_next, r, done, _ = env.step(a)
            r = -1 * r
            #if verbose:
                #print(f"Estado: {s}, Ação: {a}, Próximo Estado: {s_next}, Recompensa: {r}, Feito: {done}")
            agent.train(s, a, r, s_next)
            episode_reward += r
            s = s_next
            i += 1
            if done:
                break

        return env, agent, episode_reward, env.get_route(), env.get_custo(),
