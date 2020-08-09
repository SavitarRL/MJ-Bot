import random

###########
## Classes
###########

# class run:
# a while loop
# distribute --> constant check of winning --> player move(draw, action, dsicard)
# --> end if win (last check)
## the procedures of the game (4 circles, 4turns each)
## transitions after end game: show winner, count points, reset, distribute


# class End:
## show winner
## show combo and its points
## if someone wins => Game.reset

# class point counters:
## if combo fail => point = 0
## if hav flowertile matching the seat number => +1
## if pong jor dragon tiles => +1
## if pong jor wind tiles and is self wind => +2
## count point according to the combo from combos
## etcetc


class Game:
    def __init__(self):
        #players
        #list of total tiles, played and unplayed tiles
        self.players = {"E":Player("E"),"S":Player("S"),"W":Player("W"),"N":Player("N")}
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
        #self.seas_tiles =[]
        #for value in range(1,5):
        #    self.seas_tiles.append(Tile("seas"), value)
        
        #self.fa_tiles =[]
        #for value in range(1,5):
        #    self.fa_tiles.append(Tile("fa"), value)

        self.alltiles = self.stick_tiles + self.circle_tiles + self.million_tiles +self.word_tiles #+self.seas_tiles +self.fa_tiles
        self.drawable_tiles = self.stick_tiles + self.circle_tiles + self.million_tiles +self.word_tiles #+self.seas_tiles +self.fa_tiles
                                                                            ## {"tile", number of tiles(136)}
                                                                            ## when drawing from drawable_tiles to player_tiles: --> drawable_tile - 1; player_tiles + 1
                                                                            ## when player_discard: --> player_tiles - 1; played_tiles + 1
                                                                            ### drawable_tiles + played_tiles = 136
        self.played_tiles = []

        ## dict or list??? sld be dict {"tile",number of played tiles(0)}
        ## use list coz more direct 

    def reset(self):
        """
        3 steps: empty hands, clear played tiles, refill drawable tiles
        ##########
        1. empty hands iterative  - ok 
        for player in self.players.values():
            for idx in range(len(i.hand.tiles)):
                player.discard(idx)
        smart way
        for player in self.players.values():
            player.hand.tiles = [] or use .clear
        even smarter - make functions for empty hand

        2. i recc save copy of all tiles as somthing, so can revert to it at any time. so self.alltiles = [(136tiles]]
        so when reset u can do self.drawable_tiles = self.alltiles
        3. ok
        """
        
        for player in self.players.values():
            player.empty_hand()
        self.played_tiles.clear()
        self.drawable_tiles = self.alltiles
    
        ## empty player_tiles and played tiles , and put all into drawable
        ## for each player hand of the player wind 
        ## empty all the players' tiles

    def pick_tile(self):
        picked_tile = random.choice(self.drawable_tiles)
        return picked_tile
        ## returns a random/top tile from derawable
        ## use this in deal

    def isStarting_wind(self):
        #if win => stay as dealer
        #if lose => E -> S -> W -> N
        pass
    
    
    def deal(self,starting_wind): 
        ## if start wind i.e. player at startingwind => 14, else 13 (#go define player wind)
        for i in self.players.values():
            if i.wind == starting_wind:
                for tiles_dis in range(14):
                    self.player_draw(starting_wind)
            else:
                for tiles_dis in range(13):
                    self.player_draw(i.wind)

    # def rigged_deal(self, starting_wind, next_wind):
    #     while i < 1:
    #         print("Choose (2 or 3) of the same")
    #         y = input()
    #         if y == 2:
    #             for x in range():
    #                 if i.wind == starting_wind:


    #         elif y == 3:
    #             for x in range(y):

    #         else:
    #             break



    def rigged_deal2(self, starting_wind, next_wind):
        for i in self.players.values():
            if i.wind == starting_wind:
                self.rigged_player_draw(starting_wind) #East
                self.rigged_player_draw(starting_wind)
                for tiles_dis in range (12):
                    self.player_draw(starting_wind)
            
            elif i.wind == next_wind: 
                self.rigged_player_draw(next_wind) #South
                for tiles_dis in range (11):
                    self.player_draw(next_wind)
            
            else:
                for tiles_dis in range(13):
                    self.player_draw(i.wind)


    def rigged_deal3(self, starting_wind, next_wind):
        for i in self.players.values():
            if i.wind == starting_wind:
                for x in range(3):
                    self.rigged_player_draw(starting_wind) #East
                
                for tiles_dis in range (11):
                    self.player_draw(starting_wind)
            
            elif i.wind == next_wind: #South
                self.rigged_player_draw(next_wind)
                for tiles_dis in range (12):
                    self.player_draw(next_wind)
            
            else:
                for tiles_dis in range(13):
                    self.player_draw(i.wind)
    
    def rigged_choice(self):
        
        print("Choose two tiles to be in the starting deal \n ")
        print("Tile 1 Type:") 
        chosen_type1 = input() #str
        print("\n Tile 1 value:")
        chosen_value1 = input() #str
        # print("\n Tile 2 type:")
        # chosen_type2 = input() #str
        # print("\n Tile 2 value:")
        # chosen_value2 = input() #str

        tile1 = Tile(chosen_type1, int(chosen_value1))
        return tile1

    
    def rigged_player_draw(self, player_wind): #test shueng and pong
        
        tile_chose = self.rigged_choice()
        self.drawable_tiles.remove(tile_chose)

        

        # self.drawable_tiles.remove(tile2)
        # self.players[player_wind].draw(tile2)
        # tile2 = Tile(chosen_type1, int(chosen_value1)



    # def rigged_player_draw_Gong(self, player_wind): #test gong
    #     gong_tile = self.rigged_choice()
    #     for i in range(3):
    #         self.drawable_tiles.remove(gong_tile)
    #         self.players[player_wind].draw(gong_tile)

        # pong / gong need 

    
    def player_draw(self,player_wind):
        picked_tile = self.pick_tile()
        self.drawable_tiles.remove(picked_tile)
        self.players[player_wind].draw(picked_tile)
        ## player draws a tile from drawable tiles
        ## return picked tile to that player only?


        #if picked_tile.isFlower or picked_tile.isSeason:
           #see if win pos = value of flower or season tile
           #true then add points
           
    def tile_removed(self, player_wind,idx):
        return self.players[player_wind].discard(idx)
        
         
    def player_discard(self, player_wind, idx): #adding to list of played_tiles
        tile_removed = self.players[player_wind].discard(idx) 
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
    
    def __eq__(self, other):
        if self.players.values() == other.players.values():
            return True
        else:
            return False
        pass
        
# class move: pong, sheung, gong, eat
# need somewhere to store and show "action"ed tiles
class move:
    def __init__(self):
        pass

class Player:
    def __init__(self,wind):
        self.hand = Hand()
        self.wind = wind

    def draw(self, tile):  #should add to self.hand 
        self.hand.add_tile(tile)

    def discard(self, idx): # should remove from self.hand
        return self.hand.remove_tile(idx)
    
    def empty_hand(self):
        self.hand.tiles.clear()


    def isDealer(self): #dice and wind "dice"
        for n in range (1,5):
            if Dice.roll == (4*n+1): ##(First game sits on east side)
                return True
            return False
    
    def starting_seat_number(self, wind):
        if self.wind == "E":
            return 1
        elif self.wind == "S":
            return 2
        elif self.wind == "W":
            return 3
        elif self.wind == "N":
            return 4

    def __str__(self):
        return self.wind + "("+str(self.starting_seat_number(self.wind)) + ")" + "\n" + str(self.hand)
class Dice:
    def __init__(self):
        self.value = value

    def roll(self):
        return random.randint(3, 18)
        
# class Combos: (need constant check)
# 
class Combos:
    def __init__(self):
        self.hand = Hand()
        
        self.pong
        self.gong
        self.sheung
        self.eat

    def isPong(self): #return true
        pass

    def isGong(self): #return true
        pass
    
    def isSheung(self): #return true
        pass

    def isEat(self): #return true
        pass

class Hand:
    def __init__(self):
        self.tiles = []
        

    def add_tile(self,tile): ## add tile to self.tiles
        self.tiles.append(tile)

    def remove_tile(self,idx): ## removes tile at idx from self.tiles
        return self.tiles.pop(idx)

    def num_tiles(self): ##return number of tiles in hand
        return len(self.tiles)

    # stick(s) --> circle(c) --> Marn(m) --> Wind --> Dragon
    # csm => numerical order (num)
    # Wind E --> S --> W --> N
    # Dragon 
    def reaarange(self):
        pass
    
    def isWind(self): #identifying wind tiles 
        if Tile.type == "w":
            if Tile.value < 5:
                return True  
        return False

    def isDragon(self): #identifying dragon tiles
        if Tile.type == "w":
            if Tile.value > 4:
                return True
        return False

    def isNum(self):
        if self.isDragon() and self.isWind() is False:
            return True
        return False
        
    #add discarded tile from other players to the list  
    #BUT do not include in the shown player list

    def isPong(self): #return true
        game = Game()
        removed_tile = game.tile_removed(player_wind, idx)
        #for each tile: check if there are 2 more equal tiles
        for tile in self.tiles:
            if self.tiles.count(tile) == 2:
                if tile == removed_tile:
                   return True
                return False
            return False

    #add discarded tile and drew tile from other players to the list

    def isGong(self): 
        game = Game()
        removed_tile = game.tile_removed(player_wind, idx)
        #for each tile: check if there are 2 more equal tiles
        for tile in self.tiles:
            if self.tiles.count(tile) == 3:
                if tile == removed_tile:
                   return True
                return False
            return False

    
    
    # def isSheung(self): #return true
    #     #
    # pass

    # def isEat(self): #return true
    #     #
    # pass
    
    def __str__(self):
        idx_string = ""
        tile_string = ""
        count = 0
        #self.tiles.sort()
        for tile in self.tiles:
            idx_string += "{:^6}|".format(count+1)
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
            stick (s), circle (c), marn(m), words(w), #Flowers (f)

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
        elif type == "fa" or type == "seas":
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

    #these stuff in Hand?
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



    
