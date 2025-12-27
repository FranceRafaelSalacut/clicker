import gymnasium as gym
import ale_py
import os
import warnings
from stable_baselines3 import PPO
from stable_baselines3 import DQN
from stable_baselines3.common.vec_env import DummyVecEnv
from stable_baselines3.common.evaluation import evaluate_policy
from stable_baselines3.common.callbacks import EvalCallback, StopTrainingOnRewardThreshold, StopTrainingOnNoModelImprovement

gym.register_envs(ale_py)
#warnings.filterwarnings("ignore")

def MAKE_MODEL_PATH(log_path, model_name, count=0):
    temp = os.path.join(log_path, model_name+"_"+str(count))
    count+=1

    if os.path.exists(temp):
        return MAKE_MODEL_PATH(log_path, model_name, count)
    else:
        os.makedirs(temp)
        return temp

def FIND_LATEST_MODEL(log_path, model_name, count=0):
    temp = os.path.join(log_path, model_name+"_"+str(count))
    
    if os.path.exists(temp):
        count+=1
        return FIND_LATEST_MODEL(log_path, model_name, count)
    else:
        count-=1
        latest = os.path.join(log_path, model_name+"_"+str(count), "best_model")
        return latest

def RL_TRAIN(game, policy, log_path, model_name, reward_threshold=200):
    env = gym.make(game)
    env = DummyVecEnv([lambda: env])
    model = PPO(policy ,env, verbose=0, tensorboard_log=log_path)
    callback_save = MAKE_MODEL_PATH(log_path, model_name)
    final_save = os.path.join(callback_save, "latest_model")

    #stop_callback = StopTrainingOnRewardThreshold(reward_threshold=reward_threshold, verbose= 1)
    stop_callback = StopTrainingOnNoModelImprovement(max_no_improvement_evals=5, min_evals=0, verbose=1)
    eval_callback = EvalCallback(env, 
                                 callback_on_new_best=stop_callback,
                                 eval_freq=100000,
                                 best_model_save_path=callback_save,
                                 verbose=1)

    model.learn(total_timesteps=10**6, callback=eval_callback)
    model.save(final_save)
    env.close()

def RL_EVAL(game, ppo_path): #NOT VERY HELPFUL FUNCTION
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

def RL_MODEL_TEST(game, episodes, model_path):
    print(f"BEST_MODEL_PATH: {model_path}")
    env = gym.make(game, render_mode="human")
    model = PPO.load(model_path, env=env)
    for episode in range(0, episodes):
        observation, _ = env.reset()
        done = False
        truncated = False
        score = 0

        while not done and not truncated :
            env.render()
            action, _ = model.predict(observation)
            observation, reward, done, truncated, info = env.step(action)
            score = score + reward
            #print(score, done, truncated)

        print(f"Episode: {episode}, Score: {score}")
    env.close()

def main():
    game = "ALE/Breakout-v5"#"CartPole-v1"#"ALE/Breakout-v5"
    policy = "CnnPolicy"
    model_name = "ppo_breakout_cnnpolicy"
    log_path = os.path.join("runs", "train")
    

    #RL_TRAIN(game, policy, log_path, model_name)
    #RL_EVAL(game, model_save_path)
    #RL_RANDOM_PLAY(game, 5)
    #RL_MODEL_TEST(game, 5, FIND_LATEST_MODEL(log_path, model_name))#os.path.join(log_path, "ppo_cartwheel_mlp_0"))

main()