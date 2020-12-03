def prime_factors(n):
    i=2
    factors=[]
    while i*i<=n:
        if n%i:
            i+=1
        else:
            n //= i
            factors.append(i)
    if n>1:
        factors.append(n)
    return print(*factors)
n=int(input('Enter number '))
prime_factors(n)