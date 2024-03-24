def counting_sort(U) :
    minimum = min(U)
    k = max(U) - minimum + 1
    count = [0]*k
    
    for element in U :
        count[element - minimum] += 1
    
    res = []
    
    for i in range(k) :
        res += [i + minimum]*count[i]
    
    return res

arr = [7, 2, 1, 6, 8, 5, 3, 4]
counting_sort(arr)
print(arr)