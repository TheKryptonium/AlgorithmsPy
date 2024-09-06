array = [1,3,5,7,9,2,42,10,12,57]
array2 = [9,8,7,6,5,4,3,2,1]
A=[[1,3],[2,4]]
B=[[2,5],[3,9]]

#MERGING ALGORITHMS
def merging (A):
    mid= len(A)//2
    left = A[:mid]
    right = A[mid:]
    C=[]
    while(min(len(left), len(right))) > 0:
        if left[0] > right [0]:
            insert = right.pop(0)
            C.append(insert)
        elif left[0] <= right[0] :
            insert = left.pop(0)
            C.append(insert)
    if len(left) > 0:
        for i in left:
            C.append(i)
    if len(right) > 0:
        for i in right:
            C.append(i)
    return C

C = merging(array2)
print(C)

