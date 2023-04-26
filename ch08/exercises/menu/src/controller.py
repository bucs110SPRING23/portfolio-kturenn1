import pygame
from src.ball import Ball
import pygame_menu

class Controller:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode()
        self.width, self. height = pygame.display.get_window_size()

        self.ball  = Ball(self.width/2, self.height/2, 100)
        self.sprites = pygame.sprite.Group((self.ball,))

        self.state = "START"

    def mainloop():
        while True:
            if self.state == "GAME":
                self.gameloop()
            elif self.state == "END":
                self.endloop()
            elif self.state == "START":
                self.startloop()

    def endloop():
        font_obj = pygame.font.SysFont(None, 48)
        msg = font_obj.render("You Won!", True, (255, 255, 255))

        while self.state == "END":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                self.screen.blit(msg, (50,50))
                pygame.display.flip()

    def startloop(self):
        self.menu = pygame_menu.Menu("Start Screen", self.width/2, self.height/2)
        self.menu.add.label("Click to start", font_size = 30)
        self.menu.add.button("Start", self.startgame, aign = pygame_menu.locals.ALIGN_CENTER)

        while self.state == "START":
            self.main.update(pygame.get.events())
            self.menu.draw(self.screen)
            pygame.display.flip()


    def gameloop(self):
        
        while True:

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.ball.rect.collidepoint(event.pos):
                        pygame.quit()
                        exit()

            self.sprites.update()
            if self.balll.rect.x < 0:
                self.ball.direction = "right"
            elif self.ball.rect.x > (self.width - self.ball.rect.width):
                self.ball.direction = "left"

            
    
    def startgame(self):
        self.state = "GAME"