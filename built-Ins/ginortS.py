# Enter your code here. Read input from STDIN. Print output to STDOUT
s = list(input())
res = [[], [], [], []]
for e in s:
    if e.isdigit():
        if int(e) % 2 == 1:
            res[2].append(e)
        else:
            res[3].append(e)
    else:
        if e.islower():
            res[0].append(e)
        else:
            res[1].append(e)

res = list(map(lambda e: sorted(e), res))
result = ''
for e in res:
    result = result + ''.join(e)
print(result)
