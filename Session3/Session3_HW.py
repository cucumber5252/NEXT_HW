class Person:
  def __init__(self, name, age, height):
    self.name=name
    self.age=age
    self.height=height

  def introduce(self):
    print(f"제 이름은 {self.name}, 내 나이는 {self.age}, 내 키는 {self.height}입니다!")

  def yell(self):
    print("아?")


class Developer(Person):
  keyboard="기계식"
  def __init__(self, name, age, height):
    super().__init__(name, age, height)
  
  def yell(self):
    print("어?")


class Designer(Person):
  def __init__(self, name, age, height, disease):
    super().__init__(name, age, height)
    self.disease=disease


class ProductManager(Person):
  def yell(self):
    print("개발자님 여기 오류있어요")
  
  def aging(self):
    self.age+=2
    self.height-=5
    print("개발자를 새로 뽑아야하나...")
    Developer.keyboard="멤브레인"


d1=Developer("강동혁", 23, 183)
d2=Designer("김동혁", 25, 173, "허리디스크")
p1=ProductManager("이동혁", 27, 163)


print(d1.keyboard)
d1.introduce()
d2.introduce()
p1.introduce()


d1.yell()
d2.yell()
p1.yell()


p1.aging()


d1.introduce()
d2.introduce()
p1.introduce()


print(d1.keyboard)