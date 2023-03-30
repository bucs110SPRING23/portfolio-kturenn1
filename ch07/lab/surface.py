from rectangle import Rectangle

class Surface:

    def __init__(self, filename, x, y, height, width):
        self.image = filename
        self.rect = rectangle.Rectangle(x, y, height, width)

    def getRect(self):
        """
        returns the rectangle object
        """
        return self.rect