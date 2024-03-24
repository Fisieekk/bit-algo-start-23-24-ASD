import random

#dowolne sortowanie O(n^2)
def selsort(A):
    for i in range(len(A)):
        min_val = i
        for j in range(i,len(A)):
            if A[min_val] > A[j]:
                min_val = j
        A[i],A[min_val] = A[min_val], A[i]
    

def bucket_sort(T,sorting_function):
    n = T[0]
    l = len(T)
    for i in range(l):
        if T[i] > n:
            n = T[i]

    buckets = [[] for _ in range(l+1)]

    for x in T:
        i = ((x/n) *l)
        buckets[int(i)].append(x)
    
    result = []
    for bucket in buckets:
        if bucket:
            sorting_function(bucket) #selsort(bucket)
        for x in bucket:
            result.append(x)
    
    return result


def test_Sorted(A):
    for i in range(1,len(A)):
        if A[i] < A[i-1]:
            return False
    return True

A = [random.random() for _ in range(1_000_000)]
#print(A)

A = bucket_sort(A,selsort)

#print(A)
print(test_Sorted(A))


#[] -> false
            
