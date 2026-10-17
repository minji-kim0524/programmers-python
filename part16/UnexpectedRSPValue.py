class UnexpectedRSPValue(Exception):
    '''가위 바위 보 중 하나가 아닌 경우 발생하는 에러'''

class BadUserName(Exception):
    '''회원가입시 잘못된 이름을 사용하는 경우 발생하는 에러'''

class PassWordNotMatched(Exception):
    '''패스워드가 일치하지 않을 경우 발생하는 에러'''