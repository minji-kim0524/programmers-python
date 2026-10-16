# 메소드
# - 클래스에 포함되어 있는 함수
# - 즉, 클래스에 묶여 클래스의 인스턴스와 관계되는 일을 하는 함수를 의미함

class Human():
    """인간에 대한 클래스 생성"""
    # 사람을 찍어내는 함수
    def create(name, weight):
        person = Human()
        person.name = name
        person.weight = weight
        return person
    # 먹는 함수
    def eat(person):
        person.weight += 0.1
        print('{}가 먹어서 {}kg이 되었습니다.'.format(person.name, person.weight))

    # 걷는 함수
    def walk(person):
        person.weight -= 0.1
        print('{}가 걸어서 {}kg이 되었습니다.'.format(person.name, person.weight))

    # 말하는 함수
    # self란?
    # - 메소드의 첫번째 인자
    def speak(self, message): 
        print(message)


person = Human.create('철수', 60.5) # 인스턴스 생성
person.walk()
person.eat()
person.walk()

person.speak("안녕하세요") # 인스턴스의 매개변수를 전달 할 때는 self 매개변수는 생략하고 전달 -> 자동으로 self 자리에 들어감