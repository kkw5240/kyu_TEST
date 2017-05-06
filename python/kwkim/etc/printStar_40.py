#   문제
#       한 행은 *로 이루어진 단어와, 단어와 단어 사이의 구분자 ' '만 존재한다.
#       한 행의 길이는 40자 이하이다.
#       한 행의 마지막에 (N)이 표시되어야 한다. N은 한 행의 글자 수(*, ' ' 포함)이다.
#   예시
#       * ***** ********* ** ******* **** ***   (37)
#       ***** *** ******** ** ***** ***         (31)
#       ********* ******* ******* ******* ***** (39)
#       ******** ******** *** * ***** ********  (38)

import random
n, linesize = 100, 40
sum = 0

rows = []
rnums = []

for i in range(n):
    rnums.append(random.randint(1,10))

for i in range(n):
    if rnums[i] + sum < 40:
        sum += rnums[i] + 1
        rows.append(str(rnums[i] * '*'))
    else:
        print("{0: <{1}}{2}".format(" ".join(rows), linesize, '('+str(sum - 1)+')'))
        rows = []
        sum = 0
