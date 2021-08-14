# valueIterationAgents.py
# -----------------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).
import np as np

import mdp, util

from learningAgents import ValueEstimationAgent

class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState)
              mdp.isTerminal(state)
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter() # A Counter is a dict with default 0
        vplus = util.Counter()
        # Write value iteration code here
        "*** YOUR CODE HERE ***"

        states = mdp.getStates()

        self.policy={}

        it = 0
        self.policy = {}
        for s in states:
            if not mdp.isTerminal(s):
                self.policy[s]=np.random.choice(mdp.getPossibleActions(s))
        while it < self.iterations:
            it+=1
            for s in states:
                val = 0
                reward = 0
                ok = 0
                for a in mdp.getPossibleActions(s):
                    sum = 0
                    for i in mdp.getTransitionStatesAndProbs(s,a):
                        sum += i[1]*(self.values[i[0]])
                    if ok == 0:
                        val = sum
                        ok = 1
                    if val <= sum:
                        val = sum
                        reward = mdp.getReward(s, a, a)
                        self.policy[s]=a
                vplus[s]=val*self.discount+reward

            for s in states:
                self.values[s] = vplus[s]









    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]


    def computeQValueFromValues(self, state, action):
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """
        "*** YOUR CODE HERE ***"
     #  sum = 0
      #  for s in self.mdp.getStates():
       #     if action in self.mdp.getPossibleActions(s):
        #        for i in self.mdp.getTransitionStatesAndProbs(s,action):
         #           sum+=i[1]*self.values[i[0]]
        #return self.mdp.getReward(state,action,action) +sum*self.discount
        sum = 0
        for i in self.mdp.getTransitionStatesAndProbs(state, action):
            sum += i[1] * (self.values[i[0]])
        return self.mdp.getReward(state,action,action) + self.discount*sum
        util.raiseNotDefined()

    def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """
        "*** YOUR CODE HERE ***"
        if self.mdp.isTerminal(state):
            return None
        return self.policy[state]
        util.raiseNotDefined()

    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)
