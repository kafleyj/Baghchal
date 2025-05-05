# from .q_learning_agent import QLearningAgent
# from .environment import BaagchalEnv
# from .utils import get_reward

from baagchal_rl.q_learning_agent import QLearningAgent
from baagchal_rl.environment import BaagchalEnv
from baagchal_rl.utils import get_reward



def train(agent: QLearningAgent, game_factory, episodes=10000):
    rewards_per_episode = []
    steps_per_episode = []
    win_history = []

    print("🚀 Training started...")

    for ep in range(episodes):
        game = game_factory()
        env = BaagchalEnv(game)
        player = "Goat" if ep % 2 == 0 else "Tiger"

        episode_reward = 0
        steps = 0

        while not game.is_game_over():
            state = env.get_state()
            legal_actions = env.get_legal_actions(player)
            if not legal_actions:
                break

            action = agent.choose_action(state, legal_actions)
            next_game = env.apply_action(action, player)
            next_env = BaagchalEnv(next_game)

            reward = get_reward(next_game, player)
            next_state = next_env.get_state()
            next_legal_actions = next_env.get_legal_actions(player)

            agent.update(state, action, reward, next_state, next_legal_actions)

            episode_reward += reward
            steps += 1

            game = next_game
            env = next_env
            player = "Tiger" if player == "Goat" else "Goat"

        rewards_per_episode.append(episode_reward)
        steps_per_episode.append(steps)
        win_history.append(game.winner)

        if ep % 100 == 0:
            print(f"Episode {ep}: Winner - {game.winner} | Steps: {steps} | Reward: {round(episode_reward, 2)}")

    print("\n✅ Training complete.")

    # Save Q-table
    agent.save("baagchal_q_table.pkl")
    print("💾 Q-table saved as 'baagchal_q_table.pkl'")

    # Save training metrics
    with open("training_metrics.pkl", "wb") as f:
        pickle.dump({
            "rewards": rewards_per_episode,
            "steps": steps_per_episode,
            "wins": win_history
        }, f)

    print("📊 Training metrics saved as 'training_metrics.pkl'")


# Optional entry point for direct execution
if __name__ == "__main__":
    from game import Game

    def game_factory():
        g = Game()
        g.board_init()
        g.reload_config()
        return g

    agent = QLearningAgent(alpha=0.1, gamma=0.95, epsilon=0.2)
    train(agent, game_factory, episodes=10000)
