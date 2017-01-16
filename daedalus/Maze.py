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
        
        for step in range(0, path.len -1):
            
            if not Section.validTransition(path[step], path[step + 1]):
                return False

        return True

    
    def __str__(self):
        
        string = ""
        
        for x in range(self.maze["length"]):
            
            for y in range(0, 3):
                
                for z in range(self.maze["width"]):
                    string += self.maze["sections"][x][y].getRow(y)
                
                string += "\n"
        
        return string

    def getSections(self):
        return self.maze["sections"]
