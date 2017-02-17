from Section import Section

class Maze(object):

    def __init__(self, maze):
        self.maze = maze

    @classmethod
    def build(cls, length, width, sections, start, end):

        maze = {}
        maze["length"] = length
        maze["width"] = width
        maze["sections"] = sections
        maze["start"] = start
        maze["end"] = end

        return cls(maze)

    #take coordiantes of two adjacent sections and open the wall between them
    def joinSections(self, x1, y1, x2, y2):

        s1 = self.maze["sections"][y1][x1]
        s2 = self.maze["sections"][y2][x2]
        
        shared = Section.sharedWall(s1, s2)

        print "shared wall is " + shared

        #shared indicates the direction one must travel
        #to get to s2 from s1
        #open that wall for s1 and the opposite wall for s2 to allow travel
        if shared == "north":
            s2.openWall("north")
            s1.openWall("south")
        elif shared == "south":
            s2.openWall("south")
            s1.openWall("north")
        elif shared == "east":
            s1.openWall("east")
            s2.openWall("west")
        elif shared == "west":
            s1.openWall("west")
            s2.openWall("east")
        else:
            raise ValueError('bad wall value returned by Section.sharedWall(): ' + shared)

        self.maze["sections"][y1][x1] = s1
        self.maze["sections"][y2][x2] = s2

        
    # Returns the result of attempting to traverse the maze
    # Path is an array of Section objects
    def correctPath(self, path):

        correctStart = (path[0] == self.start)

        # Exit early if the path does not begin and end  at the correct section
        if not correctStart:
            return False

        correctEnd = (path[path.len] == self.end)

        if not correctEnd:
            return False

        # Iterate through transitions and return false if any transition is not valid
        # any path made up of a sequence of valid transitions which begins and ends
        # at the correct start and end is considered a valid path
        for step in range(0, path.len - 1):
            s1 = sections[path[step][0], path[step][1]]
            s2 = sections[path[step + 1][0], path[step + 1][1]]
            
            if not Section.validTransition(path[step], path[step + 1]):
                return False

        return True
    
    def __str__(self):
        
        string = ""
        
        for y in range(self.maze["length"]):
            for z in range(0, 3):
                for x in range(self.maze["width"]):
                    print "x: " + str(x) + " y: " + str(y) + " z: " + str(z)
                    string += self.maze["sections"][y][x].getRow(z)
                
                string += "\n"
        
        return string

    def getSections(self):
        return self.maze["sections"]
