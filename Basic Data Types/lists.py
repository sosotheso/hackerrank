import sys
import re

if __name__ == '__main__':
    N = int(input())
    my_list = []

    for i in range(0, N):
        t = sys.stdin.readline()
        if re.search("^insert", t):
            my_list.insert(int((t.split())[1]), int((t.split())[2]))
        elif re.search("^print", t):
            print(my_list)
        elif re.search("^remove", t):
            my_list.remove(int((t.split())[1]))
        elif re.search("^append", t):
            my_list.append(int((t.split())[1]))
        elif re.search("^sort", t):
            my_list.sort()
        elif re.search("^pop", t):
            my_list.pop(len(my_list) - 1)
        elif re.search("^reverse", t):
            my_list.reverse()
