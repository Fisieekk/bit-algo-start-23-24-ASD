# DISCLAIMER
# Tego profesor Falsizewski nie omawiał raczej na wykładzie, więc nie można mieć tego kodu na kartce na kolokwiach i egzaminach


def merge_sort(arr,increasing = True):
    current_size = 1
    n = len(arr)
    while current_size < n:
        left = 0
        while left < n - 1:
            mid = min((left + current_size - 1), (n-1))
            right = ((2 * current_size + left - 1, n-1)[2 * current_size + left - 1 > n-1])
            merge(arr, left, mid, right,increasing)
            left += current_size * 2
        current_size *= 2
    return arr

def merge(arr, left, mid, right,increasing = True):
    n1 = mid - left + 1
    n2 = right - mid
    L = [0] * n1
    R = [0] * n2
    for i in range(n1):
        L[i] = arr[left + i]
    for j in range(n2):
        R[j] = arr[mid + j + 1]
    i = j = 0
    k = left
    while i < n1 and j < n2:
        #<= -> malejąco, >= -> rosnąco
        if not increasing :
            if L[i] >= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
        if increasing :
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
        k += 1
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

test = [8,14,370,39,599,812,99,98,45,2,10]

print(merge_sort(test))