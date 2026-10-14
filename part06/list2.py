# 리스트 수정
list2 = [37, 23, 10, 33, 29, 40]
print(list2)

# 리스트에 새로운 값 추가하기
# 방법 1
# - 기존 리스트 변경
# list2.append(16)
# print(list2) # [37, 23, 10, 33, 29, 40, 16]

# 방법 2
# - 새 리스트 생성
list3 = list2 + [16]
print(list3) # [37, 23, 10, 33, 29, 40, 16]

list4 = list2 + list3
print(list4)

# 리스트 값 포함여부 확인방법
# in 연산자 활용
# - 결과가 boolean 값으로 나옴 -> if문 활용에 좋음
n = 12
ownership = n in list3
print(ownership)

n = 10
if n in list3:
    print('{}은 있어!'.format(n))

# 리스트에서 값 지우기
# 방법1. del
# - 특정 위치를 지정시, 해당 위치의 값이 지워짐
print(list4)
# del list4[12]
del(list4[12]) # 위와 동일
print(list4)

# 방법2. remove
# - 특정 값을 지정하여 리스트 내 첫번째로 등장하는 해당 값 지우기
list4.remove(40)
print(list4)