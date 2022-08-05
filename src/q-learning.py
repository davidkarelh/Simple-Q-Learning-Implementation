import random
from game import Game


class QLearning:
    __iterations_rewards = []
    iteration_count = 1000
    max_step = 100

    learning_rate = 0.1
    discount_rate = 0.99

    exploration_rate = 1
    max_exploration_rate = 1
    min_exploration_rate = 0.01
    exploration_decay_rate = 0.001
    q_table = [[0, 0] for i in range(10)]

    def __init__(self) -> None:
        pass

    def __q_learning(self):
        for iteration in range(self.iteration_count):
            game = Game()
            current_step_reward = 0

            for step in range(self.max_step):
                exploit_now = False
                exploration_rate_threshold = random.uniform(0, 1)

                if (exploration_rate_threshold > self.exploration_rate):
                    exploit_now = True
                
                if (exploit_now):
                    if (self.q_table[game.playerIndex][0] == 0):
                        pass
                    elif (self.q_table[game.playerIndex][1] == 0):
                        pass
                    else:
                        pass
                else:
                    if (self.q_table[game.playerIndex][0] > self.q_table[game.playerIndex][1]):
                        pass
                    elif (self.q_table[game.playerIndex][1] > self.q_table[game.playerIndex][0]):
                        pass
                    else:
                        pass
                


