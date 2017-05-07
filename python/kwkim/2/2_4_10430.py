#   나머지
#   문제
#       (A×B)%C는 (A%C × B%C)%C 와 같을까?
#       세 수 A, B, C가 주어졌을 때, 위의 네가지 값을 구하는 프로그램을 작성하시오.
#   입력
#       첫째 줄에 A, B, C가 순서대로 주어진다. (2 ≤ A, B, C ≤ 10000)
#   출력
#       첫째 줄에 (A+B)%C, 둘째 줄에 (A%C + B%C)%C, 셋째 줄에 (A×B)%C, 넷째 줄에 (A%C × B%C)%C를 출력한다.

A, B, C = input().split()

result = (int(A) + int(B)) % int(C)
print(result)

result = (int(A) % int(C) + int(B) % int(C)) % int(C)
print(result)

result = (int(A) * int(B)) % int(C)
print(result)

result = (int(A) % int(C) * int(B) % int(C)) % int(C)
print(result)