from classes import *






if __name__ == "__main__":
    print(Tile("stick", 2))
    print(Tile("words",6))
    print(Tile("circle",1))
    a = Tile("circle" , 6)
    b = Tile("words", 3)
    print(a.isDirection())
    print(b.isDirection())
    c = Tile("circle" , 6)
    print(a==c)