

#from featureExtractors import *

import random,math
from Player import *
from Features import *

class QLearningAgent(Player):

    def __init__(self, x,y,grid,screen):
        Player.__init__(self,x,y,grid,screen)
       # ReinforcementAgent.__init__(self, **args)

        "*** YOUR CODE HERE ***"
        self.qval = {}
        self.epsilon = 0.05
        self.discount = 0.8
        self.alpha = 0.2

    def getLegalActions(self,state):

        actions = []
        cols = len(self.grid[0])
        rows = len(self.grid)

        if state[0] > 0:
            if self.grid[state[1]][state[0]-1] == 1:
                actions.append("west")
        if state[0] < cols:
            if self.grid[state[1]][state[0]+1] == 1:
                actions.append("east")
        if state[1] > 0:
            if self.grid[state[1]-1][state[0]] == 1:
                actions.append("north")
        if state[1] < rows:
            if self.grid[state[1]+1][state[0]] == 1:
                actions.append("south")

        return actions



    def getQValue(self, state, action):
        """
          Returns Q(state,action)
        """
        if (state,action) in self.qval:
            return self.qval[state,action]
        else:
            self.qval[state, action]=0.0
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
                val = self.getQValue(state,a)
            if val <= self.getQValue(state,a):
                val = self.getQValue(state,a)
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
       # print(legalActions)
        action = None
        "*** YOUR CODE HERE ***"
        prob = random.random()
        if prob < self.epsilon:
            return random.choice(legalActions)
        elif legalActions:
            return self.computeActionFromQValues(state)
        return action

    def update(self, state, action, nextState, reward):
        sum = 0
        ok = 0
        if not (nextState,action) in self.qval:
            self.qval[nextState, action]=0.0
        for a in self.getLegalActions(nextState):
            if (nextState, a) not in self.qval:
                self.qval[nextState, a] = 0.0
            if not ok:
                ok = 1
                sum = self.qval[nextState,a]
            if self.qval[nextState,a] >= sum:
                sum = self.qval[nextState,a]

        if (state, action) not in self.qval:
            self.qval[state, action] = 0.0

        self.qval[state,action] = self.qval[state,action] *(1-self.alpha)  + self.alpha *(reward + self.discount* sum)
        return self.qval[state,action]


    def getPolicy(self, state):
        return self.computeActionFromQValues(state)

    def getValue(self, state):
        return self.computeValueFromQValues(state)


class PacmanQAgent(QLearningAgent):
    "Exactly the same as QLearningAgent, but with different default parameters"

    def __init__(self, x,y,grid,screen):
        #args['epsilon'] = epsilon
        #args['gamma'] = gamma
        #args['alpha'] = alpha
        #args['numTraining'] = numTraining
        self.index = 0  # This is always Pacman
        QLearningAgent.__init__(self,x,y,grid,screen)

    def getAction(self, state):
        action = QLearningAgent.getAction(self,state)
        #self.doAction(state,action)
        return action


class ApproximateQAgent(PacmanQAgent):

    def __init__(self, x,y,grid,screen):
        self.featExtractor = IdentityExtractor()
        #self.featExtractor = util.lookup(extractor, globals())()
        PacmanQAgent.__init__(self, x,y,grid,screen)
        self.weights = {}


    def getWeights(self):
        return self.weights

    def getQValue(self, state, action):
        """
           return Q(state,action) = w * featureVector
        """
        sum = 0.0
        i = 0

        for f in self.featExtractor.getFeatures(state,action):
            sum += self.featExtractor.getFeatures(state,action).get(f)* self.weights[f]
            i+=1
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
                sum = self.getQValue(nextState,a)
            if self.getQValue(nextState,a) >= sum:
                sum = self.getQValue(nextState,a)

        i = 0
        #difference

        diff = (reward + self.discount * sum) - self.getQValue(state, action)
        for f in self.featExtractor.getFeatures(state, action):
            self.weights[f] = self.weights[f] + self.alpha * diff * self.featExtractor.getFeatures(state,action).get(f)
            i += 1
        return self.weights


        #    def final(self, state):
        #"Called at the end of each game."
        # call the super-class final method
        #PacmanQAgent.final(self, state)

        # did we finish training?
        #if self.episodesSoFar == self.numTraining:
           #debugging here
         #   pass"""