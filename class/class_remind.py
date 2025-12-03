class Student:

    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.health = 100

    # метод класу
    def say_hello(self):
        print(f"Привіт, я {self.name}, мені {self.age} років, моє здоровя: {self.health} ")


# функція
def hello():
    print("Helloo!!!")


hello()
student1 = Student("Андрій",16)
student1.say_hello()


