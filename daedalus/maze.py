from daedalus import section

class Maze:

    def __init__(self, maze):
        self.maze = maze


    @classmethod
    def build(cls, length, width, sections, start, end):
        self.length = length
        self.width = width
        self.sections = sections
        self.start = start
        self.end = end


    #returns the result of attempting to traverse the maze
    #path is an array of Section objects    
    def correctPath(self, path):

        correctStart = path[0] == self.start

        #exit early if the path does not begin and end  at the correct section
        if not correctStart:
            return False

        correctEnd = path[path.len] == self.end

        if not correctEnd:
            return False

        #iterate through transitions and return false if any transition is not valid
        #any path made up of a sequence of valid transitions which begins and ends
        #at the correct start and end is considered a valid path
        for step in range(0, path.len -1):
            if not Section.validTransition(path[step], path[step + 1]):
                return False


        return True                
