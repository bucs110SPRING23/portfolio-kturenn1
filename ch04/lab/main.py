import pygame
import random

pygame.init()
window = pygame.display.set_mode()
width = pygame.display.get_window_size()

window.fill("blue")
pygame.draw.circle(window, "pink", [width[0]/2, width[1]/2], width[1]/2)
pygame.draw.line(window, "black", (0, width[1]/2), (width[0], width[1]/2))
pygame.draw.line(window, "black", (width[0]/2, 0), (width[0]/2, width[1]))


dart = int(10)
while dart > 0:
    
    valuex = random.randrange(0, width[0]+1)
    valuey = random.randrange(0, width[1]+1)
    pygame.draw.circle(window, "green", [valuex, valuey], 20)
    dart -= 1
    pygame.display.flip()
    pygame.time.wait(1000)

pygame.display.flip()
pygame.time.wait(3000)