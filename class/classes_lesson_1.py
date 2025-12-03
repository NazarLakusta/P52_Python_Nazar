class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author

    def info(self):
        print(f"{self.title}, автор: {self.author}")




class Reader:
    def __init__(self,name):
        self.name = name
        self.book = None

    def take_book(self,book):
        self.book = book
        print(f"{self.name} взяв(ла) книгу: {self.book.title}")

    def show_book(self):

        if self.book is None:
            print(f"{self.name} зараз без книги")

        else:
            print(f"{self.name} читає книгу")
            self.book.info()


book1 = Book("Мистецтво програмування","Дональд Кнут")
reader1 = Reader("Назар")


reader1.show_book()
reader1.take_book(book1)
reader1.show_book()





