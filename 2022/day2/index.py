from functools import reduce

with open('./input', 'r') as file:
    input = file.read()

ents = input.split('\n')

def mySum(carriage, item):
    if item:
        match item:
            case "A X": value = 3+1
            case "A Y": value = 6+2
            case "A Z": value = 0+3
            case "B X": value = 0+1
            case "B Y": value = 3+2
            case "B Z": value = 6+3
            case "C X": value = 6+1
            case "C Y": value = 0+2
            case "C Z": value = 3+3
        carriage.append(value)
    return carriage


def mySum2(carriage, item):
    if item:
        match item:
            case "A X": value = 0+3
            case "B X": value = 0+1
            case "C X": value = 0+2
            case "A Y": value = 3+1
            case "B Y": value = 3+2
            case "C Y": value = 3+3
            case "A Z": value = 6+2
            case "B Z": value = 6+3
            case "C Z": value = 6+1
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
