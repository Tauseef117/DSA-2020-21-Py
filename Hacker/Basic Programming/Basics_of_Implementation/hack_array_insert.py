a, b = map(int, input().split())
arr=list(map(int, input().split()))
for k in range(b):
    p,q,r=map(int, input().split())
    if p==1:
        arr[q]=r
    elif p==2:
        print(sum(arr[q:r+1]))

