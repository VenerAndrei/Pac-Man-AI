import pygame
import env.Consts as consts


class Ghost:

    def __init__(self, screen, x, y, grid):
        self.screen = screen
        self.x = x
        self.y = y
        self.grid = grid
        self.ghost_sprite = pygame.image.load("../images/ghost.png")
        self.ghost_sprite = pygame.transform.scale(self.ghost_sprite, (consts.tile_size+consts.tile_size//2, consts.tile_size+consts.tile_size//2))
        print(consts.tile_size//2)
    def draw(self):
        #pygame.draw.rect(self.screen,consts.RED,pygame.Rect((self.x * consts.tile_size + 2,self.y * consts.tile_size + 2),(consts.tile_size- 2,consts.tile_size-2)))
        self.screen.blit(self.ghost_sprite,(self.x*consts.tile_size-4,self.y*consts.tile_size-4))

    def set_pos(self, x, y):
        if self.grid[y][x] == 1:
            self.x = x
            self.y = y
