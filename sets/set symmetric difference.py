# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
nSet = set(map(int,input().split()))

m = int(input())
mSet = set(map(int,input().split()))
rSet = (nSet.difference(mSet)).union(mSet.difference(nSet))
print(len(rSet))
