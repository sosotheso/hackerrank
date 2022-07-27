# Enter your code here. Read input from STDIN. Print output to STDOUT

n= int(input())

for i in range(1,n+1):
    nA= int(input())
    A = set(map(int,input().split()))
    nB= int(input())
    B = set(map(int,input().split()))
    print(A.issubset(B))
