import math
from itertools import permutations

V=4

def separator():
    print('\n')
    print('***********************************************************')
    print('\n')


#Egyptian fractions
def egyptianFraction(numerator, denominator):

    egyptList=[]

    while numerator!=0:
        x = math.ceil(denominator/numerator)
        egyptList.append(x)
        numerator = x*numerator-denominator
        denominator *= numerator
        print('Numerator: ', numerator, ' Denominator: ', denominator)

    print("Egypt list: ")
    print(egyptList)
    string=""

    for ones in egyptList:
        string += '1/{0} + '.format(ones)

    finalString= string[:-3]
    print("The final fraction is: ", finalString)

egyptianFraction(24,1000)

separator()

#UGLY NUMBERS
def successDiv(x,y):
    while x%y == 0:
        x = x//y
    return x

def uglyCheck(number) :
    number = successDiv(number,2)
    number = successDiv(number, 3)
    number = successDiv(number, 5)

    if number == 1:
        return True
    else :
        return False


def nthUgly(n):
    i = 1
    counter = 1

    while n > counter:
        i+=1
        if uglyCheck(i):
            counter+=1
    
    return i

n=int(input('Enter the rank of the ugly number you want: '))
print('The {0}th ugly number is: {1}'.format(n, nthUgly(n)))

separator()

#SHORTEST PATH ALGORITHM
def travelSalesmanProblem(graph, s):
    
    vertex =[]

    for i in range(V):
        if i != s :
            vertex.append(i)
            print(vertex)
    
    minPath = []
    nextPerm  = permutations(vertex)

    for i in nextPerm:
        currentPath = 0
        k=s

        for j in i:
            currentPath += graph[k][j]
            k=j
        
        currentPath += graph[k][s]
        minPath.append(currentPath)
        x = sorted(minPath)

    return x[0]


graph = [[0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]]

s=2
print("The shortest path: ", travelSalesmanProblem(graph, s))
