import pygame

pygame.init()

screen = pygame.display.set_mode()

screen.fill("red")
pygame.display.flip()
pygame.time.wait(1000)

screen.fill("blue")
pygame.display.flip()
pygame.time.wait(1000)

screen.fill("green")
pygame.display.flip()
pygame.time.wait(1000)

screen_size = screen.get_size()

pygame.draw.rect(screen, "pink", [100, 10, 100, 100])
pygame.display.flip()
pygame.time.wait(1000)