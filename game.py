from classes import *






if __name__ == "__main__":

    ##test init
    game = Game()
    print("initial state")
    print(game)
    assert (all(player.hand.num_tiles()==0 for player in game.players)), "players don't start with empty hand"
    assert (game.num_tiles_left()==136), "Reminaing tiles is not 136 tiles or num_tiles_left() not implemented"
    print("pass init")

    ## test deal
    game.deal("W")
    print(game)
    assert (game.players["W"].hand.num_tiles()==14), "starting wind doesn't have 14 tiles"
    assert (game.players[i].hand.num_tiles()==13 for i in ["N","S","E"]), "non-starting wind doesn't have 13 tiles"
    assert (game.num_tiles_left()==83), "Reminaing tiles is not 83 tiles or num_tiles_left() not implemented"
    print("pass deal")

    ## test 
    game.player_discard("S", 10)
    print(game)
    assert (game.players["W"].hand.num_tiles()==14), "starting wind doesn't have 14 tiles"
    assert (game.players[i].hand.num_tiles()==13 for i in ["N","E"]), "non-starting wind doesn't have 13 tiles"
    assert (game.players["S"].hand.num_tiles()==12), "played card didn't decrease hand size"
    assert (game.num_tiles_left()==83), "Reminaing tiles is not 83 tiles or num_tiles_left() not implemented"
    for i in range(13):
        game.player_discard("N", 0)
    game.player_discard("E", 10)
    assert (game.players["W"].hand.num_tiles()==14), "starting wind doesn't have 14 tiles"
    assert (game.players["N"].hand.num_tiles()==0), "can't play all cards"
    assert (game.players["S"].hand.num_tiles()==12), "playing card affects other players"
    assert (game.players["E"].hand.num_tiles()==12), "played card didn't decrease hand size"
    assert (game.num_tiles_left()==83), "Reminaing tiles is not 83 tiles or num_tiles_left() not implemented"

    
    print("pass discard")

    game.player_draw("N")
    print(game)
    assert (game.players["W"].hand.num_tiles()==14), "starting wind doesn't have 14 tiles"
    assert (game.players["N"].hand.num_tiles()==1), "Draw incorrect num of card/ didn't draw"
    assert (game.players["S"].hand.num_tiles()==12), "drawing card affects other players"
    assert (game.players["E"].hand.num_tiles()==12), "drawing card affects other players"
    assert (game.num_tiles_left()==82), "Reminaing tiles is not 82 tiles or num_tiles_left() not implemented"

    print("pass draw")

    game.reset()
    print(game)
    assert (all(player.hand.num_tiles()==0 for player in game.players)), "players don't start with empty hand"
    assert (game.num_tiles_left()==136), "Reminaing tiles is not 136 tiles or num_tiles_left() not implemented"
    print("pass reset")







    
     
