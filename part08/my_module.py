# 모듈 만들기
def random_rsp():
    """무작위로 가위바위보를 내는 함수"""
    import random
    return random.choice(['가위', '바위', '보'])

PAPER = '보'
SCISSOR = '가위'
ROCK = '보'