def kadane(arr):
    max_current,max_global=arr[0],arr[0]
    for i in range(1,len(arr)):
        max_current=max(arr[i] , arr[i]+max_current)
        if max_current>max_global:
            max_global = max_current
    return max_global

ar=[-2,3,2,-1]
print(kadane(ar))
