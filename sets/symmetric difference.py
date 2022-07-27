# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    mSize = int(input())
    mSet = set(list(map(int, input().split())))
    nSize = int(input())
    nSet = set(list(map(int, input().split())))
    rSet = (nSet.difference(mSet)).union(mSet.difference(nSet))
    rList = list(rSet)
    rList.sort()
    print(*rList, sep="\n")


