# 인스턴스

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
