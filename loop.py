def factorial_loop(number):
    fact=1
    for i in  range(2, number+1):
        fact*=i
    return fact

def permute_loop(string):
    string = list(string)
    for p in range(factorial_loop(len(string))):
        print(''.join(string))
        i=len(string)-1
        while i>0 and string[i-1]>string[i]:
            i-=1
        string[i:]=reversed(string[i:])
        if i > 0:
            q=i
            while string[i-1]>string[q]:
                q+=1
            temp=string[i-1]
            string[i-1]=string[q]
            string[q]=temp

permute_loop("ABC")
