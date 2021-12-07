n=int(input("enter number"))
d=0
sum=0
while(n>0):
  d=n%10
  sum=sum+d
  n=int(n/10)
print("sum is",sum)
