import turtle

# use dot operator for a method
# use parentheses for a function

class Num:

    def __init___(self, n):
        self.data = n
        self.x = "string"

    #dunder (a double underscore)
    #never call this method directly
    #python uses this method

    #requirement: return a string
    #requirement: only self as a parameter
    def __str__(self):
        obj_str = f"The number is: {self.data}"
        return obj_str

    def __add__(self, num):
        self.data = self.data + num

    def addone(self):
        self.data += 1

def main():
    n = Num(5)
    n.addone()
    print(n.data)

    nw = Num(10)
    print(nw)