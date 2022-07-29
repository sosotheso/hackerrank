# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

t = int(input())
for i in range(1, t + 1):
    l = int(input())
    dq = deque(map(int, input().split()))
    b = 'Yes'
    left = dq[0]
    right = dq[l - 1]
    if left >= right:
        old = dq.popleft()
    else:
        old = dq.pop()
    l = l - 1
    while l != 0:
        left = dq[0]
        right = dq[l - 1]
        if max(left, right) > old:
            b = 'No'
            break
        if left >= right:
            old = dq.popleft()
        else:
            old = dq.pop()
        l = l - 1
    print(b)

