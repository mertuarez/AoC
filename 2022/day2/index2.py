from functools import reduce

with open('./input', 'r') as file:
    input = file.read()

ents = input.split('\n')

def mySum(carriage, item):
    if item:
        vals = {"A":1,"B":2,"C":3,"X":1,"Y":2,"Z":3}
        value = vals[item[2]];
        value += 3 if vals[item[0]] - vals[item[2]] == +0 else 0
        value += 6 if vals[item[0]] - vals[item[2]] == -1 else 0
        value += 6 if vals[item[0]] - vals[item[2]] == +2 else 0
        carriage.append(value)
    return carriage


def mySum2(carriage, item):
    if item:
        vals = {"A":1,"B":2,"C":3,"X":0,"Y":3,"Z":6}
        scor = [1,2,3,1,2]
        value = vals[item[2]]+scor[vals[item[0]]+1] if vals[item[2]] == vals["X"] else 0
        value = vals[item[2]]+scor[vals[item[0]]-1] if vals[item[2]] == vals["Y"] else value
        value = vals[item[2]]+scor[vals[item[0]]+0] if vals[item[2]] == vals["Z"] else value
        carriage.append(value)
    return carriage


#reduce callback carriage ijection
ents.insert(0,[])

#part1
ents[0] = [] #reset cariage
red = reduce(mySum, ents)
print(sum(red))

#part2
ents[0] = [] #reset cariage
red = reduce(mySum2, ents)
print(sum(red))
