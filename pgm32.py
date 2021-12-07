def squares(a,b):
 for i in range(a,b+1):
     for j in range(1,int((i/2)+1)):
                   d=i
                   if((i/j)==j):
                      while(i!=0):
                          c=i%10
                          if(c%2==0):
                              i=int(i%10)
                          else:
                                  break
                                  if(i==0):
                                      print(d)
a=int(input("Enter a 4 digit number"))
b=int(input("Enter another 4 digit number"))
                    squares(a,b)
                   
