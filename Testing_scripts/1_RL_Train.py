import gymnasium as gym
import ale_py
import os
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv
from stable_baselines3.common.evaluation import evaluate_policy

gym.register_envs(ale_py)

log_path = os.path.join("runs", "train")
ppo_path = os.path.join(log_path, "ppo_cartpole_out")


env = gym.make("CartPole-v1")
env = DummyVecEnv([lambda: env])
model = PPO('MlpPolicy',env,verbose=0, tensorboard_log=log_path)

model.learn(total_timesteps=200000)
model.save(ppo_path)
