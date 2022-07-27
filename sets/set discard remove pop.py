n = int(input())
s = set(map(int, input().split()))
N = int(input())
for i in range(1, N + 1):
    command = input().split()
    if command[0] == 'pop':
        if len(s) > 0:
            s.pop()
    else:
        s.discard(int(command[1]))

print(sum(s))

