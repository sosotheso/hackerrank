# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

n = int(input())
d = OrderedDict()

for i in range(1, n + 1):
    s = input().split()
    l = len(s)
    item_name = ' '.join(s[:l - 1])
    price = int(s[l - 1])
    if item_name in d:
        d[item_name] = d[item_name] + price
    else:
        d[item_name] = price

for i in d:
    print(i, d[i])

