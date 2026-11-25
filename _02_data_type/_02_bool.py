""" boolean과 조건 조합

- 불리언은 참/거짓을 나타냄.

- python에서는 "bool"이라고 표현

- 참(true), 거짓(False)

- 주로 조건에 따른 코드 분기에 많이 사용
"""

is_true = True
is_false = False

print("is_true: ", is_true, type(is_true))
print("is_false: ", is_false, type(is_false))

# 비교 연산자
# >, <, ==, >=, <=, !=

print("1 > 0.5:", 1 > 0.5) # True
print("1 < 0.5:", 1 < 0.5) # False
print("1 >= 0.5:", 1 >= 0.5) # True
print("1 <= 0.5:", 1 <= 0.5) # False
print("1 == 1:", 1 == 1) # True
print("1 != 1:", 1 != 1) # False

# 논리 부정 연산자 (! => not)
print(True)
print(not True)

# 논리 연산자: and, or

# and 연산자
# - 좌항과 우항이 모두 참(True)일 때만 참



# or 연산자
# - 좌항과 우항이 모두 거짓(False)일 때만 거짓

print("100 > 0 or 1 == 1:", 100 > 0 or 1 == 1) 
print("10 * 10 == 100 or 1 != 1:", 10 * 10 == 100 or 1 != 1)
print("100 == 0 or 10 == 10:", 100 == 0 or 10 == 10)
print("100 - 1000 > 0 or 23 != 20 + 3:", 100 - 1000 > 0 or 23 != 20 + 3) 


print("--- 합격 또는 불합격 여부 판별하기 ---")
# 조건: 각 과목 점수가 40점 이상, 평균 60점 이상만 True, 나머진 False

kor = 70
eng = 50

result = kor >= 40 and eng >= 40 and (kor + eng) / 2 >= 60

print("합격 여부: ", result)

print ("합격" if result else '불합격')

# 논리 연산자(not, and, or), 비교 연산자(>, <, ==, >=, <=, !=)의 결과는
# 항상 자료형이 bool이다







