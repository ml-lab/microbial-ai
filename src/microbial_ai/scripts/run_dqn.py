import sys
import os
import click
import gym
import numpy as np

sys.path.append(os.getcwd().rsplit('/', 1)[0] + '/utils/')
from dqn import DQNAgent

@click.command()
@click.option('--game', default='CartPole-v1', help='OpenAI gym game')
@click.option('--batch', default=32, help='Batch size of replay training')
@click.option('--iterations', default=1000, help='Number of games the AI plays')
@click.option('--timelimit', default=500, help='Time limit of each iteration')
@click.option('--render', default=False, help='Render training environment')
def main(game, batch, iterations, timelimit, render):
    env = gym.make(game)
    input_size = env.observation_space.shape[0]
    output_size = env.action_space.n
    agent = DQNAgent(input_size, output_size)
    for i in range(iterations):
        state = env.reset()
        state = np.reshape(state, [1, input_size])
        for time in range(timelimit):
            if render:
                env.render()
            action = agent.act(state)
            next_state, reward, done, _ = env.step(action)
            reward = reward if not done else -10
            next_state = np.reshape(next_state, [1, input_size])
            agent.remember(state, action, reward, next_state, done)
            state = next_state
            if done:
                print(f'iteration: {i}/{iterations}, score: {time}')
                break
        if len(agent.memory) > batch:
            agent.replay(batch)

if __name__ == '__main__':
    main()