from MazeGen import MazeGen

maze = MazeGen.initMaze(10,10)

print maze.getSections()[0][0]


print "\n\n"

#print maze


maze2 = MazeGen.generateMaze(10, 10)

print maze2
