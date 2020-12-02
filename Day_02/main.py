#2 december 2020
#Day two for the advent of code 2020

import sys


def checkPasswordRule(line):
    if len(line) == 0:
        return False
    print("LOG: checkPasswordRule: line = ", line, len(line))
    lst = line.split(' ')
    mini = int(lst[0].split('-')[0])
    maxi = int(lst[0].split('-')[1])
    letter = lst[1][0]
    #password to check
    pwtc = lst[2]
    numLetterInPWTC = pwtc.count(letter)
    print("regle : il faut minimum : ", mini, " et au maximum ", maxi, " la lettre : ", letter, " le mdp a verifier : ", pwtc)
    print("et il y a : ", numLetterInPWTC)
    if numLetterInPWTC >= mini and numLetterInPWTC <= maxi:
        print("c'est Bon !")
        return True
    else:
        return False

def main(arg):
    print("Here is where the magik happen")
    finalRes = 0
    if len(arg) >= 2:
        fd = open(arg[1], 'r')
    else:
        fd = open ("./input_password.txt", 'r')
    input = fd.read()
    lst = input.split('\n')
    for i in lst:
        print("element de la liste : ", i)
        rtr = checkPasswordRule(i)
        if rtr:
            finalRes += 1
    checkPasswordRule(lst[0])
    print("il y a ", finalRes, " password valid")

if __name__=="__main__":
    print(sys.argv)
    main(sys.argv) 