# Enter your code here. Read input from STDIN. Print output to STDOUT
nm = list(map(int, input().split()))
n = nm[0]
m = nm[1]
arr = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))

arr = sorted(arr)
l = len(arr)
hppy = 0
i = 0

while i < l:
    a = arr[i]
    c = 1
    i = i + 1
    while i < l:
        if arr[i] != a:
            break
        c = c + 1
        i = i + 1
    if a in A:
        hppy = hppy + (1 * c)
    elif a in B:
        hppy = hppy - (1 * c)

print(hppy)
