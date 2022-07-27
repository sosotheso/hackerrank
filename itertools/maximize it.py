# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import *
kn = input().split()
k = int(kn[0])
n = int(kn[1])
s = list()
for j in range(0,k):
    line = input().split()
    line = line[1:]
    s.append(set(map(lambda x: (int(x)**2)% n,line)))

P = list(product(*s))
res = list(map(lambda x: sum(x) % n,P))
print(max(res))
