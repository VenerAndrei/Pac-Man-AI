import pygame
import env.Consts as consts
import random


def pick_next_node(graph, source):
    near_nodes_idx = []
    for x in range(graph.n_nodes):
        if graph.dTable[source][x] != 0:
            near_nodes_idx.append(x)

    random_next_node = random.choice(near_nodes_idx)
    return random_next_node


class Ghost:

    def __init__(self, screen, x, y, grid):
        self.screen = screen
        self.x = x
        self.y = y
        self.grid = grid
        self.ghost_sprite = pygame.image.load("../images/ghost.png")
        self.ghost_sprite = pygame.transform.scale(self.ghost_sprite, (
            consts.tile_size + consts.tile_size // 2, consts.tile_size + consts.tile_size // 2))
       # print(consts.tile_size // 2)
        self.heading = 0
        self.heading_x = 0
        self.heading_y = 0
        self.depart_time = 0
        self.dir = ""
        self.destination_reached = False

    def draw(self):
        # pygame.draw.rect(self.screen,consts.RED,pygame.Rect((self.x * consts.tile_size + 2,self.y * consts.tile_size + 2),(consts.tile_size- 2,consts.tile_size-2)))
        self.screen.blit(self.ghost_sprite, (self.y * consts.tile_size - 4, self.x * consts.tile_size - 4))

    def set_pos(self, x, y):
        if self.grid[y][x] == 1:
            self.x = x
            self.y = y

    def head_to_node(self, node_idx, graph):

        self.depart_time = pygame.time.get_ticks()
        self.heading = node_idx
        self.heading_x = graph.nodes[self.heading].x
        self.heading_y = graph.nodes[self.heading].y
        if self.heading_x == self.x:
            if self.y - self.heading_y < 0:
                self.dir = "down"
            else:
                self.dir = "up"

        if self.heading_y == self.y:
            if self.x - self.heading_x < 0:
                self.dir = "left"
            else:
                self.dir = "right"

    def run(self, graph):
        # print("At x:{} y:{} heading to x:{} y:{} id:{}".format(self.x,self.y,self.heading_x,self.heading_y,self.heading))
        if self.heading_x == self.x and self.heading_y == self.y:
            # Arrived to destination node
            return True

        if self.dir == "down":
            self.y += 1
        if self.dir == "up":
            self.y -= 1
        if self.dir == "right":
            self.x -= 1
        if self.dir == "left":
            self.x += 1

        return False

    def check_delay(self):
        if pygame.time.get_ticks() - self.depart_time < 50:
            return False

        self.depart_time = pygame.time.get_ticks()
        return True

    def get_pos(self):
        return self.y, self.x


