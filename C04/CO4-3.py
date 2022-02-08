class Rectangle:
    __width=0
    __length=0
    __area=0
    def __init__(self,length,width):
        self.__length=length
        self.__width=width
    def area(self):
        self.__area=self.__length*self.__width
        print("Area is :",self.__area)
    def __lt__(self,ob):
        if(self.__area<ob.__area):
            return "Area1 is lesserthan Area2"
        else:
            return "Area2 is lesserthan Area1"
length=int(input("enter the length"))
width=int(input("enter the width"))
ob1=Rectangle(length,width)
ob1.area()
length=int(input("enter the length"))
width=int(input("enter the width"))
ob2=Rectangle(length,width)
ob2.area()
print(ob1<ob2)
              
    

    
