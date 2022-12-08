from functools import reduce
import re

with open('./input', 'r') as file:
    input = file.read()

ents = input.split('\n')

LEFT = 1 #0001
UP   = 2 #0010
RIGHT= 4 #0100
DOWN = 8 #1000

def myScan(lines):
    visible = [[0 for element in range(len(lines[0]))] for element in range(len(lines)-1)]
    borders = {
                LEFT : [-1 for element in range(len(visible))],
                UP   : [-1 for element in range(len(visible[0]))],
                RIGHT: [-1 for element in range(len(visible))],
                DOWN : [-1 for element in range(len(visible[0]))],
            }

    for x in range(len(visible)):
        for y in range(len(visible[x])):
            xx = len(visible)-(1+x)
            yy = len(visible[x])-(1+y)
            treeTL = int(lines[x][y]);
            treeTR = int(lines[x][yy]);
            treeBL = int(lines[xx][y]);
            treeBR = int(lines[xx][yy]);

            visible[x][y]    |= (borders[LEFT][x]  < treeTL) * LEFT
            visible[x][yy]   |= (borders[RIGHT][x] < treeTR) * RIGHT
            visible[x][y]    |= (borders[UP][y]    < treeTL) * UP
            visible[xx][yy]  |= (borders[DOWN][y]  < treeBR) * DOWN

            borders[LEFT][x]  = max(treeTL, borders[LEFT][x])
            borders[RIGHT][x] = max(treeTR, borders[RIGHT][x])
            borders[UP][y]    = max(treeTL, borders[UP][y])
            borders[DOWN][y]  = max(treeBR, borders[DOWN][y])
    return visible

def mySum(lines,xx,yy):
    treeA = int(lines[xx][yy])
    t = l = b = r = 0

    for x in range(0,len(lines)-1):
        treeB = int(lines[x][yy])
        if   x < xx: t = t+1 if treeA>treeB else 1
        elif x > xx:
            b+= 1
            if not treeA>treeB: break

    for y in range(0,len(lines[0])):
        treeB = int(lines[xx][y])
        if   y < yy: l = l+1 if treeA>treeB else 1
        elif y > yy:
            r+= 1
            if not treeA>treeB: break

    return t*l*b*r

def myScan2(lines):
    visible = [[0 for element in range(len(lines[0]))] for element in range(len(lines)-1)]
    for x in range(len(visible)):
        for y in range(len(visible[x])):
            visible[x][y] = mySum(lines,x,y)

    return visible


#part 1
field = myScan(ents)
summary=0
for x in range(len(field)):
    for y in range(len(field[x])):
        if field[x][y]!=0: summary+=1

print(summary)

#part 2
field = myScan2(ents)
maximum = 0
for x in range(len(field)):
    maximum = max(maximum,max(field[x]))

print(maximum)
