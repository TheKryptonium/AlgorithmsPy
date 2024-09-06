#-*-coding utf-8 *-
from itertools import permutations

def factorial(number):
    if number<=1: return 1
    else:return number*factorial(number-1)

def permute(string, pocket=""):
    if len(string)==0: 
        print(pocket)
    else:
        for i in range(len(string)):
            letter = string[i]
            front= string[0:i]
            back= string[i+1:]
            together= front+back
            permute(together, letter+pocket)


print(factorial(14))
print(permute("ABC"))