class Section:
    
    def __init__(self, data):
        self.data = data
        
    @classmethod
    def build(cls, x, y, north, south, east, west):
        data = {}
        data.x = x
        data.y = y
        
        walls = {}
        walls["north"] = bool(north)
        walls["south"] = bool(south)
        walls["east"] = bool(east)
        walls["south"] = bool(south)

        data.walls = walls
        return cls(data)

    @classmethod
    def fromDict(cls, dict):
        return cls(dict)

    @classmethod
    def copy(cls, copy):
        return cls(copy.data)


    @classmethod
    def isAdjacent(cls, s1, s2):
        # check adjacency
        # start at [2, 2]
        # [1, 2], [3, 2], [2,1], [2, 3] are adjacent
    
        if s1.getX() + 1 == s2.getX() and s1.getY() == s2.getY():
            return True;

        elif s1.getX - 1 == s2.getX() and s1.getY() == s2.getY():
            return True;

        elif s1.getX() == s2.getX() and s1.getY() + 1 == s2.getY():
            return True;

        elif s1.getX() == s2.getX() and s1.getY() - 1 == s2.getY():
            return True;

        return False

    #returns which wall s1 shares with s2
    #if the sections are not adjacent it will return None
    @classmethod
    def sharedWall(cls, s1, s2):

        if s1.getX() + 1 == s2.getX() and s1.getY() == s2.getY():
            return "east";

        elif s1.getX() == s2.getX() and s1.getY() == s2.getY():
            return "west"

        elif s1.getX() == s2.getX() and s1.getY() + 1 == s2.getY():
            return "north"

        elif s1.getX() == s2.getX() and s1.getY() - 1 == s2.getY():
            return "south"

        return None

    @classmethod
    def isWallOpen(cls, section, wall):

        return bool(section.getWalls()[wall])

    #returns wether or not moving from one section to another is possible
    #are these two sections adjacent, are there any walls betweent them?    
    @classmethod
    def validTransition(cls, s1, s2):

        sharedWall = Section.(s1, s2)

        if sharedWall == None:
            return False
        
        if sharedWall == "north":
            return s1.isWallOpen("north") and s2.isWallOpen("south")            

        elif sharedWall == "south":
            return s1.isWallOpen("south") and s2.isWallOpen("north") 

        elif sharedWall == "east":
            return s1.isWallOpen("east") and s2.isWallOpen("west")

        elif sharedWall == "west":
            return s1.isWallOpen("west") and s2.isWallOpen("east")

    def getX(self):
        return self.data.x

    def getY(self):
        return self.data.y

    def getWalls(self):
         return self.data.walls
