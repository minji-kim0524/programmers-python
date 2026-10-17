# datetime 모듈
# - 빼기(-) 연산을 지원함 -> 남은 일수 계산가능
import datetime

# datetime 모듈안에는 같은 이름의 클래스가 있음 -> 사용시 아래와 같이 작성함
start_time = datetime.datetime.now()

# replace 메소드
# - 자기 자신을 변경하는 것이 아니라 새로운 변수에 변경된 값을 저장함 (기존 변수의 값은 변경되지❌)
# - 자기 자신을 변경하려면 기존 변수에 replace 를 적용해서 값을 할당시켜줘야함
new_time = start_time.replace(year= 2020, month= 12, day =12)
print(new_time)
print(start_time)

# 처음 만들때부터 원하는 datetime이 있다면 지정해서 만들 수 있음
pix_time = datetime.datetime(2028,5,1)
print(pix_time)

# 남은 일수 계산
# - how_long과 같은 값을 가지는 변수는 시,분은 확인할 수 없음. days, seconds만 확인가능하므로 시, 분은 seconds를 기준으로 계산해야함
how_long = pix_time - datetime.datetime.now()
print("2028년 5월 1일까지는 {}일 {}시간 남았습니다.".format(how_long.days, how_long.seconds//3600))