import re

s = input().split()

x = s[0]
y = s[1]

reg = re.compile("[1-9]+")
r1 = reg.match(x)
reg1 = re.compile("[0][1-9]")
r2 = reg.match(y)

if(r1 and r2) :
    x1 = int(x)
    y1 = int(y)
    if (x1 > 0 and  y1 < 10) :
        print(x1/y1)
    else :
        print("")
else :
    print("")

