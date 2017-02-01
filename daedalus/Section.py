class Section(object):
    
    def __init__(self, data):
        self.data = data
        
    @classmethod
    def build(cls, x, y, north, south, east, west):
        data = {}
        data["x"] = x
        data["y"] = y
        
        data["north"] = bool(north)
        data["south"] = bool(south)
        data["east"] = bool(east)
        data["west"] = bool(west)
        return cls(data)

    @classmethod
    def fromDict(cls, dict):
        return cls(dict)

    @classmethod
    def copy(cls, copy):
        return cls(copy.data)


    @staticmethod
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
    @staticmethod
    def sharedWall(s1, s2):

        if s1.getX() + 1 == s2.getX() and s1.getY() == s2.getY():
            return "east";

        elif s1.getX() == s2.getX() and s1.getY() == s2.getY():
            return "west"

        elif s1.getX() == s2.getX() and s1.getY() + 1 == s2.getY():
            return "north"

        elif s1.getX() == s2.getX() and s1.getY() - 1 == s2.getY():
            return "south"

        return None

    @staticmethod
    def isWallOpen(section, wall):

        return bool(section.getWalls()[wall])

    #set a particular wall to open
    def openWall(self, wall):

        #wall already open
        if self.data[wall]:
            return
        else:
            self[wall] = True

    #returns wether or not moving from one section to another is possible
    #are these two sections adjacent, are there any walls betweent them?    
    @classmethod
    def validTransition(cls, s1, s2):

        sharedWall = Section.sharedWall(s1, s2)

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

    def __str__(self):
        """
        closed    ***
                  * *
                  ***
        """
        string = "*"
        string += ("*" if self.data["north"] else " ")
        string += "*"
        string += "\n"
        string += ("*" if self.data["west"] else " ")
        string += " "
        string += ("*" if self.data["east"] else " ")
        string += "\n"
        string += "*"
        string += ("*" if self.data["south"] else " ")
        string += "*"

        return string

    def getRow(self, n):

        if n == 0:
            return "*" + ("*" if self.data["north"] else " ") + "*"
        elif n == 1:
            return ("*" if self.data["west"] else " ") + " " + ("*" if self.data["east"] else " ")
        elif n== 2:
            return "*" + ("*" if self.data["south"] else " ") + "*"
        else:
            return None
    
    def dump(self):

        print "x: " + str(self.data.x) + " y: " + str(self.data.y)

        for x in self.data.walls.keys():
            print str(self.data.walls.keys()[x]) + " " + str(self.data.walls[x])

        
    def getX(self):
        return self.data["x"]

    def getY(self):
        return self.data["y"]

    def getWalls(self):
        walls = []
        walls.append(self.data["north"])
        walls.append(self.data["south"])
        walls.append(self.data["east"])
        walls.append(self.data["west"])
        return walls
