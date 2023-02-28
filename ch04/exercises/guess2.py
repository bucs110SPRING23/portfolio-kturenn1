import random
import math

number = int(random.randrange(1,1001))
count = int(0)
guess = input("Guess a number from 1-1000 (inclusive)")


while count != (1000 * math.log(2)):
    theguess = int(guess)
    count += 1
    if theguess == number: 
        print("correct! /n")
        print("Guess count:", count)
    else:
        count += 1
        if theguess < number:
            print("Too Low")
        if theguess > number:
            print("Too High")
        guess = input("Guess again")
    
