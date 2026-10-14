# 딕셔너리와 반복문
# - 딕셔너리에서는 list 와 다르게 정해진 순서가 없기때문에 출력되는 순서가 매번 다름

ages = {
    # key:value
    'Tod':35,
    'Jane':23,
    'Paul':62
}

print(ages)

# for key in ages.keys():
#     print(key)

# 파이썬에서는 뒤에 .keys() 를 붙이지 않아도 기본적으로 가져오는 것으로 봄 -> 생략가능
# for key in ages.keys():
for key in ages:
    print('{}의 나이는 {}입니다.'.format(key, ages[key]))

# for value in ages.values():
#     print(value)

# key, value를 같이 가져오는 방법: items() 활용 / list의 enumerate 와 같은 역할이라고 보면됨
for key, value in ages.items():
    print('{}의 나이는 {}입니다.'.format(key, value))