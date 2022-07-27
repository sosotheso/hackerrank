# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath
z = complex(input())
r = z.real
i = z.imag

print(abs(complex(r,i)))
print(cmath.phase(complex(r,i)))
