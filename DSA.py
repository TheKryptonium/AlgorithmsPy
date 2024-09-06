array = [1,3,5,7,9,2,42,10,12,57]
array2 = [9,8,7,6,5,4,3,2,1]

def separator():
    print('\n')
    print('***********************************************************')
    print('\n')

#LINEAR SEARCH
def linear(arr, target):
    for i in range(len(arr)):

        if arr[i]==target:
            return i


print("Result from linear research: {0}".format(linear(array, 10))) 

separator()

#BINARY SEARCH
def binary(arr, target,start, end):
    while start<=end:
        mid = (start+end)//2
        
        if arr[mid] < target:
            start = mid+1
        elif arr[mid] > target :
            end = mid-1
        else:
            return mid
    
    return start


def recursiveBinary(arr, target, start, end):
    if end >= start:

        mid = start + end - 1 // 2

        if arr[mid] < target :
            return recursiveBinary(arr, target, mid+1, end)
        elif arr[mid] > target :
            return recursiveBinary(arr, target, start, mid-1)
        else :
            return mid
    
    else :
        return -1


print("Iterative binary research: {0}".format(binary(array,10, 0, len(array)-1)))
print("Recursive binary research: {0}".format(recursiveBinary(array, 10, 0, len(array)-1)))

separator()

#SORTING ALGORITHMS
def bubbleSort(A):
    iterations = 0
    
    for i in range(len(A)):
        for j in range(len(A)-(i+1)):
            iterations+=1
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
    
    return iterations


def insertionSort(A):
    iterations = 0
    for j in range(1, len(A)):
        iterations+=1
        key = A[j]
        i = j-1
        while i>=0 and key < A[i] :
            A[i+1] = A[i]
            i-=1
        A[i+1] = key

    return iterations


iterations = bubbleSort(array)
iterates = insertionSort(array2)
print("Array after sorting: {0} and the number of iterations: {1}".format(array, iterations)) 
print("Array after using the insertion sort algorithm: {0}, number of iterations: {1}".format(array2, iterates))

separator()

#LINKED-LISTS
class Node:
    def __init__(self, data):
        print('New head...')
        self.data = data
        self.next = None


class linkedList :
    def __init__(self, head):
        self.head = head
    
    def traversal(self):
        first = self.head
        
        while first:
            print(first.data)
            first = first.next

    def insertHead(self, data):
        new = Node(data)
        new.next = self.head
        self.head = new
    
    def search(self, x):
        print('Searching...')
        temp  = self.head
        
        while temp is not None:
            if temp.data == x:
                return True
            temp = temp.next
        else:
            return False 

    def deleteNode(self, data) :
        print('Deleting a node...')
        temp = self.head 

        while temp is not None:
            if temp.data == data:
                break
            prev = temp
            temp = temp.next
        
        prev.next = temp.next
    
    def deleteTail(self):
        print("Deleting the tail...")
        temp = self.head
        
        while temp.next.next is not None:
            temp = temp.next
        
        temp.next = None



father = Node("Bob")
wife = Node("Amy")
firstKid = Node("Max")
secondKid = Node("Jenny")

father.next = wife
wife.next = firstKid
firstKid.next = secondKid

family = linkedList(father)

print("Family members: ")
family.traversal()

family.insertHead('Patrick')
print("Family members: ")
family.traversal()

print(family.search('Max'))

family.deleteNode('Bob')
family.traversal()

family.deleteTail()
family.traversal()