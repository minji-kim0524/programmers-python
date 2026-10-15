# bool
# true, false
# - 숫자 0을 제외한 모든 수 => true
# - 빈 딕셔너리, 빈 리스트를 제외한 모든 딕셔너리, 리스트 => true
# - 아무 값도 없다는 의미인 None => false
# - 빈문자열을 제외한 모든 문자열 => true

value = input('내용을 입력해주세요') or '아무 내용도 입력받지 못했습니다.'
print('입력받는 내용>', value)