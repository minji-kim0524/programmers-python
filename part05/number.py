# 숫자
five1 = 5
five2 = 5.0
five3 = 5.0000

print(five1)
print(five2) # 5.0
print(five3) # 5.0

five4 = 5 * 1
five5 = 5 * 1.0

print(five4) # 5
print(five5) # 5.0

div1 = 6 / 5
div2 = 6 // 5

print(div1) # 1.2
print(div2) # 1

a = 6
b = 5
print(a == b * (a // b) + (a % b)) # True

# 부동소수점: 파이썬에서 쓰는 실수 표현방법
#  - 정수보다 정확도가 떨어짐
print(0.1 + 0.1 == 0.2) # True
print(0.1 + 0.1 + 0.1 == 0.3) # False

print(int(5.0)) # 정수
print(float(5)) # 부동소수점
print(5 * 1.0) # 부동소수점
