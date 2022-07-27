# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

ab = int(input())
bc = int(input())
ac = math.sqrt(ab**2 + bc **2)

bt = bc / 2
tc = bc / 2
mc = ac / 2
mt = math.sqrt(mc**2 - tc **2)

print(str(round(math.degrees(math.atan(mt/bt))))+chr(176))
