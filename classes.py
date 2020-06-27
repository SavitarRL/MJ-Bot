###########
## Classes
###########


class Hand:
    def __init__(self):
        self.tiles = [Tile("circle",3),Tile("words", 4)]

    def add_tile(self,tile):
        ## add tile to self.tiles
        pass

    def remove_tile(self,idx):
        ## removes tile at idx from self.tiles
        pass

    def num_tiles(self):
        ##return number of tiles in hand
        pass
    def __str__(self):
        idx_string = ""
        tile_string = ""
        count = 0
        for tile in self.tiles:
            idx_string += "  {}  |".format(count)
            tempstring = str(tile).ljust(5, " ")
            tile_string += "{}|".format(tempstring)
        return idxstring + "\n" + tile_string
    







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
            words: 1:east, 2:south, 3:west, 4:north, 5:mid, 6:fat, 7:white
        """

        super().__init__()
        if type not in ["stick", "circle", "million", "words"]:
            raise Exception("No such Mahjong type, got {}".format(self.type))
        self.type = type
        self.value = value
        self.word_dict = {1:"east", 2:"south", 3: "west", 4: "north", 5:"mid", 6:"fat",7: "white"}
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
            return "{} {}".format(self.value, self.type[0])


    
