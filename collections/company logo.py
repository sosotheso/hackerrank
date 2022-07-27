from collections import Counter, OrderedDict, deque, defaultdict

entry = input()
l = list(entry)
c = Counter(l)
d = dict(c)
resDict = defaultdict(list)
for key, val in d.items():
    # print(key, sorted(list(group)))
    resDict[val].append(key)

resOrderDict = OrderedDict(sorted(resDict.items()))
cpt = 3
resList = deque()
while (cpt > 0):
    mx = max(resOrderDict)
    for i in sorted(resOrderDict[mx]):
        if cpt == 0:
            break
        resList.append((i, mx))
        cpt -= 1
    del (resOrderDict[mx])

for e in resList:
    print(e[0],e[1])
