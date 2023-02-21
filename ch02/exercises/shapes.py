import pygame

pygame.init()
screen = pygame.display.set_mode()

pygame.draw.circle(screen, "red", [500, 500], 50)

pygame.draw.circle(screen, "green", [500, 460], 35)

pygame.draw.circle(screen, "blue", [500, 430], 30)

pygame.display.flip()
pygame.time.wait(4000)