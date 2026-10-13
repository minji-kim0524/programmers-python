# 주석이란? 코드를 설명하기 위해 코드에 적어 놓은 프로그래밍 언어가 무시하는 문자
print('안녕! 나는 지구인이야. 너는 어느 별에서 왔니?')


identity = '지구인' # 이렇게도 주석을 달 수 있다.
number_of_legs = 2
print('안녕! 나는', '지구인', '이야.', '나는 다리가', 2, '개 있어')
print('안녕! 나는', identity, '이야.', '나는 다리가', number_of_legs, '개 있어')

identity = '한국인'
number_of_legs = 4
print('안녕! 나는', identity, '이야.', '나는 다리가', number_of_legs, '개 있어')

# 여러줄을 주석으로 처리하고 싶을때는 따옴표 """로 그 내용을 둘러싼다.

"""identity = '지구인' # 이렇게도 주석을 달 수 있다.
number_of_legs = 2
print('안녕! 나는', '지구인', '이야.', '나는 다리가', 2, '개 있어')
print('안녕! 나는', identity, '이야.', '나는 다리가', number_of_legs, '개 있어')

identity = '한국인'
number_of_legs = 4
print('안녕! 나는', identity, '이야.', '나는 다리가', number_of_legs, '개 있어')"""