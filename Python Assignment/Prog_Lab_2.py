import math
def divisors(n):
    number_of_factors = 0
    a=int(math.ceil(math.sqrt(n)))
    for i in range(1,a ):
        if n % i == 0:
            number_of_factors += 2
        else:
            continue
    return number_of_factors

x=1
for y in range(2,1000000):
    x += y
    if divisors(x) >= 500:
     print(x)
     break