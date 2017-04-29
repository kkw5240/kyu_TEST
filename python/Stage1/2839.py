import math

n = input()
x = 3
y = 5
temp  = 0
temp2 = 0

n1 = int(n)

if(n1 >= 3 and n1 <= 5000 ) :
    temp = int(n1 / y)
    n1 = n1 - (y * temp)
    temp2 =  (n1 / x)
    if(temp2 == math.floor(temp2)) :
        temp = int(temp) +  int(temp2)
        print(temp)
    else :
        print("-1")
else :
    print("")
