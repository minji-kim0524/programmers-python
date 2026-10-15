# 예외처리
# try:
#   에러가 발생할 가능성이 있는 코드(경우)
# except 에러종류:
#   에러가 발생했을 경우 처리할 코드
# try except 예외처리 대신 if else를 사용할 수 있다.
text = '100%'
try:
    number = int(text)
except ValueError:
    print('{}는 숫자가 아닙니다.'.format(text))


def safe_pop_index(list, index):
    try:
        print(list.pop(index))
    except IndexError:
        print('{}번째 index의 값을 가져올 수 없습니다.'.format(index))

safe_pop_index([1,2,3], 5)

# if문을 우선적으로 사용하고, 대부분 if문으로 처리가 가능하나
# try except 문이 아니면 해결하기 어려운 경우도 있다. (아래의 경우)
try:
    import my_module
except ImportError:
    print('해당 모듈이 없습니다.')