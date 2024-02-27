def mul_rec(m,n):
    if n == 1:
        return m
    else:
        return m + mul_rec(m ,n - 1)
    
def hailstone(n):
    if n == 1:
        print(1)
        return 1
    elif n % 2 == 0:
        print(n)
        return 1+hailstone(n//2)
    elif n % 2 == 1:
        print(n)
        return 1+hailstone(n * 3 + 1)

def merge(n1,n2):
    """ Merges two numbers
    >>> merge(31, 42)
    4321
    >>> merge(21, 0)
    21
    >>> merge (21, 31)
    3211
    """
    if n1 == 0:
        return n2
    elif n2 == 0:
        return n1
    elif n1 % 10 < n2 % 10:
        return merge(n1 // 10, n2) * 10 + n1 % 10
    else:
        return merge(n1, n2 // 10) * 10 + n2 % 10

def is_prime(n):
    def prime_helper(k):
        if n == k:
            return True
        elif n % k == 0 or n == 1:
            return False
        else: 
            return prime_helper(k + 1)
    return prime_helper(2)