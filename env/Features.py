
import env.Consts as consts

class IdentityExtractor():
    def getFeatures(self, state, action):
        feats={}
        feats[(state, action)] = 1.0
        return feats

def dirToVec(action):
    if action == "north":
        return 0, -1
    elif action == "south":
        return 0, 1
    elif action == "west":
        return -1, 0
    else:
        return 1, 0



def getLegalPos(state,grid):
    pos = []
    cols = len(grid[0])
    rows = len(grid)

    if state[0] > 0:
        if grid[state[1]][state[0] - 1] == 1:
            pos.append((state[0] - 1, state[1]))
    if state[0] < cols:
        if grid[state[1]][state[0] + 1] == 1:
            pos.append((state[0] + 1, state[1]))
    if state[1] > 0:
        if grid[state[1] - 1][state[0]] == 1:
            pos.append((state[0], state[1] - 1))
    if state[1] < rows:
        if grid[state[1] + 1][state[0]] == 1:
            pos.append((state[0], state[1] + 1))
    return pos


def closestFood(pos,coin_grid,grid):
    """
    closestFood -- this is similar to the function that we have
    worked on in the search project; here its all in one place
    """
    fringe = [(pos[0], pos[1], 0)]
    expanded = set()
    while fringe:
        pos_x, pos_y, dist = fringe.pop(0)
        if (pos_x, pos_y) in expanded:
            continue
        expanded.add((pos_x, pos_y))
        # if we find a food at this location then exit
        if coin_grid[pos_y][pos_x]==1:
            return dist
        # otherwise spread out from the location to its neighbours
        nbrs = getLegalPos((pos_x, pos_y),grid)
        for nbr_x, nbr_y in nbrs:
            fringe.append((nbr_x, nbr_y, dist+1))
    # no food found
    return None

class SimpleExtractor():



    def getFeatures(self, state, action,ghosts, coin_grid,grid):
        # extract the grid of food and wall locations and get the ghost locations


        features = {}

        features["bias"] = 1.0

        # compute the location of pacman after he takes the action
        x, y = state
        dx, dy = dirToVec(action)
        next_x, next_y = int(x + dx), int(y + dy)

        # count the number of ghosts 1-step away
        features["#-of-ghosts-1-step-away"] = 0

        for g in ghosts:
            if (next_x,next_y) in getLegalPos(g.get_pos(),grid):
                features["#-of-ghosts-1-step-away"]+=1

        for g in ghosts:
            if (x,y) in getLegalPos(g.get_pos(),grid):
                features["#-of-ghosts-1-step-away"]+=1



        # if there is no danger of ghosts then add the food feature
        if features["#-of-ghosts-1-step-away"]==0 and coin_grid[next_y][next_x]==1:
            features["eats-food"] = 1.0

        dist = closestFood((next_x, next_y),coin_grid,grid)

        if dist is not None:
            # make the distance a number less than one otherwise the update
            # will diverge wildly
            features["closest-food"] = float(dist)/(consts.tile_size*consts.tile_size*consts.tile_size*consts.tile_size)
        for f in features:
            features[f] = features[f]/10
        return features

