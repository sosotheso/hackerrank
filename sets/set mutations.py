# Enter your code here. Read input from STDIN. Print output to STDOUT

nA = int(input())
A = set(map(int, input().split()))
nSets = int(input())

for i in range(1, nSets + 1):
    operation = input().split()
    oSet = set(map(int, input().split()))
    if operation[0] == 'intersection_update':
        A.intersection_update(oSet)
    elif operation[0] == 'symmetric_difference_update':
        A.symmetric_difference_update(oSet)
    elif operation[0] == 'difference_update':
        A.difference_update(oSet)
    else:
        A.update(oSet)

print(sum(A))

