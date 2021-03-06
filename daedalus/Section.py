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
    def isAdjacent(s1, s2):
        # check adjacency
        # start at [2, 2]
        # [1, 2], [3, 2], [2,1], [2, 3] are adjacent

        print "isAdjacent"
        print "x: " + str(s1.getX()) + " y: " + str(s1.getY())
        print "x: " + str(s2.getX()) + " y: " + str(s2.getY())
        
        if s1.getX() + 1 == s2.getX() and s1.getY() == s2.getY():
            return True;

        elif s1.getX() - 1 == s2.getX() and s1.getY() == s2.getY():
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

        elif s1.getX() - 1 == s2.getX() and s1.getY() == s2.getY():
            return "west"

        elif s1.getX() == s2.getX() and s1.getY() + 1 == s2.getY():
            return "north"

        elif s1.getX() == s2.getX() and s1.getY() - 1 == s2.getY():
            return "south"

        return None

    def isWallOpen(self, wall):

        return self.data[wall]

    #set a particular wall to open
    def openWall(self, wall):
        self.data[wall] = True

    #returns whether or not moving from one section to another is possible
    #e.g. are these two sections adjacent? Are there any walls between them?    
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

    #prints this single section independently
    #cannot be used in a loop to print a full maze
    def __str__(self):
        """
        closed    ***
                  * *
                  ***
        """
        
        string = "*"
        string += ("*" if not bool(self.data["north"]) else " ")
        string += "*"
        string += "\n"
        string += ("*" if not bool(self.data["west"]) else " ")
        string += " "
        string += ("*" if not bool(self.data["east"]) else " ")
        string += "\n"
        string += "*"
        string += ("*" if not bool(self.data["south"]) else " ")
        string += "*"

        return string

    #used to iterate through a maze and print it to the console
    def getRow(self, n):

        if n == 0:
            return "*" + ("*" if not self.data["north"] else " ") + "*"
        elif n == 1:
            return ("*" if not self.data["west"] else " ") + " " + ("*" if not self.data["east"] else " ")
        elif n == 2:
            return "*" + ("*" if not self.data["south"] else " ") + "*"
        else:
            return None
    
    def dump(self):

        print "x: " + str(self.data["x"]) + " y: " + str(self.data["y"])

        print "north: " + str(self.data["north"])
        print "south: " + str(self.data["south"])
        print "east: " + str(self.data["east"])
        print "west: " + str(self.data["west"])
       
    def getX(self):
        return self.data["x"]

    def getY(self):
        return self.data["y"]

    def getWalls(self):
        walls = {}
        walls["north"] = self.data["north"]
        walls["south"] = self.data["south"]
        walls["east"] = self.data["east"]
        walls["west"] = self.data["west"]
        return walls
