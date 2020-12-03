d=int(input())
toffee=0
for i in range(d):
    r , x=input().split()
    capacity=int(x)*100
    radius=2*(22/7)*int(r)
    if capacity>=radius:
        toffee+=1
print(toffee)