class Rectangle:

    def __init__(self, x, y, height, width):
        self.x = abs(x)
        self.y = abs(y)
        self.height = abs(height)
        self.width = abs(width)

    def __str__(self):
        """
        returns a string representation of the rectangle
        """
        return "Rectangle at ({self.x}, {self.y}) with height {self.height} and width {self.width}."

    