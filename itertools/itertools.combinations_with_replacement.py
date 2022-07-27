# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement
data = list(input().split())
result = list(combinations_with_replacement(sorted(list(data[0])),int(data[1])))
result2= list(map(lambda x: ''.join(x),result))
print(*result2, sep="\n")
