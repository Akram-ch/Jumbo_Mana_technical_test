# Jumbo Mana technical test

This document details all the steps that I took to attemp to solve the Jumbo Mana technical recruitement test.

## Step 1 : Training
The test requires the use and manipulation of reinforcement learning techniques, which I am not yet familiar with. So I started by watching a YouTube tutorial and creating a small test project to get started.

**video link** : https://www.youtube.com/watch?v=Mut_u40Sqz4&t=895s

These are the notes I took while following the tutorial:
### Notes: 

**How RL works:** Reinforcement learning focuses on teaching agents through trial and error.

**Agent:** the actor operating within the environment, it is usually governed by a policy (a rule that decides which action to take)

**Environment:** the world in which the agent can operate

**Action:** the agent can do something within the environment known as an action

**Reward and observation**: in return, the agent recieves an award and a view of what the environment looks like after acting on it.

The agent takes actions in order to maximize the word recieved from the environment.

![Alt text](be7152_c68c151c0c6d4911907458740125e09d~mv2.png)

#### 1-Setup:
```
pip install stable-baselines3[extra]
```
**Stable baselines documentation:** https://stable-baselines3.readthedocs.io/en/master/

#### 2-Enviroments: Environments can be eiter real or simulated. Simulated environments give you the ability to trial and train a model in a safe and cost effective model.

**OpenAI Gym** : provides an easy way to build environments for rl agents.

#### Cartpole environment: 
```python
environment_name = "CartPole-v0"
env = gym.make(environment_name, render_mode="human")
episodes = 5
for episode in range(1, episodes+1):
    state = env.reset()
    done = False
    truncated = False
    score = 0 
    
    while not done:
        env.render()
        action = env.action_space.sample()
        n_state, reward, done, truncated, info = env.step(action)
        score+=reward
    print('Episode:{} Score:{}'.format(episode, score))
env.close()
```

Here I loaded the premade cartpole environment from OpenAI gym.

The model goes through 5 iterations (episodes)

in the beginning of each episode, the environment is reset to its default values, and the model takes a random action from the action space (in this case 0 or 1) and the score is calculated for each episode

* **Action space**: The action is a ndarray with shape (1,) which can take values {0, 1} indicating the direction of the fixed force the cart is pushed with
* **Observation space** : The observation is a ndarray with shape (4,) with the values corresponding to the following positions and velocities (cart position, cart velocity, pole angle, pole angular velocity)









## Step 2: Creating custom environment
For this step I am creating the custom matrix environment in which my agent will operate.