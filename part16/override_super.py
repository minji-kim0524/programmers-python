# 오버라이드 super()
# - 자식클래스에서 부모클래스의 내용을 사용하고 싶은 경우
# - super().부모클래스내용

# 부모 클래스
class Animal():
    def __init__(self, name):
        self.name = name

    def walk(self):
        print("걷는다")

    def eat(self):
        print("먹는다")

    def greet(self):
        print("{}이/가 인사한다".format(self.name))

# 자식 클래스1
class Human(Animal):
    def __init__(self, name, hand):
        super().__init__(name)
        self.hand = hand

    def wave(self):
        print("{}을 흔들면서".format(self.hand))

    # 부모 클래스의 메소드와 동일한 이름의 메소드를 만듦으로써 덮어쓰기함
    def greet(self):
        self.wave()
        super().greet()

person = Human("철수", "오른손")
person.greet()

