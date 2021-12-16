import gym
from collections import namedtuple
import numpy as np
import matplotlib.pyplot as plt

import torch
import torch.nn as nn

HIDDEN_SIZE = 128
BATCH_SIZE = 16
PERCENTILE = 70 

class Net(nn.Module):
  def __init__(self, obs_size, hidden_size, n_actions):
    super(Net, self).__init__()
    self.model = nn.Sequential(
        nn.Linear(obs_size, hidden_size),
        nn.ReLU(),
        nn.Linear(hidden_size, hidden_size),
        nn.ReLU(),
        nn.Linear(hidden_size, n_actions),
        nn.Softmax(dim=1)
    )
    
    self.loss_function = nn.CrossEntropyLoss()
    self.optimizer = torch.optim.Adam(self.parameters(), lr=0.01)
  
  def forward(self, input_tensor):
    return self.model(input_tensor)
  
  def train(self, obs_input, acts_v_target):
    action_scores_v = self.forward(obs_input)

    self.optimizer.zero_grad()
    loss_v = self.loss_function(action_scores_v, acts_v_target)  # loss_f(input, target)
    loss_v.backward()
    self.optimizer.step()
    return loss_v
  
Episode = namedtuple("Episode", field_names=["reward", "steps"])                # Store total undiscounted rewards + collections of EpisodeRewads
EpisodeStep = namedtuple("EpisodeStep", field_names=["observation", "action"])  # For one single step in episode and stores obesrvation

count_batch = 0
def iterate_batches(env, net, batch_size, render=False, show_ep=50):
    global count_batch
    batch = []
    episode_reward = 0.0
    episode_steps = []
    obs = env.reset()   # observation
    while True:
        obs_tensor = torch.FloatTensor([obs])
        action_probabilities_v = net.forward(obs_tensor)            # State/Observation is converted through Net to actions
        act_probs = action_probabilities_v.data.numpy()[0]
        action = np.random.choice(len(act_probs), p=act_probs)      # Choose between 0 and 1 action (for exploration)

        next_obs, reward, is_done, _ = env.step(action)
        episode_reward += reward
        episode_steps.append(EpisodeStep(observation=obs, action=action))
        if is_done:
            batch.append(Episode(reward=episode_reward, steps=episode_steps))
            episode_reward = 0.0
            episode_steps = []
            next_obs = env.reset()
            if len(batch) == batch_size:
                count_batch += 1
                yield batch
                batch = []
        obs = next_obs

        if render != False and count_batch % show_ep == 0:
            print(count_batch)
            env.render()


def filter_batch(batch, percentile):
    rewards = list(map(lambda s: s.reward, batch))
    reward_bound = np.percentile(rewards, percentile)
    reward_mean = float(np.mean(rewards))  # only if reward_mean is almost perfect (near 200) program will quit

    train_obs = []
    train_act = []
    for example in batch:
        # Only above certain percentile get pass through and than Net get trained on it
        if example.reward < reward_bound:               
            continue
        # [n, 4] matrix (tensor shape)
        train_obs.extend(map(lambda step: step.observation, example.steps))
        train_act.extend(map(lambda step: step.action, example.steps))

    train_obs_v = torch.FloatTensor(train_obs)
    train_act_v = torch.LongTensor(train_act)
    return train_obs_v, train_act_v, reward_bound, reward_mean


def plot_reward(index, a, b):
    plt.plot(index, a, color="maroon", label="reward bound")
    plt.plot(index, b, color="orangered", label="reward mean")
    plt.legend(loc="best")
    plt.show()

def plot_loss(index, loss):
    plt.plot(index, loss, color="indigo", label="loss")
    plt.title("loss over iteration")
    plt.show()

if __name__ == "__main__":
    env = gym.make("CartPole-v0")
    obs_size = env.observation_space.shape[0]
    n_actions = env.action_space.n

    net = Net(obs_size, HIDDEN_SIZE, n_actions)
    
    iteration_history, loss_history, reward_bound_history, reward_mean_history = [], [], [], []
    plt.style.use("seaborn")

    for iter_index, batch in enumerate(iterate_batches(env, net, BATCH_SIZE, render=True)):
        obs_v, acts_v, reward_bound, reward_mean = filter_batch(batch, PERCENTILE)
        loss_v = net.train(obs_v, acts_v)
        print("%d: loss=%.3f, reward_mean=%.1f, reward_bound=%.1f" % (
            iter_index, loss_v.item(), reward_mean, reward_bound))
        iteration_history.append(iter_index)
        loss_history.append(loss_v)
        reward_bound_history.append(reward_bound)
        reward_mean_history.append(reward_mean)
        if reward_mean > 199:
            print("Solved!")
            plot_reward(iteration_history, reward_bound_history, reward_mean_history)
            plot_loss(iteration_history, loss_history)
            break