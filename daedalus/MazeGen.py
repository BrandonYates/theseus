from Section import Section
from Maze import Maze
import random

class MazeGen:

    def __init__(self, data):
        self.data = data

    @staticmethod
    def initMaze(length, width):

        section = Section({})
        maze = Maze({})

        sections = [[section.build(x, y, False, False, False, False)for x in range(width)] for y in range(length)]

        maze = maze.build(length, width, sections, [0,0],[width, length])

        return maze


    @staticmethod
    def generateMaze(length, width):

        print "generating maze"
        sections = [[Section.build(x, y, False, False, False, False)for x in range(width)] for y in range(length)]
        fullMaze = Maze.build(length, width, sections, [0,0],[width, length])

        print fullMaze
        
        #track available neighbors
        maze = [[0 for x in range(width)] for y in range(length)]
        
        dx = [0, 1, 0, -1]
        dy = [-1, 0, 1, 0] # 4 directions to move in the maze

        # start the maze from a random cell

        start = [(random.randint(0, width - 1), random.randint(0, length - 1))]
        end = [(random.randint(0, width - 1), random.randint(0, length - 1))]
        stack = start

        iters = 0
        while len(stack) > 0:

            (currX, currY) = stack[-1]
            maze[currY][currX] = 1

            #print "currX: " + str(currX) + " currY: " + str(currY)

            # find a new cell to add
            nlst = [] # list of available neighbors

            #calculate movable directions
            for i in range(4):
                newX = currX + dx[i]
                newY = currY + dy[i]
                #print "newX: " + str(newX) + " newY: " + str(newY)
                #new cell must be within maze bounds    
                if newX >= 0 and newX < width and newY >= 0 and newY < length:

                    if maze[newY][newX] == 0:
                        # of occupied neighbors must be 1 to be available
                        count = 0
                        for j in range(4):
                            ex = newX + dx[j]
                            ey = newY + dy[j]
                            #print "ex: " + str(ex) + " ey: " + str(ey)
                            if ex >= 0 and ex < width and ey >= 0 and ey < length:
                                if maze[ey][ex] == 1:
                                    count += 1
                        #print "count: " + str(count)
                        if count == 1:
                            #print "append: " + str(i) 
                            nlst.append(i)

            #print "nlist length: " + str(len(nlst))
            # if 1 or more neighbors available then randomly select one and move
            if len(nlst) > 0:
                moveIndex = nlst[random.randint(0, len(nlst) - 1)]
                nextX = currX + dx[moveIndex]
                nextY = currY + dy[moveIndex]

                #open path between current section and selected neighbor
                fullMaze.joinSections(currX, currY, nextX, nextY)
                stack.append((nextX, nextY))
            else:
                stack.pop()

            iters += 1
            #print str(iters)
            if iters % 40 == 0:
                print str((iters * 100)/400) + "%"
            if iters > (400):
                return fullMaze

        return fullMaze
        

                        
