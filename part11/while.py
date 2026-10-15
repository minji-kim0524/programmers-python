# while 반복문
# - if문은 조건이 맞을 때 한번만 실행
# - while문은 조건이 맞으면 계속 반복하여 실행함
# - for 반복문으로 작성한 코드는 while 반복문으로도 작성할 수 있음

# selected = None
# while selected not in ['가위', '바위', '보']:
#     selected = input('가위, 바위, 보 중에 선택하세요')

# print('선택된 값:', selected)

# for문과 while문 비교
# 아래 두 방법은 동일한 결과를 가져옴
patterns = ['가위', '보', '보']
length = len(patterns)
i = 0

# 방법1
for pattern in patterns:
    print(pattern)

# 방법2
while i < length:
    print(patterns[i])
    i = i + 1