# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
t = int(input())
for i in range(t):
    try:
        re.compile(input())
        print('True')
    except re.error:
        print('False')