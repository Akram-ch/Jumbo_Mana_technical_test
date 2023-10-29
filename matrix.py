import gym
import numpy as np
from gym import spaces

#The matrix class inherits the gym.Env class

#The matrix class inherits the gym.Env class

class MatrixEnv(gym.Env):
    def __init__(self):
        super(MatrixEnv, self).__init__()
        
        #Defining the dimensions of the matrix
        self.grid_size = 12
        self.observation_space = spaces.Discrete(self.grid_size**2) 
        self.action_space = spaces.Discrete(4) # Four possible actions
        
        #rewards and penalties
        self.goal_state = (11, 11) #placeholder
        self.goal_reward = 1.0
        self.default_reward = 0.0
        
        #Obstacle locations
        self.obstacles =[
                        (4,1), (2,2), (3,2), (4,2), (2,3), (3,3), (4,3), (3,4), (4,4), #obstacle 1
                        (8,1), (9,1), (7,2), (8,2), (9,2), (7,3), (8,3), (9,3), (7,4), (8,4), (9,4), (10,4), #obstacle 2
                        (2,7), (3,7), (4,7), (2,8), (3,8), (4,8), (2,9), (3,9), (4,9), (2,10), #obstacle 3
                        (7,7), (8,7), (7,8), (8,8), (9,8), (7,9), (8,9), (9,9), (7,10) #obstacle 4
                        ]
        
        self.agent_position = (0, 0) #placeholder
        self.player_position = (0, 0) #placeholder
        
    
    
    def reset(self):
        #Randomly initialize the player's position
        while True:
            random_position = tuple(np.random.randint(0, self.grid_size - 1, size=2))
            if random_position not in self.obstacles:
                self.agent_position = tuple(random_position)
                break
        while True:
            #player can't spawn on the edge to avoid being stuck
            random_position = tuple(np.random.randint(1, self.grid_size - 2, size=2))
            
            #if the AI spawns to the left of the player, the goal is to get to their right
            #if the AI spawns to the right of the player, the goal is to get to their left
                
            if(self.agent_position[0] <= random_position[0]):
                goal = (random_position[0] + 1, random_position [1])

            elif(self.agent_position[0] > random_position[0]):
                goal = (random_position[0] - 1, random_position [1])
                
            if (random_position != self.agent_position) and (random_position not in self.obstacles) and (goal not in self.obstacles):
                self.player_position = tuple(random_position)
                self.goal_state = goal
                break
        
                

            
        #return observation state
        return self.agent_position[0] * self.grid_size + self.agent_position[1]

    
    
    def step(self, action):
        if action == 0:  # Move up
            new_position = (self.agent_position[0] - 1, self.agent_position[1])
        elif action == 1:  # Move down
            new_position = (self.agent_position[0] + 1, self.agent_position[1])
        elif action == 2:  # Move left
            new_position = (self.agent_position[0], self.agent_position[1] - 1)
        elif action == 3:  # Move right
            new_position = (self.agent_position[0], self.agent_position[1] + 1)
        
        # Check if the new position is within the grid and not an obstacle
        if (0 <= new_position[0] < self.grid_size) and (0 <= new_position[1] < self.grid_size) and (new_position not in self.obstacles) and (new_position != self.player_position):
            self.agent_position = new_position
       
        # Determine the reward and check if the agent is behind the player
        
        if (self.agent_position == self.goal_state):
            reward = self.goal_reward
            done = True
        else:
            reward = self.default_reward
            done = False
        
        return self.agent_position[0] * self.grid_size + self.agent_position[1], reward, done, {}
    

    def render(self, mode='human'):
        if mode == 'human':
            self._render_human()
        else:
            super(MatrixEnv, self).render(mode=mode)

    def _render_human(self):
        grid = np.ones((self.grid_size, self.grid_size), dtype=int)

        # Set obstacle cells to black
        for obs in self.obstacles:
            grid[obs[0], obs[1]] = 0

        # Set agent cell to turqouise
        grid[self.agent_position[0], self.agent_position[1]] = 2

        # Set player cell to yellow
        grid[self.player_position[0], self.player_position[1]] = 4

        # Set goal cell to green
        grid[self.goal_state[0], self.goal_state[1]] = 3

        plt.imshow(grid)
        plt.show()
