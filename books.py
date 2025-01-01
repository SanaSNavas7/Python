class Publisher:
    def __init__(self,name):
        self.name=name
    def display(self):
        print(f"Book name: {self.name}")
class Book(Publisher):
    def __init__(self,name,title,author):
        super().__init__(name)
        self.title=title
        self.author=author
    def display(self):
        print(f"{self.title},written by {self.author}")
        super().display()
class Python(Book):
    def __init__(self,price,no_pages):
        super().__init__(price,no_pages)
        self.price=price
        self.no_pages=no_pages
    def display(self):
        super().display()
        print(f"Price: {self.price} No.of pages: {no_pages}")
book=Python("Python programming","introduction","sana",200,2000)
book.display()


    

    