import pygame
from pygame.sprite import Group
pygame.init()


pygame.display.set_caption("rocket in space by stefan")
WIDTH = 700
HEIGHT = 500
screen = pygame.display.set_mode([WIDTH,HEIGHT])
class Player (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("rocket in space/spaceship.png")
        self.image = pygame.transform.scale(self.image,(70,100))
        self.rect = self.image.get_rect()

sprites = pygame.sprite.Group()
def start_game ():
    ship = Player()
    sprites.add(ship)
    while True:
        for i in pygame.event.get():
            if i .type == pygame.QUIT:
                pygame.quit()
        screen.blit(pygame.image.load("rocket in space/spacebg.png"),(0,0))
        sprites.draw(screen)
        pygame.display.update()

start_game()
 