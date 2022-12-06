from functools import reduce
import re

with open('./input', 'r') as file:
    input = file.read()

ents = input.split('\n')

def myCount(txt):
    pos="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    prio=[]
    for i in range(0, len(txt)):
        val=pos.index(txt[i])+1
        if val not in prio:
            prio.append(val)
    return sum(prio)


def mySum(carriage, item):
    if item:
        txt = re.sub('[^'+item[0:int(len(item)/2)]+']', '', item[int(len(item)/2):len(item)])
        result=myCount(txt);
        carriage.append(result)
    return carriage


def mySum2(items):
    result=[];
    for i in range(0,len(items)-3,3):
        val = re.sub('[^'+items[i+1]+']', '', items[i])
        val = re.sub('[^'+items[i+2]+']', '', val)
        result.append(myCount(val))
    return result


#reduce callback carriage ijection
ents.insert(0,[])

#part1
ents[0] = [] #reset cariage
red = reduce(mySum, ents)
print(sum(red))

#part2
ents.pop(0) #remove cariage
red = mySum2(ents)
print(sum(red))
