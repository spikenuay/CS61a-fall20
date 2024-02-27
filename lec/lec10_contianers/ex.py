def sum_below(n):
    total  = 0
    for i in range(n + 1):
        total += i
        print('total = ', total)
        print('i =',i)
    return total

def my_sum(L):
    if L == []:
        return 0
    else:
        return L[0] + my_sum(L[1:])
    
def sum_iterative(n):
    total = 0
    a = list(range(n + 1))
    while a != []:
        total += a[0]
        a = a[1:]
    return total

def sum_recursive(n):
    a = list(range(n + 1))
    def sum_helper(L):
        if L == []:
            return 0
        else:
            return L[0] + sum_helper(L[1:])
    return sum_helper(a)




