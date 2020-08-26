from classes import *


#test init
def test_init(show=False):
    game = Game()
    if show:
        print(game)
    assert (all(player.hand.num_tiles()==0 for player in game.players.values())), "players don't start with empty hand"
    assert (game.num_tiles_left()==136), "Reminaing tiles is not 136 tiles or num_tiles_left() not implemented"
    print("pass init")

#test deal
def test_deal(show=False):
    game = Game()
    ## test deal
    game.deal("W")
    # print(game)
    if show:
        print(game)
    assert (game.players["W"].hand.num_tiles()==14), "starting wind doesn't have 14 tiles"
    assert (game.players[i].hand.num_tiles()==13 for i in ["N","S","E"]), "non-starting wind doesn't have 13 tiles"
    assert (game.num_tiles_left()==83), "Reminaing tiles is not 83 tiles or num_tiles_left() not implemented"
    print("pass deal")

#test discard
def test_discard(show=False):
    game = Game()
    ## test deal
    game.deal("W")
    game.player_discard("S", 10)
    if show:
        print(game)
    assert (game.players["W"].hand.num_tiles()==14), "starting wind doesn't have 14 tiles"
    assert (game.players[i].hand.num_tiles()==13 for i in ["N","E"]), "non-starting wind doesn't have 13 tiles"
    assert (game.players["S"].hand.num_tiles()==12), "played card didn't decrease hand size"
    assert (game.num_tiles_left()==83), "Reminaing tiles is not 83 tiles or num_tiles_left() not implemented"
    for i in range(13):
        game.player_discard("N", 0)
    game.player_discard("E", 10)
    if show:
        print(game)
    assert (game.players["W"].hand.num_tiles()==14), "starting wind doesn't have 14 tiles"
    assert (game.players["N"].hand.num_tiles()==0), "can't play all cards"
    assert (game.players["S"].hand.num_tiles()==12), "playing card affects other players"
    assert (game.players["E"].hand.num_tiles()==12), "played card didn't decrease hand size"
    assert (game.num_tiles_left()==83), "Reminaing tiles is not 83 tiles or num_tiles_left() not implemented"
    print("pass discard")

#test draw
def test_draw(show=False):
    game = Game()
    ## test deal
    game.deal("W")
    game.player_discard("S", 10)
    for i in range(13):
        game.player_discard("N", 0)
    game.player_discard("E", 10)
    game.player_draw("N")
    if show:
        print(game)
    assert (game.players["W"].hand.num_tiles()==14), "starting wind doesn't have 14 tiles"
    assert (game.players["N"].hand.num_tiles()==1), "Draw incorrect num of card/ didn't draw"
    assert (game.players["S"].hand.num_tiles()==12), "drawing card affects other players"
    assert (game.players["E"].hand.num_tiles()==12), "drawing card affects other players"
    assert (game.num_tiles_left()==82), "Reminaing tiles is not 82 tiles or num_tiles_left() not implemented"
    print("pass draw")

#test reset
def test_reset(show=False):
    game = Game()
    ## test deal
    game.deal("W")
    game.player_discard("S", 10)
    for i in range(13):
        game.player_discard("N", 0)
    game.player_discard("E", 10)
    game.player_draw("N")
    game.reset()
    if show:
        print(game)
    assert (all(player.hand.num_tiles()==0 for player in game.players.values())), "players don't start with empty hand"
    assert (game.num_tiles_left()==136), "Reminaing tiles is not 136 tiles or num_tiles_left() not implemented"
    print("pass reset")

#test rigged deal
def test_rdeal(show=False):
    game = Game()
    hand = Hand()
    ## test rigged deal (starting_wind, next_wind)
    ## east is starting, next is south
    ## game.rigged_choice() = 9c (can change to white)
    ans = input("test 2 or 3: ")
    
    start_handtiles = game.players["E"].hand.tiles
    nxt_handtiles = game.players["S"].hand.tiles
    
    if ans == "2":
        game.rigged_deal2("E", "S")
        if show: #if show == True: print game
            print(game)
        #test rigged stuff
        for dup_tile in nxt_handtiles:
            if nxt_handtiles.count(dup_tile) == 2:
                THE_tile = dup_tile 
        assert (game.rigged_choice() == dup_tile for dup_tile in nxt_handtiles if nxt_handtiles.count(dup_tile) == 2), "Tile of starting wind does not have two of a kind"
        # assert (game.rigged_choice() == sgl_tile for sgl_tile in nxt_handtiles == THE_tile), "Tile of the next wind does not have the kind chosen"
        # can be ommited because zi gei set jor
        assert (game.players["E"].hand.num_tiles()==14), "starting wind doesn't have 14 tiles"
        assert (game.players[i].hand.num_tiles()==13 for i in ["N","S","E"]), "non-starting wind doesn't have 13 tiles"
        assert (game.num_tiles_left()==83), "Reminaing tiles is not 83 tiles or num_tiles_left() not implemented"
        if (game.num_tiles_left()!=83):
            print("Remaining tiles is: {}".format(game.num_tiles_left())) 
        print("pass rigged_deal 2")

    elif ans == "3":
        game.rigged_deal3("E", "S")
        if show: #if show == True: print game
            print(game)
        #test rigged stuff
        for dup_tile in nxt_handtiles:
            if start_handtiles.count(dup_tile) == 3:
                THE_tile = dup_tile 
        assert (game.rigged_choice() == dup_tile for dup_tile in nxt_handtiles if nxt_handtiles.count(dup_tile) == 3), "Tile of starting wind does not have three of a kind"
        assert (game.players["E"].hand.num_tiles()==14), "starting wind doesn't have 14 tiles"
        assert (game.players[i].hand.num_tiles()==13 for i in ["N","S","E"]), "non-starting wind doesn't have 13 tiles"
        assert (game.num_tiles_left()==83), "Reminaing tiles is not 83 tiles or num_tiles_left() not implemented"
        if (game.num_tiles_left()!=83):
            print("Remaining tiles is: {}".format(game.num_tiles_left())) 
        print("pass rigged_deal 3")
    
    else: 
        print("Try again")
    
#test isPong
def test_isPong(show=False):
    game = Game()
    hand = Hand()
    # east bei south c9x3 def
    # south pong
    #another case:
    # south bei north; north pong
    # if success --> pass
    start_handtiles = game.players["E"].hand.tiles
    nxt_handtiles = game.players["S"].hand.tiles
    game.rigged_deal2("E", "S")
    #tile to remove = game.rigged_choice()
    rtile = game.rigged_choice()
    idx =  game.players[player_wind].hand.tiles.index(rtile)
    game.player_discard("E", idx)
    if show:
        print(game)
    #tests 
    # 1. start player remove has 13 cards
    assert (game.players["E"].hand.num_tiles()==13), "starting wind doesn't have 13 tiles"
    # 2. da yuen added to a list, every player can use that card 
    assert (game.players[i].hand.num_tiles()==13 for i in ["N","S","E"]), "non-starting wind doesn't have 13 tiles"
    # 3. no draw => remaining tiles = 83
    assert (game.num_tiles_left()==83), "Reminaing tiles is not 83 tiles or num_tiles_left() not implemented"
    # 4. if removed tile in the list + hand.tiles = 3 --> pass isPong
    assert(game.players["S"].hand.isPong() is True), "isPong Error"
    print("pass isPong")
    pass

def test_gong(show = False):
    game = Game()
    hand = Hand()
    # east bei south c9x4
    # south pong
    #another case:
    # south bei north; north pong
    # if success --> pass
    start_handtiles = game.players["E"].hand.tiles
    nxt_handtiles = game.players["S"].hand.tiles
    game.rigged_deal3("E", "S")
    game.player_discard("E", 10)
    if show:
        print(game)
    #tests 
    # 1. start player remove has 13 cards
    assert (game.players["E"].hand.num_tiles()==13), "starting wind doesn't have 13 tiles"
    # 2. da yuen all players can have that card (everyone has 14) 
    assert (game.players[i].hand.num_tiles()==14 for i in ["N","S","E"]), "non-starting wind doesn't have 14 tiles"
    # 3. no draw => remaining tiles = 83
    assert (game.num_tiles_left()==83), "Reminaing tiles is not 83 tiles or num_tiles_left() not implemented"
    # 4. if removed tile + hand.tiles = 4 --> pass isGong
    pass

def test_sheung(show = False):
    pass

def test_eat(show=False):
    pass

def test_pointcounter(show=False):
    pass

def test_player_move(show=False):
    pass

def test_game_run(show=False):
    pass


# if __name__ == "__main__":
#     test_discard()


    

    
    

    







    
     
