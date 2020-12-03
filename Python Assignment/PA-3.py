def rotate_list(ll, step):
    l = len(ll)
    step %= l
    ans = ll[l - step:] + ll[:l - step]
    return ans

print(rotate_list([1,2,3,4,5],1))
print(rotate_list([1,2,3,4,5],3))
print(rotate_list([1,2,3,4,5],12))
