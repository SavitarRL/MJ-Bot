import random


###########
## Classes
###########


class Game:
    def __init__(self):
        self.players = [Player("E"),Player("S"),Player("W"),Player("N")]
        self.played_tiles = {} ## dict or list???
        self.drawable_tiles = {}
        ## can add more stuff
    
    def reset(self):
        ## empty player_tiles, put all into drawable, shuffle
        pass

    def pick_tile(self):
        ## returns a random/top tile from derawable
        ## use this in deal
        pass

    def deal(self):
        ## deals tiles to 4 players
        pass
    
    
    def __str__(self):
        bigstring = ""
        for player in self.players:
            bigstring += str(player)
            bigstring += "\n"
        return bigstring





class Player:
    def __init__(self,wind):
        self.hand = Hand()
        self.wind = wind

        
    def draw(self):
        # should add to self.hand
        pass

    def discard(self):
        # should remove from self.hand
        pass
    
    def __str__(self):
        return self.wind + "\n" + str(self.hand)



class Hand:
    def __init__(self):
        self.tiles = []

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
            tile_string += "{:^5}|".format(str(tile))
            count+=1
        return idx_string + "\n" + tile_string
    







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
            return "{}{}".format(self.value, self.type[0])


    
