class Publisher:
    def __init__(self,name):
        self.name=name
    def display(self):
        print("Publisher name=",self.name)
class Book(Publisher):
    def __init__(self,name,title,author):
        Publisher.__init__(self,name)
        self.title=title
        self.author=author
    def displaybook(self):
        self.display()
        print("title=",self.title)
        print("author=",self.author)
class Python(Book):
    def __init__(self,name,title,author,price,pages):
        Book.__init__(self,name,title,author)
        self.price=price
        self.pages=pages
    def displaydetails(self):
        self.displaybook()
        print("price=",self.price)
        print("number of pages=",self.pages)
s1=Python("DC books","Python programming","Dr.Jeeva Jose",350,220)
s1.displaydetails()
    
