def con_sum(ar):
    if len(ar)==0:
        return 0

    max_sum=cur_sum=ar[0]
    for num in ar[1:]:
        cur_sum=max(cur_sum+num,num)
        max_sum=max(max_sum,cur_sum)
    return max_sum

print(con_sum([-1,-1,10,10]))

