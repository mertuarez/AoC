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
    borders = {
                LEFT : [-1 for element in range(len(lines)-1)],
                UP   : [-1 for element in range(len(lines[0]))],
                RIGHT: [-1 for element in range(len(lines)-1)],
                DOWN : [-1 for element in range(len(lines[0]))],
            }
    visible = [[0 for element in range(len(lines[0]))] for element in range(len(lines)-1)]
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
    l = 0
    r = 0
    t = 0
    b = 0

    for x in range(0,len(lines)-1):
        treeB = int(lines[x][yy])
        if x == xx:
            continue
        elif x < xx:
            if treeA>treeB:
                t+=1
            else:
                t=1
        elif x > xx:
            if treeA>treeB:
                b+=1
            else:
                b+=1
                break

    for y in range(0,len(lines[0])):
        treeB = int(lines[xx][y])
        if y == yy:
            continue
        elif y < yy:
            if treeA>treeB:
                l+=1
            else:
                l=1
        elif y > yy:
            if treeA>treeB:
                r+=1
            else:
                r+=1
                break



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
