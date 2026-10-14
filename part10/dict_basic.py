# 딕셔너리 만들기
# 딕셔너리(Dictionary)란?
# - 여러 값을 저장해두고 필요한 값을 꺼내 쓰는 기능
# - 이름표를 이용하여 값을 꺼내서 사용
# - 딕셔너리명 = {
#     '이름표1':'값1',
#     '이름표2':'값2'
# }
wintable = {
    # 디기셔너리는 이름:값 의 형태로 되어있음
    '가위':'보',
    '바위':'가위',
    '보':'가위'
}
print(wintable['가위'])

def rsp(mine, yours):
    if mine == yours:
        return 'draw'
    elif wintable[mine] == yours:
        return 'win'
    else:
        return 'lose'
    
result = rsp('가위', '바위')
print(result)

messages = {
    'win':'이겼다!',
    'draw':'비겼네',
    'lose':'아 졌어...'
}

print(messages[result])