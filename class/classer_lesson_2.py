class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author

    def info(self):
        print(f"{self.title}, автор: {self.author}")

# .add  {a,b,c}
# .append  []

class Reader:
    def __init__(self,name):
        self.name = name
        self.books = []

    def take_book(self,book):
        self.books.append(book)
        print(f"{self.name} взяв(ла) книгу: {book.title}")

    def show_book(self):

        if not self.books:
            print(f"{self.name} зараз без книги")

        else:
            print(f"{self.name} має такі книги")
            for book in self.books:
                book.info()


book1 = Book("Мистецтво програмування","Дональд Кнут")
book2 = Book("Чиста Архітектура","Роберт Марті")
reader1 = Reader("Назар")


reader1.show_book()
reader1.take_book(book1)
reader1.take_book(book2)

reader1.show_book()



