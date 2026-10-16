# 모델링
# - 클래스로 현실의 개념을 표현하는 것

class Human():
    """인간에 대한 클래스 생성"""

person = Human()
person.name = '철수'
person.weight = 60.5

# 사람을 찍어내는 함수
def create_human(name, weight):
    person = Human()
    person.name = name
    person.weight = weight
    return person

Human.create = create_human

person = Human.create('철수', 60.5)

# 먹는 함수
def eat(person):
    person.weight += 0.1
    print('{}가 먹어서 {}kg이 되었습니다.'.format(person.name, person.weight))

# 걷는 함수
def walk(person):
    person.weight -= 0.1
    print('{}가 걸어서 {}kg이 되었습니다.'.format(person.name, person.weight))

Human.eat = eat
Human.walk = walk

person.walk()
person.eat()
person.walk()