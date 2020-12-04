#Day 03
#advent of code 2020

import sys

def printLineChanged(line, pos, isTree):
    i = 0
    while i < len(line):
        if i == pos:
            if isTree == True:
                print("X", end='')
            else:
                print("O", end='')
        else:
            print(line[i], end='')
        i += 1


def tobogan(file, toRight, todown):
    tree = 0
    pos = 0
    max = 0
    isTree = False
    line = file.readline()
    max = len(line)
    print("une ligne fait : ", max)
    print("la ligne est :")
    print(line, end='')
    while line:
        pos += toRight
        line = file.readline()
        if todown == 2:
            line = file.readline()
        if pos >= len(line)-1:
            pos = pos - len(line) +1

        if line:
            if line[pos] == "#":
                tree += 1
                isTree = True
        printLineChanged(line, pos, isTree)
        isTree = False
    return tree



def main(arg):
    print("Here is where the magik happen")
    finalRes = 0
    finalResLst = []
    if len(arg) >= 2:
        fd = open(arg[1], 'r')
    else:
        fd = open ("./input.txt", 'r')
    finalRes = tobogan(fd, 3, 1)
    print("et donc il y a eu : ", finalRes, " tree")
    print("Part 2 :")
    fd.close()
    fd = open(arg[1], 'r')
    finalResLst.append(tobogan(fd, 1, 1))
    fd.close()
    fd = open(arg[1], 'r')
    finalResLst.append(tobogan(fd, 3, 1))
    fd.close()
    fd = open(arg[1], 'r')
    finalResLst.append(tobogan(fd, 5, 1))
    fd.close()
    fd = open(arg[1], 'r')
    finalResLst.append(tobogan(fd, 7, 1))
    fd.close()
    fd = open(arg[1], 'r')
    finalResLst.append(tobogan(fd, 1, 2))
    fd.close()
    print(finalResLst)
    total = 1
    for i in finalResLst:
        total *= i
    print("le tttal = ", total)


if __name__=="__main__":
    print(sys.argv)
    main(sys.argv) 