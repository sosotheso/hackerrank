# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
n = int(input())
d = OrderedDict()
for i in range(1,n+1):
    word = (input())
    if word in d:
        d[word] = d[word] + 1
    else:
        d[word] = 1
print(len(d))
print(*d.values(), sep=' ')
