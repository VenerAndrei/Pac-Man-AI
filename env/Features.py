
from Agent import *

class IdentityExtractor():
    def getFeatures(self, state, action):
        feats={}
        feats[(state, action)] = 1.0
        return feats



class SimpleExtractor(ApproximateQAgent):
    def getLegalPos(self,ghost):

        pos = []
        cols = len(self.grid[0])
        rows = len(self.grid)
        state = ghost.get_pos()

        if state[0] > 0:
            if self.grid[state[1]][state[0] - 1] == 1:
                pos.append((state[0]-1,state[1]))
        if state[0] < cols:
            if self.grid[state[1]][state[0] + 1] == 1:
                pos.append((state[0]+1,state[1]))
        if state[1] > 0:
            if self.grid[state[1] - 1][state[0]] == 1:
                pos.append((state[0],state[1]-1))
        if state[1] < rows:
            if self.grid[state[1] + 1][state[0]] == 1:
                pos.append((state[0],state[1]+1))
        return pos
    def dirToVec(self,action):
        if action=="north":
            return 0, -1
        elif action=="south":
            return 0, 1
        elif action == "west":
            return -1, 0
        else :
            return 1, 0
    def getFeatures(self, state, action):
        # extract the grid of food and wall locations and get the ghost locations
        food = state.getFood()
        walls = state.getWalls()
        ghosts = state.getGhostPositions()

        features = {}

        features["bias"] = 1.0

        # compute the location of pacman after he takes the action
        x, y = state
        dx, dy = self.dirToVec(action)
        next_x, next_y = int(x + dx), int(y + dy)

        # count the number of ghosts 1-step away
        features["#-of-ghosts-1-step-away"] = sum(
            (next_x, next_y) in Actions.getLegalNeighbors(g, walls) for g in ghosts)

        # if there is no danger of ghosts then add the food feature
        if not features["#-of-ghosts-1-step-away"] and food[next_x][next_y]:
            features["eats-food"] = 1.0

        dist = closestFood((next_x, next_y), food, walls)
        if dist is not None:
            # make the distance a number less than one otherwise the update
            # will diverge wildly
            features["closest-food"] = float(dist) / (walls.width * walls.height)
        features.divideAll(10.0)
        return features

