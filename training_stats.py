import pickle
import matplotlib.pyplot as plt
import numpy as np

# Load training metrics
with open("training_metrics.pkl", "rb") as f:
    metrics = pickle.load(f)

rewards = metrics["rewards"]
steps = metrics["steps"]
wins = metrics["wins"]

def moving_average(data, window_size=100):
    return np.convolve(data, np.ones(window_size) / window_size, mode='valid')

win_binary = [1 if w == "Goat" else 0 for w in wins]

# --- Plot 1: Rewards per Episode ---
plt.plot(rewards)
plt.title("Rewards per Episode")
plt.xlabel("Episode")
plt.ylabel("Total Reward")
plt.grid(True)
plt.savefig("plot_rewards_per_episode.png")
plt.clf()

# --- Plot 2: Moving Average of Rewards ---
plt.plot(moving_average(rewards))
plt.title("Moving Average of Rewards (Window = 100)")
plt.xlabel("Episode")
plt.ylabel("Avg Reward")
plt.grid(True)
plt.savefig("plot_rewards_moving_avg.png")
plt.clf()

# --- Plot 3: Steps per Episode ---
plt.plot(steps)
plt.title("Steps per Episode")
plt.xlabel("Episode")
plt.ylabel("Steps")
plt.grid(True)
plt.savefig("plot_steps_per_episode.png")
plt.clf()

# --- Plot 4: Cumulative Rewards ---
plt.plot(np.cumsum(rewards))
plt.title("Cumulative Rewards")
plt.xlabel("Episode")
plt.ylabel("Cumulative Reward")
plt.grid(True)
plt.savefig("plot_cumulative_rewards.png")
plt.clf()

# --- Plot 5: Win Rate (Goat wins) ---
plt.plot(moving_average(win_binary))
plt.title("Goat Win Rate (Moving Average)")
plt.xlabel("Episode")
plt.ylabel("Win Rate")
plt.grid(True)
plt.savefig("plot_goat_win_rate.png")
plt.clf()

# --- Plot 6: Role-wise Reward Comparison ---
goat_rewards = [rewards[i] for i in range(len(rewards)) if i % 2 == 0]
tiger_rewards = [rewards[i] for i in range(len(rewards)) if i % 2 != 0]
plt.plot(goat_rewards, label="Goat")
plt.plot(tiger_rewards, label="Tiger")
plt.title("Role-wise Reward Comparison")
plt.xlabel("Episode")
plt.ylabel("Reward")
plt.legend()
plt.grid(True)
plt.savefig("plot_rolewise_rewards.png")
plt.clf()

# --- Plot 7: Reward Distribution ---
plt.hist(rewards, bins=30, edgecolor='black')
plt.title("Reward Distribution")
plt.xlabel("Reward")
plt.ylabel("Frequency")
plt.grid(True)
plt.savefig("plot_reward_distribution.png")
plt.clf()

print("✅ All plots have been saved successfully.")
