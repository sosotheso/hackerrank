# Enter your code here. Read input from STDIN. Print output to STDOUT
n = input()
l = input().split()
any_res = any(list(map(lambda e: e == e[::-1], l)))
all_res = all(list(map(lambda e: int(e) > 0, l)))
print(any_res and all_res)
