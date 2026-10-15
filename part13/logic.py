# 논리연산
a = 10
if a < 0 and 2**a > 1000 and a%5 == 2 and round(a) == a:
    print("너무 복잡한 식이에요")

def return_false():
    print("함수 return_false")
    return False

def return_true():
    print("함수 return_true")
    return True

print("테스트1 시작")
a = return_false()
b = return_true()
if a and b:
    print(True)
else:
    print(False)

print("테스트2 시작")
if return_false() and return_true():
    print("True")
else:
    print(False)
# 테스트2 결과
# 테스트2 시작
# 함수 return_false <- 이렇게 나오는 이유는 "단락평가" 때문이다.
# - return_false() 부분이 False 이기때문에 이미 조건성립(참)이 안된다.
# - 그래서 어차피 결과는 False 이기때문에 return_true 는 출력되지 않는 것이다.
# False

# 단락평가란?
# - 논리연산에서 코드의 앞부분만 보고 이미 결과를 알 수 있는 경우, 뒤쪽은 보지 않고 값을 결정함