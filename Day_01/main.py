#2 december 2020
#Day one for the advent of code 2020

import sys

def findTwentyTwenty(lst):
    if lst[0] == '\n':
        return 0
    found = False
    elem = lst.pop(0)
    result = []
    #for len(lst) > 0:
    print("LOG: findTwentyTwenty : elem = ", elem)
    lst.pop(len(lst)-1)
    while len(lst) > 0:
        for i in lst:
            print("elem + i = ", int(elem), " ", int(i), " = ", int(elem)+int(i))
            if int(elem) + int(i) == 2020:
               print("result are : ", elem, " and ", i)
               found = True
               result.append(int(elem))
               result.append(int(i))
               break
        if found:
            return result
        elem = lst.pop(0)
    
    


def main(arg):
    print("Here is where the magik happen")
    if len(arg) >= 2:
        fd = open(arg[1], 'r')
    else:
        fd = open ("./input_test.txt", 'r')
    input = fd.read()
    lst = input.split('\n')
    for i in lst:
        print("element de la liste : ", i)

    res = findTwentyTwenty(lst)
    print("Final, le resultat preliminaire est : ", res)
    print("et le resultat final : ", res[0] * res[1])

if __name__=="__main__":
    print(sys.argv)
    main(sys.argv) 