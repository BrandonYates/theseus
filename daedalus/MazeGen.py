from Section import Section
from Maze import Maze

class MazeGen:

    def __init__(self, data):
        self.data = data

    @staticmethod
    def initMaze(length, width):

        section = Section({})
        maze = Maze({})

        sections = [[section.build(length, width, 1, 1, 1, 1)for x in range(length)] for y in range(width)]

        maze = maze.build(length, width, sections, [0,0],[width, length])

        return maze
        

                        
