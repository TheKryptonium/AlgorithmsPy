def nthUgly(n):

    Ugly = [0]*n
    Ugly[0] = 1
    
    u2=u3=u5=0

    multiple2 = 2
    multiple3 = 3
    multiple5 = 5

    for i in range(1,n):

        Ugly[i]=min(multiple2, multiple3, multiple5)

        if Ugly[i] == multiple2:
            u2+=1
            multiple2 = Ugly[u2] * 2
        
        if Ugly[i] == multiple3:
            u3+=1
            multiple3 = Ugly[u3] * 3
        
        if Ugly[i] == multiple5:
            u5+=1
            multiple5 = Ugly[u5] * 5
        
    return Ugly[n-1]


n=15
print('The {0}th ugly number is: {1}'.format(n, nthUgly(n)))


