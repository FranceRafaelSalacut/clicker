import gymnasium as gym
import ale_py
import os
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv
from stable_baselines3.common.evaluation import evaluate_policy

gym.register_envs(ale_py)

epochs = 0

frames = []  # for animation
done = False
log_path = os.path.join("runs", "train")
ppo_path = os.path.join(log_path, "ppo_breakout")

env = gym.make("ALE/Breakout-v5", render_mode="human")
env = DummyVecEnv([lambda: env])
model = PPO('MlpPolicy', env, verbose=1, tensorboard_log=log_path)
#env = gym.make("BipedalWalker-v3", render_mode="human")
#observation, info = env.reset()
#terminated = False

print(env.action_space)
print(env.observation_space)

model.learn(total_timesteps=10**10)
model.save(ppo_path)

#model = PPO.load(ppo_path, env=env)
evaluate_policy(model, env, n_eval_episodes=10, render=True)
