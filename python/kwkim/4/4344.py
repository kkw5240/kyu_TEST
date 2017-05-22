#   평균은 넘겠지
#   문제
#     대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 당신은 그들에게 슬픈 진실을 알려줘야 한다.
#   입력
#     첫째 줄에는 테스트케이스 C가 주어진다.
#     둘째 줄부터 각 테스트케이스 마다 첫 수로 정수 N(1 <= N <= 1000)명의 학생이 주어지고 그 다음으로 N명의 0부터 100 사이의 점수가 이어서 주어진다.
#   출력
#     각 케이스마다 한줄씩 평균을 넘는 학생들의 비율을 소수점 넷째자리에서 반올림하여 출력한다.

totalNum = 0
totalSum = 0
mean = 0

c = int(input())

testCase = []
for i in range(c):
    testCase.append(input().split(' '))

meanArr = []
for i in range(c):
    totalSum = 0
    n = int(testCase[i][0])
    for j in range(n):
        totalSum += int(testCase[i][j+1])
    meanArr.append(totalSum/n)

for i in range(c):
    n = int(testCase[i][0])
    cnt = 0
    for j in range(n):
        if int(testCase[i][j+1]) > meanArr[i]:
            cnt += 1
    print("{0:.3f}%".format(round(cnt/n*100, 4)))




# totalNum = 0
# totalSum = 0
# mean = 0
#
# c = int(input())
#
# testCase = []
# for i in range(c):
#     testCase.append(input().split(' '))
#
# print(testCase)
#
# for i in range(c):
#     for j in range(int(testCase[i][0])):
#         totalNum += 1
#         totalSum += int(testCase[i][j+1])
#
# mean = totalSum / totalNum
# print(mean)
#
# for i in range(c):
#     n = int(testCase[i][0])
#     cnt = 0
#     for j in range(n):
#         if int(testCase[i][j+1]) >= mean:
#             cnt += 1
#     print("{:.3f}".format(round(cnt/n*100, 4)))