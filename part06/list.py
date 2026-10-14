# 리스트 자료형
list1 = ['가위', '바위', '보']
list2 = [37, 23, 10, 33, 29, 40]

print(list1)
print(list2)

print(list1[1])
print(list1[2])
# print(list1[3]) # IndexError: list index out of range
print(list1[0]) # 첫번째 값

# 값 변경 (변수처럼 다루기)
list1[0] = '바위'
print(list1[0])
print(list1)

print(list1[-1]) # 여기서 -1 은 '뒤에서 첫번째' 라는 의미
print(list1[-3]) # 바위