# main.py

from q_learning_agent import QLearningAgent
from trainer import train

# IMPORTANT: Replace this with your actual Game class import
from game import Game  

def game_factory():
    """Creates a new instance of the game for each episode."""
    game = Game()
    game.board_init()
    game.reload_config()
    return game

def main():
    print("Initializing Q-learning agent for Baagchal...")
    
    # Initialize agent with learning rate (alpha), discount factor (gamma), and exploration rate (epsilon)
    agent = QLearningAgent(alpha=0.1, gamma=0.95, epsilon=0.2)

    # Train the agent
    episodes = 1000  # You can increase this to 10,000+ for better performance
    print(f"Starting training for {episodes} episodes...")
    train(agent, game_factory, episodes=episodes)

    # Save Q-table
    agent.save("baagchal_q_table.pkl")
    print("Training complete. Q-table saved as 'baagchal_q_table.pkl'.")

if __name__ == "__main__":
    main()
