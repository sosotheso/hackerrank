# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import *

io = input()
t= list(map(int,list(io)))
an_iterator = groupby(t)

for key,group in an_iterator:
    print('('+str(len(list(group)))+', '+str(key)+')', end=' ')
