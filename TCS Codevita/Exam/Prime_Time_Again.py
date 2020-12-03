def get_prime_array(d):
    prime_array=list()
    prime=[i for i in range(d+1)]
    prime[0],prime[1]=0,0
    for i in range(2,d+1):
        if prime[i]==0:
            continue
        for j in range(i**2,d+1,i):
            prime[j]=0
    for i in range(2,d+1):
        if prime[i]!=0:
            prime_array.append(prime[i])
    return prime_array

d,p=map(int,input().split())
part_hours= d / p
arr=get_prime_array(d)
count_no_of_hrs_in_part=0

for i in arr:
    if i<=part_hours:
        count_no_of_hrs_in_part+=1
    else:
        break

prime_time_array=[[0 for i in range(p)] for j in range(count_no_of_hrs_in_part)]
for i in range(count_no_of_hrs_in_part):
    prime_time_array[i][0]=arr[i]
    for j in range(1,p):
        prime_time_array[i][j]=(int(prime_time_array[i][j-1] + part_hours) if (prime_time_array[i][j - 1] + part_hours) in arr else 0)

for i in prime_time_array:
    if i.count(0)>=1:
        count_no_of_hrs_in_part-=1
print(count_no_of_hrs_in_part, end="")
