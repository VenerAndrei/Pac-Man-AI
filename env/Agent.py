import random, math
from Player import *
from Features import *


class QLearningAgent(Player):

    def __init__(self, x, y, grid, screen, ghosts, coin_grid):
        Player.__init__(self, x, y, grid, screen, ghosts, coin_grid)
        self.qval = {}
        self.epsilon = 0.05
        self.discount = 0.8
        self.alpha = 0.2

    def getLegalActions(self, state):

        actions = []
        cols = len(self.grid[0])
        rows = len(self.grid)

        if state[0] > 0:
            if self.grid[state[1]][state[0] - 1] == 1:
                actions.append("west")
        if state[0] < cols:
            if self.grid[state[1]][state[0] + 1] == 1:
                actions.append("east")
        if state[1] > 0:
            if self.grid[state[1] - 1][state[0]] == 1:
                actions.append("north")
        if state[1] < rows:
            if self.grid[state[1] + 1][state[0]] == 1:
                actions.append("south")

        return actions

    def getQValue(self, state, action):
        """
          Returns Q(state,action)
        """
        if (state, action) in self.qval:
            return self.qval[state, action]
        else:
            self.qval[state, action] = 0.0
            return 0.0

    def computeValueFromQValues(self, state):
        """
          Returns max_action Q(state,action)
        """
        ok = 0
        val = 0
        for a in self.getLegalActions(state):
            if not ok:
                ok = 1
                val = self.getQValue(state, a)
            if val <= self.getQValue(state, a):
                val = self.getQValue(state, a)
        return val

    def computeActionFromQValues(self, state):
        """
          Compute the best action to take in a state.
        """

        if not self.getLegalActions(state):
            return None
        ok = 0
        val = 0
        act = None
        for a in self.getLegalActions(state):
            if not ok:
                ok = 1
                val = self.getQValue(state, a)
            if val <= self.getQValue(state, a):
                act = a
                val = self.getQValue(state, a)
        return act

    def getAction(self, state):
        """
          Compute the action to take in the current state.
        """
        legalActions = self.getLegalActions(state)
        action = None
        prob = random.random()

        if prob < self.epsilon:
            return random.choice(legalActions)
        elif legalActions:
            return self.computeActionFromQValues(state)
        return action

    def update(self, state, action, nextState, reward):
        sum = 0
        ok = 0
        if not (nextState, action) in self.qval:
            self.qval[nextState, action] = 0.0
        for a in self.getLegalActions(nextState):
            if (nextState, a) not in self.qval:
                self.qval[nextState, a] = 0.0
            if not ok:
                ok = 1
                sum = self.qval[nextState, a]
            if self.qval[nextState, a] >= sum:
                sum = self.qval[nextState, a]

        if (state, action) not in self.qval:
            self.qval[state, action] = 0.0

        self.qval[state, action] = self.qval[state, action] * (1 - self.alpha) + self.alpha * (
                    reward + self.discount * sum)
        return self.qval[state, action]

    def getPolicy(self, state):
        return self.computeActionFromQValues(state)

    def getValue(self, state):
        return self.computeValueFromQValues(state)


class PacmanQAgent(QLearningAgent):
    "Exactly the same as QLearningAgent, but with different default parameters"

    def __init__(self, x, y, grid, screen, ghosts, coin_grid):
        self.index = 0  # This is always Pacman
        QLearningAgent.__init__(self, x, y, grid, screen, ghosts, coin_grid)

    def getAction(self, state):
        action = QLearningAgent.getAction(self, state)
        return action


class ApproximateQAgent(PacmanQAgent):

    def __init__(self, x, y, grid, screen, ghosts, coin_grid):
        self.featExtractor = SimpleExtractor()
        PacmanQAgent.__init__(self, x, y, grid, screen, ghosts, coin_grid)
        self.weights = {}

    def getWeights(self):
        return self.weights

    def getQValue(self, state, action):
        """
           return Q(state,action) = w * featureVector
        """
        sum = 0.0

        for f in self.featExtractor.getFeatures(state, action, self.ghosts, self.coin_grid, self.grid):
            if f not in self.weights:
                self.weights[f] = 0
            sum += self.featExtractor.getFeatures(state, action, self.ghosts, self.coin_grid, self.grid).get(f) * \
                   self.weights[f]

        self.qval[state, action] = sum
        return sum

    def update(self, state, action, nextState, reward):
        """
           Should update weights based on transition
        """
        sum = 0
        ok = 0
        for a in self.getLegalActions(nextState):
            if not ok:
                ok = 1
                sum = self.getQValue(nextState, a)
            if self.getQValue(nextState, a) >= sum:
                sum = self.getQValue(nextState, a)

        diff = (reward + self.discount * sum) - self.getQValue(state, action)
        for f in self.featExtractor.getFeatures(state, action, self.ghosts, self.coin_grid, self.grid):
            self.weights[f] = self.weights[f] + self.alpha * diff * self.featExtractor.getFeatures(state, action,
                                                                                                   self.ghosts,
                                                                                                   self.coin_grid,
                                                                                                   self.grid).get(f)
        return self.weights
