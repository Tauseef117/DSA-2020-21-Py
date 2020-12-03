def fib(n):
    if n==0 or n==1:
        return n
    else:
        return (fib(n-1) + fib(n-2))
a=int(input('Enter the number of terms in Fibbonacci '))
for i in range(a):
    print(fib(i))

#0 1 1 2 3