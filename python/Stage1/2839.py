inputN = input()
n= int(inputN)
temp = n
temp2 = 0

x = 5
y = 3
forCnt = 0
xCnt = 0
yCnt = 0

result = 0;

if(n >= 3 and n <= 5000 ) :
    forCnt = int(n / x)

    for i in range(forCnt, -1, -1) :
        temp = n - (x *  i)

        yCnt =  int(temp / y)
        temp2 = temp % y

        if(temp2 == 0) :
            xCnt = i
            result = xCnt +  yCnt
            print(result)
            break

    if(result == 0) :
        print(-1)
else :
    print(-1)