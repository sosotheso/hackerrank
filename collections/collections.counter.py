# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
x = int(input())
shoes = list(map(int,input().split()))
shoesCollection= Counter(shoes)
n = int(input())
total = 0
for i in range(1,n+1):
    purshase = list(map(int, input().split()))
    sh= purshase[0]
    xi = purshase[1]
    t = shoesCollection[sh]
    if t != 0:
        total = total + xi
        shoesCollection[sh] = t - 1

print(total)
