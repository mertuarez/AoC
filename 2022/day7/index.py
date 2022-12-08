from functools import reduce
import re

with open('./input', 'r') as file:
    input = file.read()

ents = input.split('\n')


def myScan(lines):
    cwd = ['']
    fs = []
    cmd = []
    for i in range(len(lines)):
        if not lines[i]: continue
        if lines[i][0] == "$":
            cmd = lines[i].split()
            if cmd[1] == "cd" and cmd[2] == "..":
                cwd = cwd[:-1]
            elif cmd[1] == "cd" and cmd[2] == "/":
                cwd = cwd[:1]
            elif cmd[1] == "cd":
                cwd.append(cmd[2])
            continue
        if cmd[1] == "ls":
            fname = lines[i].split()
            cwd.append(fname[1])
            fs.append('/'.join(cwd)+" "+fname[0])
            cwd = cwd[:-1]
    return fs

def mySize(lines):
    fsd = ['/']
    fss = [0]

    for i in range(len(lines)):
        line = lines[i].split(' ')
        if line[1] == "dir":
            fsd.append(line[0])
            fss.append(0)
        else:
            for j in range(len(fsd)):
                if line[0][:len(fsd[j])] == fsd[j]:
                    fss[j] += int(line[1])
    return [fsd,fss]

fsys = myScan(ents)
fsys.sort()

#part 1
fsys2 = mySize(fsys)
summary = 0
for i in range(len(fsys2[0])):
    if fsys2[1][i]<=100000:
        summary += fsys2[1][i]

print(summary)

#part2
total = fsys2[1][0]
last = total
capacity = 70000000
target = 30000000

for i in range(len(fsys2[0])):
    if last>fsys2[1][i] and capacity-(total-fsys2[1][i])>=target:
        last=fsys2[1][i]

print(last)
