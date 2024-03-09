def left(i):
    return 2*i + 1
def right(i):
    return 2*i + 2
def parent(i):
    return (i-1)//2

def buildheap(T):
    n=len(T)
    for i in range(parent(n-1),-1,-1): #(n//2)-1,-1,-1
        heapify(T,i,n)

def heapify(T,i,n):
    l = left(i)
    r = right(i)
    max_ind=i
    print(T)
    if l < n and T[l] > T[max_ind]: #T[i]
        max_ind = l
    if r < n and T[r] > T[max_ind]:
        max_ind = r
    if max_ind != i:
        T[i],T[max_ind]=T[max_ind],T[i]
        heapify(T,max_ind,n)

def heapsort(T):
    n=len(T)
    buildheap(T)
    print("start")
    for i in range(n-1,0,-1):
        print("krok")
        T[0],T[i]=T[i],T[0]
        heapify(T,0,i)
from random import randint
t=[randint(1,10) for i in range(5)]
heapsort(t)
print(t)