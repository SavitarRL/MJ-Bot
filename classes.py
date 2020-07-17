import random

###########
## Classes
###########


# class Combos:


# class End:


class Game:
    def __init__(self):
        self.players = {"E":Player("E"),"S":Player("S"),"W":Player("W"),"N":Player("N")}
        ## can add more stuff 
        
        ## creating list of total tiles
        self.stick_tiles =[]
        for value in range(1,10):
            for num_stick in range(4):
                self.stick_tiles.append(Tile('s', value))
        self.circle_tiles =[]
        for value in range(1,10):
            for num_circle in range(4):
                self.stick_tiles.append(Tile('c', value))
        self.million_tiles =[]
        for value in range(1,10):
            for num_mil in range(4):
                self.stick_tiles.append(Tile('m', value))
        self.word_tiles =[]
        for value in range(1,8):
            for num_word in range(4):
                self.stick_tiles.append(Tile('w', value))

        self.drawable_tiles = self.stick_tiles + self.circle_tiles + self.million_tiles +self.word_tiles

        ## {"tile", number of tiles(136)}
        ## when drawing from drawable_tiles to player_tiles: --> drawable_tile - 1; player_tiles + 1
        ## when player_discard: --> player_tiles - 1; played_tiles + 1
        ### drawable_tiles + played_tiles = 136

        self.played_tiles = []

        ## dict or list??? sld be dict {"tile",number of played tiles(0)}
        ## use list coz more direct 
        ## goi siusiu yeh la

    def reset(self, player_wind, idx):
        for i in self.players.values():
            for idx in Hand.tiles:
                self.player_discard(i, idx)
        self.drawable_tiles.extend(self.played_tiles)
        self.played_tiles.clear()

        ## idk how to do
        ## maming bb plz help :<

        

        
        ## empty player_tiles and played tiles , and put all into drawable
        ## for each player hand of the player wind 
        ## empty all the players' tiles

    def pick_tile(self):
        picked_tile = random.choice(self.drawable_tiles)
        return picked_tile
        ## returns a random/top tile from derawable
        ## use this in deal

    def isStarting_wind(self):
        pass

    def deal(self,starting_wind): 
        ## deals tiles 
        ## if start wind i.e. player at startingwind => 14, else 13 (#go define player wind)
        for i in self.players.values():
            if i.wind == starting_wind:
                for tiles_dis in range(14):
                    self.player_draw(starting_wind)
            else:
                for tiles_dis in range(13):
                    self.player_draw(i.wind)

    
    def player_draw(self,player_wind):
        picked_tile = self.pick_tile()
        self.drawable_tiles.remove(picked_tile)
        self.players[player_wind].draw(picked_tile)
        ## player draws a tile from drawable tiles
        ## return picked tile to that player only?

    ## define starting_wind ##rolling dice and shit
    def player_discard(self, player_wind, idx): #adding to list of played_tiles
        tile_removed = Player.discard(idx)
        for tiles in self.drawable_tiles:
            if tile_removed not in self.drawable_tiles:
                self.played_tiles.append(tile_removed)
        return self.played_tiles
    
    def num_tiles_left(self): ## give number of tiles ***drawable*** left
        return len(self.drawable_tiles)

    def num_tile_played(self): ##give number of tiles played
        return len(self.played_tiles)

    def __str__(self):
        bigstring = ""
        for player in self.players.values():
            bigstring += str(player)
            bigstring += "\n"
        return bigstring

 

class Player:
    def __init__(self,wind):
        self.hand = Hand()
        self.wind = wind

    def draw(self, tile):  #should add to self.hand 
        self.hand.add_tile(tile)

    def discard(self, idx): # should remove from self.hand
        return self.hand.remove_tile(idx)
    
    def isDealer(self): #dice and wind "dice"
        dice_roll = random.randint(3, 18)
        for n in range (1,5):
            if dice_roll == (4*n+1): ##(First game sits on east side)
                return True
            return False

    def __str__(self):
        return self.wind + "\n" + str(self.hand)
    

class Hand:
    def __init__(self):
        self.tiles = []

    def add_tile(self,tile): ## add tile to self.tiles
        self.tiles.append(tile)

    def remove_tile(self,idx): ## removes tile at idx from self.tiles
        return self.tile.pop(idx)

    def num_tiles(self): ##return number of tiles in hand
        return len(self.tiles)


    def __str__(self):
        idx_string = ""
        tile_string = ""
        count = 0
        for tile in self.tiles:
            idx_string += "{:^6}|".format(count)
            tile_string += "{:^6}|".format(str(tile))
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
            stick (s), circle (c), million(m), words(w), #Flowers (f)

        value: int
            normal: 1-9
            words: 1:east, 2:south, 3:west, 4:north, 5:mid, 6:fat, 7:white
            ##flowers:
            flower: 1: "Plum", 2: "Lily", 3: "Chrys", 4: "Bamb"
            Season: 1: "Spr", 2: "Sum", 3: "Aut", 4: "Wint"
        """
        super().__init__() #inherit
        if type not in ["s", "c", "m", "w", "fa", "seas"]:
            raise Exception("No such Mahjong type, got {}".format(self.type))
        self.type = type
        self.value = value
        self.word_dict = {1:"east", 2:"south", 3: "west", 4: "north", 5:"mid", 6:"fat",7: "white"}
        self.flower_dict = {1: "Plum(1)", 2: "Lily(2)", 3: "Chrys(3)", 4: "Bamb(4)"}
        self.season_dict = {1: "Spr(1)", 2: "Sum(2)", 3: "Aut(3)", 4: "Wint(4)"}
        if type != "w" and type != "fa":
            if value >9 or value <1:
                raise Exception("Value not in range")
        elif type == "fa" and type == "seas":
            if value >4 or value <1:
                raise Exception("Value not in range")
        else:
            if value >7 or value <1:
                raise Exception("Value not in range")


    def __str__(self): 
        if self.type == "w":
            return self.word_dict[self.value]
        elif self.type == "fa":
            return self.flower_dict[self.value]
        elif self.type == "seas":
            return self.season_dict[self.value]
        else:
            return "{}{}".format(self.value, self.type)

    
    def isWind(self): #identifying wind tiles 
        if self.type == "w":
            if self.value < 5:
                return True  
        return False

    def isDragon(self): #identifying dragon tiles
        if self.type == "w":
            if self.value > 4:
                return True
        return False
        
    def isFlower(self):
        if self.type == "fa":
            return True
        return False

    def isSeason(self):
        if self.type == "seas":
            return True
        return False


    def __eq__(self, other):
        if self.type == other.type and self.value == other.value:
            return True
        else:
            return False



    
