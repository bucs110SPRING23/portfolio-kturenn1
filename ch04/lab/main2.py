import pygame
import random
import math

pygame.init()
window = pygame.display.set_mode()
width1 = pygame.display.get_window_size()

window.fill("blue")
pygame.draw.circle(window, "pink", [width1[0]/2, width1[1]/2], width1[1]/2)
pygame.draw.line(window, "black", (0, width1[1]/2), (width1[0], width1[1]/2))
pygame.draw.line(window, "black", (width1[0]/2, 0), (width1[0]/2, width1[1]))


dart = int(10)
while dart > 0:
    
    valuex = random.randrange(0, width1[0]+1)
    valuey = random.randrange(0, width1[1]+1)

    distance_from_center = math.hypot((width1[0]/2)-valuex, (width1[1]/2)-valuey) #the distance formula
    is_in_circle = distance_from_center <= width1[1]/2 #screen width

    if is_in_circle:
        pygame.draw.circle(window, "green", [valuex, valuey], 20)
    else:
        pygame.draw.circle(window, "red", [valuex, valuey], 20)

    dart -= 1
    pygame.display.flip()
    pygame.time.wait(1000)

pygame.display.flip()
pygame.time.wait(3000)

window.exitonclick()