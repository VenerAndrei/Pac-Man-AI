import pygame
from env.Ghost import *
from utils.Graph import *
from Agent import *

# SCORE
score = 0
# FONT
pygame.font.init()  # you have to call this at the start,
# if you want to use this module.
font = pygame.font.SysFont('consolas', 20)
# SCREEN SIZES
tile_size = 16
width = 28 * tile_size
height = 31 * tile_size
cols, rows = (28, 31)
screen = pygame.display.set_mode((width + 400, height))

done = False
# MAP
FPS = 30  # frames per second setting
fpsClock = pygame.time.Clock()

# COLORS
WHITE = (255, 255, 255)
GRAY = (255 // 2, 255 // 2, 255 // 2)
BLACK = (0, 0, 0)

sprites = pygame.image.load("../images/map.png")
grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

coin_grid = copy_arr(grid)
rewards = copy_arr(grid)

print("AICI")
print(rows, cols)

for i in range(rows):
    for j in range(cols):
        if rewards[i][j] == 1:
            rewards[i][j] = 10
        else:
            rewards[i][j] = -10
copy_rewards = copy_arr(rewards)


def draw_coins(g):
    for y in range(len(g)):
        for x in range(len(g[0])):
            if g[y][x] == 1:
                pygame.draw.circle(screen, WHITE, (x * tile_size + tile_size / 2, y * tile_size + tile_size / 2), 1)


def draw_path(path, ghost_1):
    for x in range(len(path) - 1):
        pygame.draw.line(screen, (225, 255, 0), (graph.nodes[ghost_1.heading].y * tile_size + tile_size / 2,
                                                 graph.nodes[ghost_1.heading].x * tile_size + tile_size / 2), (
                             graph.nodes[path[-1]].y * tile_size + tile_size / 2,
                             graph.nodes[path[-1]].x * tile_size + tile_size / 2)
                         )

        pygame.draw.line(screen, (255, 255, 0), (
            graph.nodes[path[x]].y * tile_size + tile_size / 2, graph.nodes[path[x]].x * tile_size + tile_size / 2), (
                             graph.nodes[path[x + 1]].y * tile_size + tile_size / 2,
                             graph.nodes[path[x + 1]].x * tile_size + tile_size / 2))


def draw_map(screen, grid):
    for k in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            if grid[k][j] == 2:
                pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(j * tile_size, k * tile_size, tile_size, tile_size))
            if grid[k][j] == 3:
                pygame.draw.rect(screen, (255, 255, 0), pygame.Rect(j * tile_size, k * tile_size, tile_size, tile_size))

    return


def draw_line(at, to, mat):
    if at[0] == to[0]:
        if at[1] - to[1] > 0:
            for x in range(to[1], at[1] + 1):
                mat[x][at[0]] = 1
            return

        for x in range(at[1], to[1] + 1):
            mat[x][at[0]] = 1
        return
    elif at[1] == to[1]:

        if at[0] - to[0] > 0:
            for x in range(to[0], at[0] + 1):
                grid[at[1]][x] = 1
            return

        for x in range(at[0], to[0] + 1):
            grid[at[1]][x] = 1
        return


mouseCounter = 0
mouseRes = [0, 0]
at = 0
to = 0

n_nodes, node_grid = get_number_of_nodes_from_grid(grid)
graph = Graph(n_nodes)
graph.make_graph(node_grid)

ghosts = []

player = ApproximateQAgent(1, 1, grid, screen, ghosts, coin_grid)


def create_reset_ghost():
    player.ghosts.clear()
    ghost_1 = Ghost(screen, graph.nodes[22].x, graph.nodes[22].y, grid)
    ghost_1.head_to_node(pick_next_node(graph, 22, ghost_1), graph)
    player.ghosts.append(ghost_1)
    ghost_2 = Ghost(screen, graph.nodes[25].x, graph.nodes[25].y, grid)
    ghost_2.head_to_node(pick_next_node(graph, 25, ghost_2), graph)
    player.ghosts.append(ghost_2)
    ghost_3 = Ghost(screen, graph.nodes[32].x, graph.nodes[32].y, grid)
    ghost_3.head_to_node(pick_next_node(graph, 32, ghost_3), graph)
    player.ghosts.append(ghost_3)
    ghost_4 = Ghost(screen, graph.nodes[33].x, graph.nodes[33].y, grid)
    ghost_4.head_to_node(pick_next_node(graph, 33, ghost_4), graph)
    player.ghosts.append(ghost_4)


create_reset_ghost()

target_grid = copy_arr(grid)


def win_game(coins):
    row = len(coins)
    col = len(coins[0])

    for i in range(row):
        for j in range(col):
            if coins[i][j] == 1:
                return 1
    return 0


def get_reward(eat, game, won_game):
    if won_game == 1:
        return 200
    if game == 1:
        return -350
    if eat:
        return 10
    else:
        return -6


def reset_game(scor, games, won_game):
    player.x = 1
    player.y = 1
    player.coin_grid = copy_arr(grid)
    if won_game:
        print("WIN at ", scor)
    create_reset_ghost()
    return 1, games + 1


while done < 25:
    print("Episode ", done)
    game_over = 0
    score = 0
    state = player.get_pos()
    win = 0

    while not game_over:
        eats = 0
        oldstate = state
        action = player.getAction(state)
        new_state = player.take_action(action)

        for ghost in player.ghosts:
            if ghost.x == player.x and ghost.y == player.y:
                game_over = 1

        if player.coin_grid[player.y][player.x] == 1:
            player.coin_grid[player.y][player.x] = 0
            score += 10
            eats = 1

        if win_game(player.coin_grid) == 0:
            game_over = 1
            win = 1

        for ghost in player.ghosts:
            hasArrived = ghost.run(graph)
            if hasArrived:
                ghost.head_to_node(pick_next_node(graph, ghost.heading, ghost.depart), graph)
                hasArrived = ghost.run(graph)

        for ghost in player.ghosts:
            if ghost.x == player.x and ghost.y == player.y:
                game_over = 1

        reward = get_reward(eats, game_over, win)
        player.update(state, action, new_state, reward)
        state = new_state

        if game_over:
            game_over, done = reset_game(score, done, win)

done = 0
pygame.init()
while done < 200:
    print("Episode ", done)
    game_over = 0
    state = player.get_pos()
    player.alpha = 0
    player.epsilon = 0
    score = 0
    win = 0
    while not game_over:
        eats = 0

        textsurface = font.render(
            "Heading to x:{:2d} y:{:2d} id:{:2d}".format(ghosts[0].heading_x, ghosts[0].heading_y, ghosts[0].heading),
            False,
            (255, 255, 255))
        scoresurface = font.render(
            "Score: {:6d}".format(score), False,
            (255, 255, 255))

        screen.fill(BLACK)
        screen.blit(sprites, (0, 0), (0, tile_size * 3, width, height))
        draw_map(screen, target_grid)
        draw_coins(player.coin_grid)

        oldstate = state
        action = player.getAction(state)
        new_state = player.take_action(action)

        for ghost in player.ghosts:
            if ghost.x == player.x and ghost.y == player.y:
                game_over = 1

        if player.coin_grid[player.y][player.x] == 1:
            player.coin_grid[player.y][player.x] = 0
            score += 10
            eats = 1

        if win_game(player.coin_grid) == 0:
            game_over = 1
            win = 1

        for ghost in player.ghosts:
            hasArrived = ghost.run(graph)
            if hasArrived:
                ghost.head_to_node(pick_next_node(graph, ghost.heading, ghost.depart), graph)
                hasArrived = ghost.run(graph)

        for ghost in player.ghosts:
            ghost.draw()

        player.draw()

        for ghost in player.ghosts:
            if ghost.x == player.x and ghost.y == player.y:
                game_over = 1

        reward = get_reward(eats, game_over, win)

        # for f in player.featExtractor.getFeatures(oldstate, action, player.ghosts, player.coin_grid, player.grid):
        #    print(f, player.featExtractor.getFeatures(oldstate, action, player.ghosts,
        #                                              player.coin_grid, player.grid).get(f),
        #          player.weights[f], reward)

        player.update(oldstate, action, new_state, reward)
        state = new_state

        if game_over:
            game_over, done = reset_game(score, done, win)

        pygame.display.flip()
        screen.blit(textsurface, (width + 20, 20))
        screen.blit(scoresurface, (width + 20, 50))
        fpsClock.tick(FPS)
