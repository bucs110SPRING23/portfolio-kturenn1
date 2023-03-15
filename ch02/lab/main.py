import pygame
import math

pygame.init()
window = pygame.display.set_mode()

points = []
xpos = int(0)
ypos = int(0)
side_length = int(50)
num_length = int(3)

for tri in range(num_length):
    angle = 360/3
    radians = math.radians(angle * tri)
    x = xpos + side_length * math.cos(radians)
    y = ypos + side_length * math.sin(radians)
    points = [x,y]

pygame.draw.polygon(window, "red", points)
pygame.display.flip()
pygame.time.wait(3000)