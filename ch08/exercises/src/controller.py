import pygame

from src import graph

class Controller:

    def __init__(self):

        """ initializes the models and any other data needed """
        pygame.init()
        self.display = pygame.display.set_mode()
        self.graph = graph.Graph(self.display.getWidth(), self.display.getHeight())
        self.drawing = False
