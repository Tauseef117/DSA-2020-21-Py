#Recursively
#The recursive solution is exponential time Big - O, with O(2 ^ n).However, its a very simple and basic implementation to consider:

def fib_rec(n):
    # Base Case
    if n == 0 or n == 1:
        return n

    # Recursion
    else:
        return fib_rec(n - 1) + fib_rec(n - 2)
fib_rec(10)



#Dynamically
# Instantiate Cache information
n = 10
cache = [None] * (n + 1)

def fib_dyn(n):
    # Base Case
    if n == 0 or n == 1:
        return n

    # Check cache
    if cache[n] != None:
        return cache[n]

    # Keep setting cache
    cache[n] = fib_dyn(n - 1) + fib_dyn(n - 2)

    return cache[n]
fib_dyn(10)


#Iteratively
def fib_iter(n):
    # Set starting point
    a = 0
    b = 1

    # Follow algorithm
    for i in range(n):
        a, b = b, a + b

    return a


fib_iter(23)