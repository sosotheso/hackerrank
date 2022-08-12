# Enter your code here. Read input from STDIN. Print output to STDOUT
n, x = map(int,input().split())
l = []
for i in range(x):
    l.append(list(map(float,input().split())))
z = zip(*l)
k = list(map(lambda e: list(e),z))
res = list(map(lambda y: sum(y)/x, k))
print(*res,sep='\n')
