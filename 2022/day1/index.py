from functools import reduce

with open('./input', 'r') as file:
    input = file.read()

ents = input.split('\n\n')

def mySum(a, b):
    a.append(sum([int(i) for i in b.split('\n') if i != '' ]))
    return a

#reduce callback carriage ijection
ents.insert(0,[])

#part1
red = reduce(mySum, ents)
print(max(red))
#part2
red = sorted(red, reverse=True)
print(red[0]+red[1]+red[2])
