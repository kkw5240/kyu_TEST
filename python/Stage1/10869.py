import re
import math

s = input().split()

x = s[0]
y = s[1]

x1 = int(x)
y1 = int(y)

if ( x1 > 0 and  x1 <= 10000 and  y1 > 0 and y1 <= 10000) :
    print(x1+y1)
    print(x1-y1)
    print(x1*y1)
    print(math.floor(x1/y1))
    print(x1%y1)

