n = input().split()

a = int(n[0])
b = int(n[1])
c = int(n[2])

if(a >= 2 and a <= 10000
   and b >= 2 and b <= 10000
   and c >= 2 and c <= 10000) :
    result1 = (a + b) % c
    result2 = (a % c +  b % c) % c
    result3 = (a * b) % c
    result4 = (a % c * b % c) % c
    print(result1)
    print(result2)
    print(result3)
    print(result4)

