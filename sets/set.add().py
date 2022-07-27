# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    n = int(input())
    rSet = set()
    for i in range(1, n + 1):
        rSet.add(input())

    print(len(rSet))
