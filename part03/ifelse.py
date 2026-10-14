# if True:
#     pass #조건이 참일 때 실행
# else:
#     pass #조건이 거짓일 때 실행

SCISSOR = '가위'
ROCK = '바위'
PAPER = '보'

WIN = '이겼습니다.'
DRAW = '비겼습니다.'
LOSE = '졌습니다.'

mine = '가위'
yours = '바위'

# if mine == yours:
#     result = DRAW
# else: # 반드시 if문 뒤에 따라오고, 단독으로 사용할 수 없음
#     result = '이기거나 지거나'

# print(result)

#elif 문법: 파이썬에서는 else if를 줄여서 elif라고 표현함 (기능차이는 없음)

if mine == yours:
    result = DRAW
else:
    if mine == SCISSOR:
        if yours == ROCK:
            result = LOSE
        else:
            result = WIN
    elif mine == ROCK:
        if yours == PAPER:
            result = LOSE
        else:
            result = WIN
    elif mine == PAPER:
        if yours == SCISSOR:
            result = LOSE
        else:
            result = WIN
    else:
        print('잘못된 입력입니다.')

print(result)