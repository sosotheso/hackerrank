# Enter your code here. Read input from STDIN. Print output to STDOUT
A = set(map(int,input().split()))
n = int(input())

b= True

for i in range(1,n+1):
    oSet = set(map(int,input().split()))
    if not oSet.issubset(A):
        b = False

print(b)
