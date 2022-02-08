class Time:
    def __init__(self,hour,minute,second):
        self.hour=hour
        self.minute=minute
        self.second=second
    def __add__(self,other):
        return (self.hour+other.hour,self.minute+other.minute,self.second+other.second)

hour=int(input("Enter hour:"))
minute=int(input("Enter minute:"))
second=int(input("Enter second:"))
time1=Time(hour,minute,second)
hour=int(input("Enter hour:"))
minute=int(input("Enter minute:"))
second=int(input("Enter second:"))
time2=Time(hour,minute,second)
print("Total time:",time1+time2)
            
