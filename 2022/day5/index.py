from functools import reduce
import re

with open('./input', 'r') as file:
    input = file.read()

ents = input.split('\n')

def myCrates(items):
    my_crates = [[] for i in range(int((len(items[0])+1)/4))]
    for i in range(len(items)):
        item = " "+items[i]
        if items[i+1].strip() == "": break
        for j in range(0, int(len(item)/4)):
            val = item[2+j*4]
            if val.strip() == "": continue
            my_crates[j].insert(0,val)
    return my_crates

def myMoves(carriage,items):
    my_crates = carriage[:]
    for i in range(len(my_crates)+1,len(items)+0):
        if items[i].strip() == "": break
        cmd = re.sub('[^0-9 ]', '', items[i]).split()
        my_crates[int(cmd[2])-1].extend(reversed(my_crates[int(cmd[1])-1][-int(cmd[0]):]))
        my_crates[int(cmd[1])-1] = my_crates[int(cmd[1])-1][:-int(cmd[0])]

    return my_crates

def myMoves2(carriage,items):
    my_crates = carriage[:]
    for i in range(len(my_crates)+1,len(items)+0):
        if items[i].strip() == "": break
        cmd = re.sub('[^0-9 ]', '', items[i]).split()
        my_crates[int(cmd[2])-1].extend(my_crates[int(cmd[1])-1][-int(cmd[0]):])
        my_crates[int(cmd[1])-1] = my_crates[int(cmd[1])-1][:-int(cmd[0])]

    return my_crates


#part1
crates = myCrates(ents)
moves = myMoves(crates,ents)
for i in range(len(moves)): print(moves[i][-1:])
print("")

#part1
crates = myCrates(ents)
moves = myMoves2(crates,ents)
for i in range(len(moves)): print(moves[i][-1:])
print("")
