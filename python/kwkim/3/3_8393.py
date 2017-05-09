#   합
#   문제
#       n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.
#   입력
#       첫째 줄에 n (1 ≤ n ≤ 10,000)이 주어진다.
#   출력
#       1부터 n까지 합을 출력한다.

totalSum = 0

n = int(input())
while n < 0 or n > 100000:
    n = int(input())

for i in range(n):
    totalSum += (i+1)

print(totalSum)