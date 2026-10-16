# 클래스 만들기

# 클래스 생성
class Human():
    """사람"""

person1 = Human() # person1은 인스턴스임
person2 = Human()

person1.language = '한국어'
person2.language = '영어'

# print(person1.language)
# print(person2.language)

person1.name = '한국인'
person2.name = '외국인'

def speak(person):
    print('{}이 {}로 말을 합니다.'.format(person.name, person.language))

# 아래 두 가지 방법은 동일한 결과를 가져옴
# 방법1
speak(person1)
speak(person2)

# 방법2
# 클래스에 함수를 넣을 수 있음
Human.speak = speak

person1.speak() # 매개변수가 없음
person2.speak()