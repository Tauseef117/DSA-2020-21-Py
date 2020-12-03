if __name__ == '__main__':
    a=[]
    for _ in range(int(input())):
        arr=[]
        arr=list(map(str,input().split()))
        query=arr[0]
        if query=='insert':
            x=int(arr[1])
            y=int(arr[2])
            a.insert(x,y)
        elif query=='print':
            print(a)
        elif query=='append':
            x=int(arr[1])
            a.append(x)
        elif query=='remove':
            x=int(arr[1])
            a.remove(x)
        elif query=='sort':
            a=a.sort()
        elif query=='pop':
            a.pop()
        elif query=='reverse':
            a.reverse()
