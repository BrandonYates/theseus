from MazeGen import MazeGen
from Section import Section

maze = MazeGen.initMaze(2,2)

print maze.getSections()[0][0]

print "adjacent? " + str(Section.isAdjacent(maze.getSections()[0][0], maze.getSections()[1][0]))

closedSection = Section({}).build(4,4, False, False, False, False)
openSection = Section({}).build(4,5, True, True, True, True)

print openSection
print closedSection

print "validTransition: " + str(Section({}).validTransition(openSection, closedSection))


shared = Section({}).sharedWall(closedSection, openSection)

print "shared: " + shared

closedSection.openWall(shared)

print closedSection.getWalls()

print closedSection

print "validTransition now:  " + str(Section({}).validTransition(closedSection, openSection))


print "\n\n"

print maze

print "\n\n"
maze.joinSections(0,0,0,1)


print maze

maze2 = MazeGen.generateMaze(10, 10)

print maze2
