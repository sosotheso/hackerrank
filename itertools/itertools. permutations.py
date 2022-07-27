# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
data = list(input().split())
result = list(permutations(sorted(list(data[0])),int(data[1])))
result2= list(map(lambda x: ''.join(x),result))
print(*result2, sep="\n")
