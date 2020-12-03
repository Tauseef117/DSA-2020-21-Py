def digit_sum(n):
    if len(str(n))==1:
        return n
    return n%10 + digit_sum(n//10)

print(digit_sum(6633))

def digit_sum(n):
    if n==0 or n==1:
        return n
    else:
        a=n%10
        n=n//10
        return a + digit_sum(n)

print(digit_sum(6633))