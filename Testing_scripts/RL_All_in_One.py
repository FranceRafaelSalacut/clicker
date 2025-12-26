import gymnasium as gym
import ale_py
import os
from stable_baselines3 import PPO
from stable_baselines3 import DQN
from stable_baselines3.common.vec_env import DummyVecEnv
from stable_baselines3.common.evaluation import evaluate_policy
from stable_baselines3.common.callbacks import EvalCallback, StopTrainingOnRewardThreshold

gym.register_envs(ale_py)


def MAKE_MODEL_PATH(log_path, model_name, count=0):
    temp = os.path.join(log_path, model_name+"_"+str(count))
    count+=1

    if os.path.exists(temp):
        return MAKE_PPO_PATH(log_path, model_name, count)
    else:
        os.makedirs(temp)
        return temp

def RL_TRAIN(game, policy, log_path, ppo_path):
    env = gym.make(game)
    env = DummyVecEnv([lambda: env])
    model = PPO(policy ,env, verbose=0, tensorboard_log=log_path)

    stop_callback = StopTrainingOnRewardThreshold(reward_threshold=200, verbose= 1)
    eval_callback = EvalCallback(env, 
                                 callback_on_new_best=stop_callback,
                                 eval_freq=10000,
                                 best_model_save_path=ppo_path,
                                 verbose=1)

    model.learn(total_timesteps=200000, callback=eval_callback)
    #model.save(ppo_path)
    env.close()

def RL_EVAL(game, ppo_path):
    env = gym.make(game, render_mode="human")
    env = DummyVecEnv([lambda: env])
    ppo_path = os.path.join(ppo_path, "best_model")

    print(env.action_space)
    print(env.observation_space)

    model = PPO.load(ppo_path, env=env)
    evaluate_policy(model, env, n_eval_episodes=10, render=True)
    env.close()

def RL_RANDOM_PLAY(game, episodes):
    env = gym.make(game, render_mode="human")
    for episode in range(0, episodes):
        observation = env.reset()
        done = False
        score = 0

        while not done:
            env.render()
            action = env.action_space.sample()
            observation, reward, done, truncated, info = env.step(action)
            score = score + reward

        print(f"Episode: {episode}, Score: {score}")
    
    env.close()

def RL_MODEL_TEST(game, episodes, ppo_path):
    env = gym.make(game, render_mode="human")
    model = PPO.load(ppo_path, env=env)
    for episode in range(0, episodes):
        observation, _ = env.reset()
        done = False
        truncated = False
        score = 0

        while not done and not truncated :
            env.render()
            action, _ = model.predict(observation)
            observation, reward, donede, truncated, info = env.step(action)
            score = score + reward
            #print(score, donede, truncated)

        print(f"Episode: {episode}, Score: {score}")
    env.close()

def main():
    game = "CartPole-v1"#"ALE/Breakout-v5"
    policy = "MlpPolicy"
    model_name = "ppo_cartpole_mlppolicy"
    log_path = os.path.join("runs", "train")
    model_save_path = MAKE_MODEL_PATH(log_path, model_name)
    

<<<<<<< HEAD
    #RL_TRAIN(game, policy, log_path, model_save_path)
    #RL_EVAL(game, model_save_path)
    #RL_RANDOM_PLAY(game, 5)
    RL_MODEL_TEST(game, 5, model_save_path)
=======
    RL_TRAIN(game, policy, log_path, model_save_path)
    RL_EVAL(game, model_save_path)
    #RL_RANDOM_PLAY(game, 5)
    #RL_MODEL_TEST(game, 5, ppo_path)
>>>>>>> 408a2ef (Commiting a Bunch of Reinforce Learning scripts for Studying)

main()