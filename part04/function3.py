# 매개변수와 실행인자
# - 매개변수: 정의에서 사용하는 이름
# - 실행인자: 함수를 호출할 때 전달하는 값
# - 매개변수와 실행인자의 개수와 순서는 일치해야 함 (여러개 일때는 쉼표로 구분)
def print_root(a, b, c): # a, b, c는 매개변수(parameter) 
    r1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    r2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)

    print('해는 {} 또는 {}입니다.'.format(r1, r2))

x = 1
y = 2
z = -8

print_root(x, y, z) # x, y, z는 실행인자(argument)

x = 2
y = -6
z = -8

print_root(x, y, z)

def print_round(number):
    rounded = round(number)
    print(rounded)

print_round(4.6)
print_round(2.2)
print_round(3.7)