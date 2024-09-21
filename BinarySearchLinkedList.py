def locate_card(cards, expcted): #linear search
    solution =-1
    
    for i in range(len(cards)):
        if cards[i]==expcted:
            solution = i
    
    return solution


def locateCard(cards, expected): #binary search
    lower, higher = 0, len(cards)-1

    while(lower <= higher):
        mid  = (lower+higher) // 2
        print("Lower: ", lower, " Higher: ", higher, " middle number: ", cards[mid], " middle index: ", mid)
        
        if(cards[mid] < expected):
            higher = mid -1
        elif(cards[mid] > expected):
            lower = mid +1
        else:
            return mid
    
    return -1   
   

def EvaluateTestCase(locationFunc, test):
    return (locationFunc(test['inputs']['card'], test['inputs']['query'])==test['output'])


tests =  []

test = {
    'inputs': {
        'card': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 7
    },
    'output': 3
}

tests.append(test)

for test in tests:
    print(locate_card(test['inputs']['card'], test['inputs']['query']))
    print(locateCard(test['inputs']['card'], test['inputs']['query']))
    print(EvaluateTestCase(locate_card, test))

