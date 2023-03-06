num = int(input("number of stars"))

def star_pyramid():
    number = num
    star = 0

    while number > 0:
        while star <= number:
            print(star*'*')
            star += 1
        number -= 1

star_pyramid()

def rstar_pyramid():
    number = num
    star = num

    while number > 0:
        while star >= number:
            print(star*'*')
            star -= 1
        number -= 1

rstar_pyramid()