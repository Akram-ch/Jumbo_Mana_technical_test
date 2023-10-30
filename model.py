from matrix import MatrixEnv
import os
from stable_baselines3 import PPO

env = MatrixEnv()
model = PPO("MlpPolicy", env, verbose=1)
# Train the agent
model.learn(total_timesteps=20000)

model_path = os.path.join('Training', 'models')

model.save(model_path)
