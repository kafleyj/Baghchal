import random
import pickle
from collections import defaultdict

class QLearningAgent:
    def __init__(self, alpha=0.1, gamma=0.95, epsilon=0.2):
        self.q_table = defaultdict(lambda: defaultdict(float))
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon

    def choose_action(self, state, legal_actions):
        if random.random() < self.epsilon:
            return random.choice(legal_actions)
        q_values = self.q_table[state]
        return max(legal_actions, key=lambda a: q_values[str(a)])

    def update(self, state, action, reward, next_state, next_legal_actions):
        action = str(action)
        max_future_q = 0
        if next_legal_actions:
            max_future_q = max(self.q_table[next_state][str(a)] for a in next_legal_actions)

        old_value = self.q_table[state][action]
        self.q_table[state][action] = old_value + self.alpha * (reward + self.gamma * max_future_q - old_value)

    def save(self, path='q_agent.pkl'):
        with open(path, 'wb') as f:
            pickle.dump(dict(self.q_table), f)

    def load(self, path='q_agent.pkl'):
        with open(path, 'rb') as f:
            loaded = pickle.load(f)
            self.q_table = defaultdict(lambda: defaultdict(float), loaded)
