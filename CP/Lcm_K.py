import math

def lcm_of_power_array(arr, m):
  lcm = arr[0]
  for i in arr:
    lcm = (lcm*i//math.gcd(lcm, i))
  return lcm%m

for _ in range(int(input())):
    n,m,k=map(int,input().split())
    arr=[i**k for i in list(map(int,input().split()))]
    print(lcm_of_power_array(arr, m))
