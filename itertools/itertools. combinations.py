# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
data = list(input().split())

for i in range(1,int(data[1])+1):
    result = list(combinations(sorted(list(data[0])),i))
    result2= list(map(lambda x: ''.join(x),result))
    print(*result2, sep="\n")
