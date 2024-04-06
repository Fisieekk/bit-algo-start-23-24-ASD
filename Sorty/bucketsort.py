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
    #wyznaczamy największy element
    n = T[0]
    l = len(T)
    for i in range(l):
        if T[i] > n:
            n = T[i]

    #tworzymy wiaderka
    buckets = [[] for _ in range(l+1)]

    #uzuepłniamy wiaderka wyznaczając indeksy wg wzoru 
    #i = (wartość/największa wartość) * długośc tablicy wejściowej
    for x in T:
        i = ((x/n) *l)
        buckets[int(i)].append(x)
    
    #ponowne składanie wyniku
    result = []
    for bucket in buckets:
        #jeżeli nie jest pusty (python traktuje [] jako fałsz)
        if bucket:
            #sort
            sorting_function(bucket) #alternatywnie: selsort(bucket)

        for x in bucket:
            #dodanie każdego elementu po kolei do wyniku
            result.append(x)

    #zwracamy [nie jest w miejscu ale oczywiście czyszcząc tablice T i
    #appendując do niej używamy referencji]
    return result

#funkcja testująca
def test_Sorted(A):
    for i in range(1,len(A)):
        if A[i] < A[i-1]:
            return False
    return True

#WYWOŁANIA 

A = [random.random() for _ in range(1_000_000)] 
#nie polecam printowania tablicy takiej wielkości heh
#print(A)

A = bucket_sort(A,selsort)

#print(A)
print(test_Sorted(A))


            
