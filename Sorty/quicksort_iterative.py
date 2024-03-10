# DISCLAIMER
# Tego profesor Falsizewski nie omawiał raczej na wykładzie, więc nie można mieć tego kodu na kartce na kolokwiach i egzaminach


def quicksort(U,increasing = True):
    stack = [(0, len(U) - 1)]
    while stack:
        start, end = stack.pop()
        if end - start <= 0:
            continue
        pivot = U[start]
        i, j = start, end
        while i <= j:
            if increasing :
                while U[i] < pivot:
                    i += 1
                while U[j] > pivot:
                    j -= 1
            else :
                while U[i] > pivot:
                    i += 1
                while U[j] < pivot:
                    j -= 1
            
            if i <= j:
                U[i], U[j] = U[j], U[i]
                i += 1
                j -= 1
        if start < j:
            stack.append((start, j))
        if i < end:
            stack.append((i, end))
    return U

test = [8,14,370,39,599,812,99,98,45,2,10]

print(quicksort(test))