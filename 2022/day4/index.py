from functools import reduce
import re

with open('./input', 'r') as file:
    input = file.read()

ents = input.split('\n')

def mySplit(carriage, item):
    if item:
        txt = re.split(',|-', item)
        result=txt
        carriage.append(result)
    return carriage

def myOverlap(carriage, item):
    if item:
        if (int(item[0])<=int(item[2]) and int(item[1])>=int(item[3])) or (int(item[0])>=int(item[2]) and int(item[1])<=int(item[3])):
            carriage.append(1)
    return carriage

def myOverlap2(carriage, item):
    if item:
        if (int(item[0])<=int(item[2]) and int(item[2])<=int(item[1]) or
            int(item[0])<=int(item[3]) and int(item[3])<=int(item[1]) or
            int(item[2])<=int(item[0]) and int(item[0])<=int(item[3]) or
            int(item[2])<=int(item[1]) and int(item[1])<=int(item[3])
            ):
            carriage.append(1)
    return carriage

#reduce callback carriage ijection
ents.insert(0,[])
ents[0] = [] #reset cariage
red = reduce(mySplit, ents)
red.insert(0,[])

#part1
red[0] = [] #reset cariage
red2 = reduce(myOverlap, red)
print(sum(red2))

#part2
red[0] = [] #reset cariage
red2 = reduce(myOverlap2, red)
print(sum(red2))
