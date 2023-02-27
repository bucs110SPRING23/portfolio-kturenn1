import random

number = int(random.randrange(1,11))
count = int(0)

for count in range(3):
    guess = input("Guess a number from 1-10 (inclusive)")
    theguess = int(guess)
    if theguess == number: 
        print("correct!")
        break
    else:
        if theguess < number:
            print("Too Low")
        if theguess > number:
            print("Too High")
    count += 1