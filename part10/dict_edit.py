# 딕셔너리 수정하기
dict = {
    'one':1,
    'two':2
}

print('수정 전', dict)
dict['one'] = 11 # 딕셔너리 값 수정
print('수정 후', dict)

# 딕셔너리에 새로운 값 추가
dict['three'] = 3
print('새로운 값 추가', dict)

# 딕셔너리 값 삭제
del (dict['two'])
print('값 삭제', dict)