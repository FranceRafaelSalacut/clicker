import gymnasium as gym
import ale_py
import os
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv
from stable_baselines3.common.evaluation import evaluate_policy

gym.register_envs(ale_py)

log_path = os.path.join("runs", "train")
ppo_path = os.path.join(log_path, "ppo_breakout_CNN")

env = gym.make("ALE/Breakout-v5", render_mode="human")
env = DummyVecEnv([lambda: env])


print(env.action_space)
print(env.observation_space)

model = PPO.load(ppo_path, env=env)
evaluate_policy(model, env, n_eval_episodes=10, render=True)
