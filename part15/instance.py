# 인스턴스
# - 인스턴스란 클래스에 의해 생성된 객체
# - 클래스가 같더라도 각자 다른 값을 가질 수 있음

# `is` 연산: 비교대상이 서로 같은 "인스턴스"인지 확인가능
# `==` 연산: 비교대상이 같은 "값" 을 가지는지 확인가능
# 예) list1 = list("hello")
#    list2 = list("hello")
#    print(list1 == list) # True
#    print(list1 is list) # False

numbers1 = []
print(type(numbers1)) # <class 'list'>

characters = list("hello")
print(characters)
print(type(characters)) # <class 'list'>

# isinstance(a, b)
# - 2개의 인자를 받음
# - a: 대상
# - b: 확인하고자하는 타입

print(isinstance(numbers1, list)) # True

print(type(numbers1) == list) # True
