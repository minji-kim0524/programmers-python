try:
    list = []
    print(list[0])

    text = 'abc'
    number = int(text)
    # 위 두가지 경우 중 어느 부분에서 에러가 발생했는지 확인하는 방법
    # Exception as ex
    # 발생한 에러의 정보(Exception)를 ex라는 변수에 담는다.
except Exception as ex:
    print('에러가 발생했습니다.', ex)