def pair_sum(arr,k):
    if len(arr)<2:
        print('Not Possible')
    else:
        #Sets for tracking
        seen=set()
        output=set()
        for num in arr:
            target=k-num
            if target not in seen:
                seen.add(num)
            else:
                output.add((min(num,target),max(num,target)))
        print('\n'.join(map(str,list(output))))

pair_sum([1,3,2,2],4)