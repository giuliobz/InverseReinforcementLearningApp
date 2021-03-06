import os
import sys
import cv2
import time
import numpy as np

from Utility.utility import read_csv_grids


# count for how much frames are equal in the clip
def no_move_count(grid):
    counts = np.zeros(len(grid))

    for i in range(len(grid)):
        for j in range(i, len(grid)):
            if np.array_equal(grid[i], grid[j]):
                counts[i] += 1

    return int(max(counts))


# If in the clip the agent is in a state where the oracle matrix is 0
# we assign 0 reward to the entire clip, in essence we discard that.
def count_reward(grid, matrix):
    x_old, y_old = 1, 1
    reward = 0

    for i in range(len(grid)):
        x, y = np.where(grid[i] == 10)
        if (not x[0] < x_old) and (not y[0] < y_old) and (not matrix[x, y][0] == 0):
            reward += matrix[x, y][0]
            x_old = x[0]
            y_old = y[0]
        else:
            reward = 0
            return reward

    return reward


# Compute the clip reward, it is useful in dense Oracle more than Sparse one.
def give_pref(reward_1, reward_2):
    preference = None

    if reward_1 > 1.5 and reward_2 > 1.5:
        preference = [0.5, 0.5]

    elif reward_1 > 1.5:
        preference = [1, 0]

    elif reward_2 > 1.5:
        preference = [0, 1]

    else:
        preference = [0, 0]

    return preference


# Define the artificial annotator, the Oracle.
# We adopted two kind of Oracle: sparse and dense modalities.
def createOracleMatrix(wrapper, env, dense=False):
    # Define the wrapper and initialize an image to create
    # the oracle predefined reward matrix
    img = wrapper.observation(env.reset())

    # Create a sizexsize matrix of zero
    oracle_rewards = np.zeros((img.shape[0], img.shape[1]))

    # Define the path that the agent must learn to do
    oracle_rewards[1:-1, 1] = 1
    oracle_rewards[-2, 1:-1] = 1

    # Define the reward for each position in the grid
    ind8 = np.where(img == 8)
    oracle_rewards[ind8[0], ind8[1]] = 10

    if dense:
        for col in range(2, len(oracle_rewards) // 2):
            for row in range(2, len(oracle_rewards) - 1):
                if oracle_rewards[row][col] == 0:
                    m = max(list(oracle_rewards[row - 1:row + 2, col - 1:col + 1].flatten()))
                    if m == 10:
                        m = 1
                    elif m <= 0.1:
                        m = 0
                    oracle_rewards[row][col] = m / 2

        for row in range(len(oracle_rewards) - 2, 1, -1):
            for col in range(1, len(oracle_rewards) - 2):
                if oracle_rewards[row][col] == 0:
                    m = max(list(oracle_rewards[row - 1:row + 2, col - 1:col + 1].flatten()))
                    if m == 10:
                        m = 1
                    elif m <= 0.1:
                        m = 0
                    oracle_rewards[row][col] = m / 2

    return oracle_rewards


class Oracle:
    def __init__(self, wrapper, env, model):

        # Define matrix oracle reward
        self._matrix = createOracleMatrix(wrapper, env)

        self._model = model

    # Function to give preference to a pair of clips. The following are handcrafted rules. 
    def takeReward(self, data_path, clip_1, clip_2, env):

        file_1 = [file_ for file_ in os.listdir(data_path + '/' + clip_1['path']) if 'grid_' in file_]
        file_2 = [file_ for file_ in os.listdir(data_path + '/' + clip_2['path']) if 'grid_' in file_]

        states_1 = read_csv_grids(data_path + '/' + clip_1['path'] + '/' + file_1[0], env)
        states_2 = read_csv_grids(data_path + '/' + clip_2['path'] + '/' + file_2[0], env)

        # number of agent states without any moves
        # if it is greater than 3 we discard the clip
        count_1 = no_move_count(states_1)
        count_2 = no_move_count(states_2)

        reward_1 = count_reward(states_1, self._matrix)
        reward_2 = count_reward(states_2, self._matrix)
        preference = None

        # In the two clips the agent mooves at least twice
        if count_1 <= 3 and count_2 <= 3:
            preference = give_pref(reward_1, reward_2)

        # In one clips make at least 3 moves and in the another clips no
        elif count_1 <= 3:
            preference = give_pref(reward_1, 0)

        # In one clips make at least 3 moves and in the another clips no
        elif count_2 <= 3:
            preference = give_pref(0, reward_2)

        if preference == None:
            preference = [0, 0]

        if self._model != None:

            if preference == [1, 0]:
                self._model.logBarDxSignal.emit('Oracle decision : prefer left clip')

            elif preference == [0, 1]:
                self._model.logBarDxSignal.emit('Oracle decision : prefer right clip')

            elif preference == [0.5, 0.5]:
                self._model.logBarDxSignal.emit('Oracle decision : prefer both clips')

            else:
                self._model.logBarDxSignal.emit('Oracle decision : discard clips')

        return preference
