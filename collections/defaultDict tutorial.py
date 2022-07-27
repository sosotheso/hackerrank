# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

nm = input().split()
n = int(nm[0])
m = int(nm[1])
# print(n)
d = defaultdict(list)
for i in range(1, n + 1):
    d[input()].append(i)

for i in range(1, m + 1):
    c = input()
    if not d[c]:
        print(-1)
    else:
        print(*d[c], sep=' ')

