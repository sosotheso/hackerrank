# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

n = int(input())
enList = list(input().split())
k = int(input())
# get list of indexes of 'a' in k
i=0
l=len(enList)
iSet =set()
for i in range(0,l):
    if enList[i]=='a':
        iSet.add(i+1)



#all possible tuples
tuples = list(combinations(range(1,n+1),k))

#convert tuples to sets
Sets = list(map(set,tuples))
l1 = len(Sets)

# remove element from Sets where element intersection iSet is empty
nSets = list(filter(lambda x: (x.intersection(iSet)!= set()) ,Sets))
l2 = len(nSets)

# Probability
print (l2/l1)
