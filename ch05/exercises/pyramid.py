num = int(input("number of stars"))

def star_pyramid():
    number = num
    star = 0
    while number > 0:
        while star <= number:
            print("*")
            star += 1
        print("\n")
        number -= 1

star_pyramid()
