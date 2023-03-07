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
pointA = 0
pointB = 0

pygame.draw.rect(window, "green", (0, 10, 100, 100))
pygame.draw.rect(window, "red", (101, 110, 100, 100))

font2 = pygame.font.Font(None, 48)
text2 = font.render("Who will win? Click green or red.", True, "white")
window.blit(text2, ((width1[0]/3), (width1[1]/3)))

for event in pygame.event.get():
    while dart > 0:
    
        valuex = random.randrange(0, width1[0]+1)
        valuey = random.randrange(0, width1[1]+1)

        distance_from_center = math.hypot((width1[0]/2)-valuex, (width1[1]/2)-valuey) #the distance formula
        is_in_circle = distance_from_center <= width1[1]/2 #screen width

        if dart % 2 == 0:
            pygame.draw.circle(window, "green", [valuex, valuey], 20)
            if is_in_circle:
                pointA += 1
        else:
            pygame.draw.circle(window, "red", [valuex, valuey], 20)
            if is_in_circle:
                pointB += 1

        dart -= 1
        pygame.display.flip()
        #pygame.time.wait(1000)

if pointA > pointB:
    font = pygame.font.Font(None, 48)
    text = font.render("Player 1 wins!", True, "white")
    window.blit(text, ((width1[0]/3), (width1[1]/3))) # where <x> and<y> are coordinates on screen

elif pointB > pointA:
    font = pygame.font.Font(None, 48)
    text = font.render("Player 2 wins!", True, "white")
    window.blit(text, ((width1[0]/3), (width1[1]/3)))

elif pointA == pointB:
    font = pygame.font.Font(None, 48)
    text = font.render("It is a tie!", True, "white")
    window.blit(text, ((width1[0]/3), (width1[1]/3)))

pygame.display.flip()
pygame.time.wait(3000)
