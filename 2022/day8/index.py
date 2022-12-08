with open('./input', 'r') as file:
    input = file.read()

ents = input.split('\n')

LEFT = 1 #0001
UP   = 2 #0010
RIGHT= 4 #0100
DOWN = 8 #1000

def myScan(lines):
    visible = [[0 for i in range(len(lines[0]))] for j in range(len(lines)-1)]
    treeT = [-1 for element in range(len(visible))]
    treeB = [-1 for element in range(len(visible))]

    for x in range(len(visible)):
        treeL = -1
        treeR = -1
        for y in range(len(visible[x])):
            xx = len(visible)   -(1+x)
            yy = len(visible[x])-(1+y)

            visible[x ][y ] |= (int(lines[x ][y ]) > treeL   ) * LEFT
            visible[x ][yy] |= (int(lines[x ][yy]) > treeR   ) * RIGHT
            visible[x ][y ] |= (int(lines[x ][y ]) > treeT[y]) * UP
            visible[xx][y ] |= (int(lines[xx][y ]) > treeB[y]) * DOWN

            treeL    = max(treeL,    int(lines[x ][y ]))
            treeR    = max(treeR,    int(lines[x ][yy]))
            treeT[y] = max(treeT[y], int(lines[x ][y ]))
            treeB[y] = max(treeB[y], int(lines[xx][y ]))

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
