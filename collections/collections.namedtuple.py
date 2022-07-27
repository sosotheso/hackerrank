# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple

N = int(input())
columns = input().split()
SumMarks = 0
student = namedtuple('student', columns)
for i in range(1, N + 1):
    st = student(*(input().split()))
    SumMarks = SumMarks + int(st.MARKS)
print(SumMarks / N)

