s=[int(x) for x in input().split(",")]
for x in s:
   if x>100:
       print(str(x).replace(str(x),'over'))
   else:
       print(x,end=" ")
  
