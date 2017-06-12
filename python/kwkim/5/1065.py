# 문제
#   어떤 양의 정수 X의 자리수가 등차수열을 이룬다면, 그 수를 한수라고 한다.
#   등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다.
#   N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오.
# 입력
#   첫째 줄에 1,000보다 작거나 같은 자연수 N이 주어진다.
# 출력
#   첫째 줄에 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력한다.


def arithmetic_sequence(n):
    str_n = str(n)
    pre = 0
    if len(str_n) < 3:
        return 1
    for i in range(len(str_n)):
        now = int(str_n[i]) - int(str_n[i-1])
        if i > 1:
            if pre != now:
                return 0
            else:
                pre = now
        else:
            pre = now
    return 1


c = 0
n = input()
for i in range(1, int(n)+1):
    c += arithmetic_sequence(i)

print('{0:} : {1:}'.format(i, c))



    # pre = 0
    # str_n = str(n)
    # p_sub = 0
    #
    # for i in range(len(str_n)):
    #     print('')
    #     print('pre: {:}'.format(pre))
    #     print('p_sub: {:}'.format(p_sub))
    #     now = int(str_n[i])
    #     print('now: {:}'.format(now))
    #     n_sub = now - pre
    #     print('n_sub: {:}'.format(n_sub))
    #     pre = now
    #
    #     if i != 0 and p_sub != n_sub:
    #         return 0
    #     else:
    #         p_sub = n_sub
    #         print(str_n)

#     return 1
#
#
# n = input()
# cnt = 0
#
# print(arithmetic_sequence(n))

# for i in range(int(n)):
#     print(i)
#     if i > 0:
#         cnt += arithmetic_sequence(i)

# print('=================================')
# print(cnt)

