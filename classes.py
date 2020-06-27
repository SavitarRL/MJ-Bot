###########
## Classes
###########


class Tile:
    """ 
    Attributes:
    
    Methods:
    """

    def __init__(self, type, value):
        """
        Parameters:
        -------------
        type : str
            stick, circle, million, words

        value: int
            normal: 1-9
            words: 1:east, 2:south, 3:west, 4:north, 5:middle, 6:fat, 7:white
        """

        super().__init__() #inherit
        if type not in ["stick", "circle", "million", "words"]:
            raise Exception("No such Mahjong type, got {}".format(self.type))
        self.type = type
        self.value = value
        self.word_dict = {1:"east", 2:"south", 3: "west", 4: "north", 5:"middle", 6:"fat",7: "white"}
        if type != "words":
            if value >9 or value <1:
                raise Exception("Value not in range")
        else:
            if value >7 or value <1:
                raise Exception("Value not in range")


    def __str__(self):
        if self.type == "words":
            return self.word_dict[self.value]
        else:
            return "{} {}".format(self.value, self.type)

    
    def isDirection(self):
        if self.type == "words":
            if self.value < 5:
                return True  
        return False
    
    
    def __eq__(self, other):
        if self.type == other.type and self.value == other.value:
            return True
        else:
            return False



