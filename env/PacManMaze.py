import pygame
from env.Ghost import *
from env.Player import Player
from utils.Graph import *
#FONT
pygame.font.init() # you have to call this at the start,
                   # if you want to use this module.
font = pygame.font.SysFont('consolas', 20)
# SCREEN SIZES
tile_size = 16
width = 28 * tile_size
height = 31 * tile_size
screen = pygame.display.set_mode((width + 400, height))
cols, rows = (28, 31)
grid = [[0 for i in range(cols)] for j in range(rows)]

pygame.init()
done = False
# MAP
FPS = 30  # frames per second setting
fpsClock = pygame.time.Clock()

# COLORS
WHITE = (255, 255, 255)
GRAY = (255 // 2, 255 // 2, 255 // 2)
BLACK = (0, 0, 0)

print(grid)
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

sum = 0


# print("Avem : {}\n".format(get_number_of_nodes_from_grid(grid)))


def draw_map(screen, grid):
    for k in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            # if grid[k][j] == 1:
            #     pygame.draw.rect(screen, GRAY, pygame.Rect(j * tile_size, k * tile_size, tile_size, tile_size))
            if grid[k][j] == 2:
                pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(j * tile_size, k * tile_size, tile_size, tile_size))
            if grid[k][j] == 3:
                pygame.draw.rect(screen, (255, 255, 0), pygame.Rect(j * tile_size, k * tile_size, tile_size, tile_size))

    return


def draw_line(at, to, grid):
    print(to, at)
    if at[0] == to[0]:
        if at[1] - to[1] > 0:
            for x in range(to[1], at[1] + 1):
                grid[x][at[0]] = 1
            return

        for x in range(at[1], to[1] + 1):
            grid[x][at[0]] = 1
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

player = Player(1, 1, grid, screen)
ghost_1 = Ghost(screen, 1, 1, grid)

dfs(graph, 0, node_grid)
print(pick_next_node(graph, 0))
parent = dijkstra(graph,65)
print_path(parent,0,65)
print(pygame.font.get_fonts())
#ghost_1.head_to_node(pick_next_node(graph, 0), graph)
path = create_path(parent,0,65)
ghost_1.head_to_node(path.pop(-1), graph)

while not done:
    textsurface = font.render("Heading to x:{:2d} y:{:2d} id:{:2d}".format(ghost_1.heading_x, ghost_1.heading_y,ghost_1.heading), False, (255, 255, 255))
    screen.fill(BLACK)
    screen.blit(sprites, (0, 0), (0, tile_size * 3, width, height))

    #draw_map(screen, node_grid)
    # for k in range(0, 28):
    #     pygame.draw.line(screen, GRAY, (k * tile_size, 0), (k * tile_size, height))
    # for k in range(0, 31):
    #     pygame.draw.line(screen, GRAY, (0, k * tile_size), (width, k * tile_size))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if mouseCounter % 2 == 0:
                res = pygame.mouse.get_pos()
                at = res
                print("Pressed at {} , {}\t that is at {},{}\n".format(res[0], res[1], res[0] // tile_size,
                                                                       res[1] // tile_size))
            if mouseCounter % 2 == 1:
                res = pygame.mouse.get_pos()
                to = res
                print("Pressed at {} , {}\t that is at {},{}\n".format(res[0], res[1], res[0] // tile_size,
                                                                       res[1] // tile_size))
                draw_line([at[0] // tile_size, at[1] // tile_size],
                          [to[0] // tile_size, to[1] // tile_size],
                          grid)
                print("Line Draw")
            mouseCounter += 1
        if event.type == pygame.KEYDOWN:
            pressed = pygame.key.get_pressed()

            if pressed[pygame.K_a]:
                print("A")
                player.set_pos(player.x - 1, player.y)
            if pressed[pygame.K_d]:
                print("D")
                player.set_pos(player.x + 1, player.y)

            if pressed[pygame.K_w]:
                print("W")
                player.set_pos(player.x, player.y - 1)

            if pressed[pygame.K_s]:
                print("S")
                player.set_pos(player.x, player.y + 1)

    player.draw()
    # if ghost_1.check_delay():
    #     hasArrived = ghost_1.run(graph)
    #     if hasArrived:
    #         ghost_1.head_to_node(pick_next_node(graph, ghost_1.heading), graph)
    if ghost_1.check_delay():
        hasArrived = ghost_1.run(graph)
        if hasArrived and len(path):
            ghost_1.head_to_node(path.pop(-1), graph)
    ghost_1.draw()
    # print(pygame.mouse.get_pressed(1))
    screen.blit(textsurface,(width+20,20))
    pygame.display.flip()
    fpsClock.tick(60)
for x in graph.dTable:
    print(x)
