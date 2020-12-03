def solve(A, N):
# Write your code here
    sub_range=2**(N-1)
    sum=0
    for i in A:
        if i>=sub_range:
            sum=sum+i
            sum=sum%(10**9+7)
    return sum

T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    out_ = solve(A, N)
    print(out_)