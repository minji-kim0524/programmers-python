#  예외처리
from UnexpectedRSPValue import UnexpectedRSPValue, BadUserName, PassWordNotMatched

value = '가'
try:
    if value not in ['가위', '바위', '보']:
        raise UnexpectedRSPValue("가위바위보 중 하나의 값이여야 합니다.")
except UnexpectedRSPValue:
    print("에러가 발생했습니다.")


def sign_up():
    '''회원가입 함수'''

try:
    sign_up()
except BadUserName:
    print("이름으로 사용할 수 없습니다.")
except PassWordNotMatched:
    print("입력하신 패스워드가 일치하지 않습니다.")