code = input("Give code \n")
money = int(input("Please pay \n"))

def myVendingMachine():
    if code == "A":
        if money >= 1:
            print("Here coke")
        else:
            print("ur broke")

    elif code == "B":
        if money >= 2:
            print("Here sprite")
        else:
            print("ur broke")
            
    elif code == "C":
        if money >= 3:
            print("Here fanta")
        else:
            print("ur broke")

    else:
        print("no code no bev")

def findMax(x, y, z):
    max = x
    if y > max:
        max = y
    if z > max:
        max = z
    
    print(max)

for _ in range(3):
    print("Enter 3 numbers:")
    a = int(input(": "))
    b = int(input(": "))
    c = int(input(": "))
    findMax(a, b, c)