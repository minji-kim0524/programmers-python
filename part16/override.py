# 오버라이드
# - 클래스의 속성 덮어쓰기

# 부모 클래스
class Animal():
    def walk(self):
        print("걷는다")

    def eat(self):
        print("먹는다")

    def greet(self):
        print("인사한다")

class Cow(Animal):
    """소"""

# 자식 클래스1
class Human(Animal):
    def wave(self):
        print("손을 흔든다")
    # 부모 클래스의 메소드와 동일한 이름의 메소드를 만듦으로써 덮어쓰기함
    def greet(self):
        self.wave()

# 자식 클래스2
class Dog(Animal):
    def wag(self):
        print("꼬리를 흔든다")
    # 부모 클래스의 메소드와 동일한 이름의 메소드를 만듦으로써 덮어쓰기함
    def greet(self):
        self.wag()

person = Human()
person.greet()

dog = Dog()
dog.greet()

cow = Cow()
cow.greet()