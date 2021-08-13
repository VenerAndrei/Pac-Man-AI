import pygame

pygame.init()
done = False
#COLORS
WHITE = (255,255,255)
GRAY = (255/2,255/2,255/2)
BLACK = (0, 0, 0)
#SCREEN SIZES
tile_size = 16;
width = 28 * tile_size
height = 31 * tile_size
screen = pygame.display.set_mode((width, height))

sprites = pygame.image.load("../images/map.png")
while not done:
    screen.fill(BLACK)
    screen.blit(sprites,(0,0),(0,tile_size*3,width,height))

    for k in range(0,28):
        pygame.draw.line(screen,GRAY,(k*tile_size,0),(k*tile_size,height))
    for k in range(0, 31):
        pygame.draw.line(screen, GRAY, (0,k*tile_size), (width,k*tile_size))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pygame.display.flip()
