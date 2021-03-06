import gym
import random

envName = 'CartPole-v1'
env = gym.make(envName)

env.reset()

print(env.observation_space.shape)
print(env.action_space)

class Agent():

	def __init__(self, env):
		self.action_size = env.action_space.n
		print(self.action_size)

	def get_action(self, state):
		action = random.choice(range(self.action_size))
		poleAngle = state[2]

		action = 0 if poleAngle < 0 else 1

		return action

agent = Agent(env)
state = env.reset()

for _ in range(1000):

	action = agent.get_action(state)
	state, reward, done, info = env.step(action)
	env.render()