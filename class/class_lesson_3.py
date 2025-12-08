class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price

    def info(self):
        print(f"{self.name} - {self.price}")


class Customer:
    def __init__(self,name):
        self.name = name

    def info(self):
        print(f"Покупець {self.name}")


class OrderItem:
     def __init__(self,product,quantity):
         self.product = product
         self.quantity = quantity

     def get_total(self):
         return self.product.price * self.quantity

     def info(self):
         total = self.get_total()
         print(f"{self.product.name} x {self.quantity} = {total} грн")


class Order:
    def __init__(self,customer):
        self.customer = customer
        self.items = []

    def add_item(self,product,quantity):
        item = OrderItem(product,quantity)
        self.items.append(item)

    def get_total(self):
        total = 0
        for item in self.items:
            total += item.get_total()

        return total

    def show_info(self):
        print("-------Замовлення-------")
        self.customer.info()

        print("Позиції")
        for item in self.items:
            item.info()

        print(f"Всього до сплати: {self.get_total()}")
        print("---------------")



pizze = Product("Піца Маргарита",200)
cola = Product("Кола",50)

customer1 = Customer("Назар")

order1 = Order(customer1)

order1.add_item(pizze,3)
order1.add_item(cola,5)

order1.show_info()