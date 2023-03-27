#model is about how the class is used

import random
import pygame

class Point:
    """ 
    docstring for Point class
    """
    # functions are called methods when they are in a class
    # first paramater to any method is always 'self'
    def __init__(self, x = 0, y = 0, color = "red"):
        #self ties the data to the object scope
        self.xcoor = abs(x)
        self.ycoor = y
        self.color = color

    # no return

    def random_color(self):
        new_color = ["red", "green", "blue", "yellow", "orange", "purple", "pink", "black", "white"]
        self.color = random.choice(new_color)

class LED:
    """
    lalala
    """

    def __init__(self, x = 0, y = 0, color = "red"):
        self.on = True
        self.rect = pygame.Rect(abs(x), abs(y), 20, 20)
        self.color = color
        self.radius = 10

    def the_random_color(self):
        new_color = ["red", "green", "blue", "yellow", "orange", "purple", "pink", "black", "white"]
        self.color = random.choice(new_color)

    def to_draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.xcoor, self.ycoor), 10)

