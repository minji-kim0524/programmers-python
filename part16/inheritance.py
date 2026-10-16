# 상속
# - 클래스의 인자 자리에 다른 클래스를 넣는 것

# 부모 클래스
class Animal():
    def walk(self):
        print("걷는다")

    def eat(self):
        print("먹는다")

# 자식 클래스1
class Human(Animal):
    # def walk(self):
    #     print("걷는다")

    # def eat(self):
    #     print("먹는다")

    def wave(self):
        print("손을 흔든다")

# 자식 클래스2
class Dog(Animal):
    # def walk(self):
    #     print("걷는다")

    # def eat(self):
    #     print("먹는다")

    def wag(self):
        print("꼬리를 흔든다")

person = Human()
person.walk()
person.eat()
person.wave()

dog = Dog()
dog.walk()
dog.eat()
dog.wag()