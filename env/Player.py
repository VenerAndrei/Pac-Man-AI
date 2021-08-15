import env.Consts as consts
import pygame


class Player:

    def __init__(self, x, y, grid, screen):
        self.x = x
        self.y = y
        self.screen = screen
        self.grid = grid

    def draw(self):
        pygame.draw.circle(self.screen, consts.YELLOW, (
            consts.tile_size * self.x + consts.tile_size / 2, consts.tile_size * self.y + consts.tile_size / 2),
                           (consts.tile_size*1.2) / 2)

    def set_pos(self, x, y):
        if self.grid[y][x] == 1:
            self.x = x
            self.y = y
