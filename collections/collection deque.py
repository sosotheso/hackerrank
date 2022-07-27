# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
n = int(input())
d = deque()
for i in range(1,n+1):
    method = input().split()
    if method[0]=='append':
        d.append(method[1])
    elif method[0]== 'appendleft':
        d.appendleft(method[1])
    elif method[0]=='pop' :
        d.pop()
    else:
        d.popleft()
print(*d, sep=' ')
