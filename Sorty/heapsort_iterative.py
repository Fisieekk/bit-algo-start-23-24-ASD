# DISCLAIMER
# Tego profesor Faliszewski nie omawiał raczej na wykładzie, więc nie można mieć tego kodu na kartce na kolokwiach i egzaminach


def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        i = largest
        return True
    return False

def heap_sort(arr):
    n = len(arr)

    for i in range(n//2 - 1, -1, -1):
        while heapify(arr, n, i):
            pass

    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        j = 0
        while heapify(arr, i, j):
            pass

arr = [12, 11, 13, 5, 6, 7]
heap_sort(arr)
print("Posortowana tablica:",arr)