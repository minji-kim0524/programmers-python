# 길이가 1~10까지인 정사가각형의 넓이를 요소로 가지는 리스트 만들기
# 기본구조
areas = []
for i in range(1, 11):
    areas = areas + [i*i]
print("첫번째 방법",areas)

# 조건추가
areas1 = []
for i in range(1, 11):
    if i % 2 == 0:
        areas1 = areas1 + [i*i]
print("조건적용1:",areas1)


# 리스트 컴프리헨션 (List Comprehension) 방식 적용
# - 기본구조: [표현식 for 변수 in 반복가능객체]
areas2 = [i*i for i in range(1,11)]
print("두번째 방법",areas2)

# - 조건문추가: [표현식 for 변수 in 반복가능객체 if 조건문]
areas3 = [i*i for i in range(1,11) if i % 2 == 0]
print("조건적용2:",areas3)

# - for문 중첩
tuple1 = [(x,y) for x in range(15) for y in range(15)]
print(tuple1)
