class Player:
    
  def __init__(self, pnum=1):
    """
    Initialize the player object
    args: pnum [int] the player's id number
    """
    self.player_num = pnum
    self.lives = 3 # players always start with 3 lives
    self.is_large = False # player always starts small

class Enemy:

    def __init__(self, health, damage, speed, range):
        """ initializes the enemy
        """
        self.health = health #health of the enemy
        self.damage = damage #damage done by the enemy
        self.speed = speed #speed of the enemy
        self.range = range #range of the enemy

class Pipe:

    def __init__(self, height, positon):
        """ initializes the pipes
        args: height [int] takes in the height of the pipes
        """
        self.height = height #height of the pipe
        self.position = position #position of the pipe
        self.is_open = False #cannot enter pipe

class Block:
#can be used for the bricks or the ground

    def __init__(self, height):
        """ initializes the blocks
        args: height [int] takes in the height of the blocks
        """
        self.height = height #height of the block
        self.can_break = True #can break the block

#class Powerup(Block):
#inherits from the block class

class Text:

    def __init__(self, font, size, position, color, message):
        """ initializes the text
        args: font [str] the font of the text
                size [int] the size of the text
                position [tuple] the position of the text
                color [tuple] the color of the text
                message [str] the message of the text
        """
        self.font = font #font of the text
        self.size = size #size of the text
        self.position = position #position of the text
        self.color = color #color of the text
        self.message = message #message of the text

