import env.Consts as consts
import pygame


class Player:

    def __init__(self, x, y, grid, screen,ghosts,coin_grid):
        self.x = x
        self.y = y
        self.screen = screen
        self.grid = grid
        self.ghosts=ghosts
        self.coin_grid = coin_grid

    def draw(self):
        pygame.draw.circle(self.screen, consts.YELLOW, (
            consts.tile_size * self.x + consts.tile_size / 2, consts.tile_size * self.y + consts.tile_size / 2),
                           (consts.tile_size*1.2) / 2)

    def set_pos(self, x, y):
        if self.grid[y][x] == 1:
            self.x = x
            self.y = y

    def get_pos(self):
        return self.x , self.y

    def take_action(self, action):
        if action=="north":
            self.set_pos(self.x, self.y - 1)
        elif action=="south":
            self.set_pos(self.x, self.y + 1)
        elif action == "west":
            self.set_pos(self.x - 1, self.y)
        else :
            self.set_pos(self.x + 1, self.y)
        return self.get_pos()


