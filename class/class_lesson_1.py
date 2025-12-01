class Dog:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def print_dog(self):
        print(f"Імя: {self.name}, Вік: {self.age}")

    def bark(self):
        print(f"{self.name} каже: вуфф-вуфф!")

dog1 = Dog("Tim",2)
dog1.print_dog()
dog1.bark()


dog2 = Dog("Baf",3)
dog2.print_dog()
dog2.bark()



class Product:
    def __init__(self,title,price,quantity):
        self.title = title
        self.price = price
        self.quantity = quantity

    def info(self):
        print(f"Назва товару: {self.title}  {self.price} грн. - {self.quantity} шт.")

    def total_price(self):
        return self.price * self.quantity


laptop = Product("Gigabyte G6 2024",40000,2)
laptop.info()
print(laptop.total_price())






