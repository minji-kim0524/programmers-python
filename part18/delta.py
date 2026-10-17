# timedelta 클래스
# - 시간의 연산을 가능하게 해주는 클래스
import datetime

# 오늘부터 100일 후 날짜 확인
hundred = datetime.timedelta(days = 100)
after_day = datetime.datetime.now() + hundred
print(after_day)

# 오늘부터 100일 전 날짜 계산
before_day = datetime.datetime.now() - hundred
print(before_day)

# 다음날 특성 시간 지정
tomorrow = datetime.datetime.now().replace(hour = 9, minute = 0, second = 0) + datetime.timedelta(days=1)
print(tomorrow)