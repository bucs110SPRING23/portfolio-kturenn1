import pygame

pygame.init()

def threenp1(n):
    while n > 1.0:
       if n % 2 == 0:
        n = int(n / 2)
       else:
        n = int(3 * n + 1)
    return None

def other(n):
    count = 0
    while n > 1.0:
        if n % 2 == 0:
            n = int(n/2)
            count += 1
        else:
            n = int(3 * n + 1)
            count += 1
    return count

def threenp1range(upper_limit):
    objs_in_sequence = {}
    for iters in range(2, (upper_limit + 1)):
        x = other(upper_limit)
        objs_in_sequence.update({x: iters})
        iters += 1

    return objs_in_sequence

def main():
    x = int(input("Number: "))
    threenp1range(x)

main()