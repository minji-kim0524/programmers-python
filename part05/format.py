# 자료형
# 문자열을 원하는 모양으로 쉽게 바꾸기 (대괄호 이용하여 변수로 바꿀수 있음)

# 인사봇
number = 20
greeting = '안녕하세요'
place = '문자열 포맷의 세계'
welcome = '환영합니다'

# 방법 1 (old)
print(number, '번 손님', greeting, '.', place, '에 오신 것을', welcome, '!')

# 방법 2 (new)
base = '{}번 손님 {}. {}에 오신 것을 {}!'
new_way = base.format(number, greeting, place, welcome)

print(base)
print(new_way)

mine = '가위'
yours = '바위'
result = '졌다...'

print('나는 {}, 너는 {}, 그래서 {}'.format(mine, yours, result))

# format의 괄호 안 갯수보다 많은 인자를 넣으면 에러가 발생한다.