# DISCLAIMER
# Tego profesor Faliszewski nie omawiał raczej na wykładzie, więc nie można mieć tego kodu na kartce na kolokwiach i egzaminach


def quickselect(U,s,increasing = True):
    if not increasing :
        s -= 1
    start, end = 0, len(U) - 1
    while start < end:
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
        if s <= j :
            end = j
        elif s >= i :
            start = i
        else :
            return U[s]
    return U[start]

test = [8,14,370,39,599,812,99,98,45,2,10]

print(quickselect(test,2,False))