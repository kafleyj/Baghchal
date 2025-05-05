"""
Baagchal RL Package
This package provides tools for training and using reinforcement learning agents
to play the traditional Nepali board game Baagchal.
"""

from .q_learning_agent import QLearningAgent
from .environment import BaagchalEnv
from .trainer import train
from .utils import encode_board, decode_board, get_reward

__all__ = [
    "QLearningAgent",
    "BaagchalEnv",
    "train",
    "encode_board",
    "decode_board",
    "get_reward"
]
