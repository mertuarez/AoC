from functools import reduce
import re

with open('./input', 'r') as file:
    input = file.read()

ents = input.split('\n')


def myCheck(line,read_size):
    for i in range(len(line)):
        occur = 0
        my_line = line[i:i+read_size]
        for j in range(len(my_line)):
            occur = max(occur, my_line.count(my_line[j]))
        if occur == 1: break
    return i+read_size


#part1
pos = myCheck(ents[0],4)
print(pos)

#part2
pos = myCheck(ents[0],14)
print(pos)
