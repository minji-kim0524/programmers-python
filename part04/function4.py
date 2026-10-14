# 함수의 값
# def add_10(value):
#     """value에 10을 더한 값을 반환하는 함수"""
#     print('return 앞')
#     return 10 # 즉시 종료됨
#     print('return 뒤')
#     result = value + 10
#     return result # return은 함수가 실행결과로 값을 갖도록 함

def add_10(value):
    """value에 10을 더한 값을 반환하는 함수"""
    if value < 10:
        return 10
    else:
        result = value + 10
        return result

# return 은 실행되는 즉시 함수를 종료하고, 그 값을 호출한 곳으로 반환함
# 하나의 함수안에 return 문이 여러개 있을 수 있음
# 여러개의 return 문이 있을 경우, 조건에 따라 실행되는 return 문이 달라질 수 있음
# 단, 특별한 조건이 없을 경우 먼저 나온 return 문이 실행됨

n = add_10(5)
print(n)

n = add_10(42)
print(n)