import os
from stable_baselines3 import PPO
from matrix import MatrixEnv

env = MatrixEnv()

model_path = os.path.join('Training', 'models')
model = PPO.load(model_path, env=env)

obs = env.reset()
env.render('human', "Initial state")

for _ in range(20):  # Adjust the number of steps for testing
    action, _ = model.predict(obs)
    obs, _, done, _ = env.step(action)
    env.render('human')
      # Optional: visualize the agent's actions