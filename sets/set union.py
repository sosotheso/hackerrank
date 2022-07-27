# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
nSet = set(map(int, input().split()))
m = int(input())
mSet = set(map(int, input().split()))

print(len(nSet.union(mSet)))
