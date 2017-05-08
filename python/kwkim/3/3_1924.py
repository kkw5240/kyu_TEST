#   2007년
#   문제
#       오늘은 2007년 1월 1일 월요일이다. 그렇다면 2007년 x월 y일은 무슨 요일일까? 이를 알아내는 프로그램을 작성하시오.
#   입력
#       첫째 줄에 빈 칸을 사이에 두고 x(1≤x≤12)와 y(1≤y≤31)이 주어진다. 참고로 2007년에는 1, 3, 5, 7, 8, 10, 12월은 31일까지, 4, 6, 9, 11월은 30일까지, 2월은 28일까지 있다.
#   출력
#       첫째 줄에 x월 y일이 무슨 요일인지에 따라 SUN, MON, TUE, WED, THU, FRI, SAT중 하나를 출력한다.

def getDayOfWeek(d):
    dayMap = {
        0: "MON",
        1: "TUE",
        2: "WED",
        3: "THU",
        4: "FRI",
        5: "SAT",
        6: "SUN"
    }
    return dayMap[d % 7]

def dayOfMonth(m):
    sumDay = 0
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    for i in range(m):
        sumDay += int(days[i])

    return sumDay

date = input().split(' ')
x, y = int(date[0]), int(date[1])

while (x<1 or x>12) or (y<1 or y>31):
    date = input().split(' ')
    x, y = int(date[0]), int(date[1])

monSub = x - 1
daySub = y - 1

print(getDayOfWeek(dayOfMonth(monSub)+daySub))