#   별찍기 - 3
#   문제
#       첫째 줄에는 별 N개, 둘째 줄에는 별 N-1개, ..., N번째 줄에는 별 1개를 찍는 문제
#   입력
#       첫째 줄에 N (1<=N<=100)이 주어진다.
#   출력
#       첫째 줄부터 N번째 줄 까지 차례대로 별을 출력한다.

N = int(input())
while N < 1 or N > 100:
    N = int(input())

for i in range(N):
    print((N-i)*'*')