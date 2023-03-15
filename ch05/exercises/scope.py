def multiply(x,y):

    """
    Multiplies two numbers without using *
    args: x (int), y (int)
    returns: (int)
    """
    
    accumulator = 0
    for _ in range(y):
        accumulator = accumulator + x
    return accumulator


def exponent(x,y):
    accumulator = 1
    for _ in range(y):
        accumulator = accumulator * x
    return accumulator

def square(x):
    return exponent(x, 2)

def main():
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    print(multiply(x,y))
    print(exponent(x,y))
    print(square(x))

main()

print(multiply.__doc__)