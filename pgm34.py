l=[]
n=int(input("Enter the limit"))
print("enter",n,"words")
for i in range(1,n+1):
    s2=input()
    l.append(s2)
    b=0
    for x in l:
        c=len(x)
        if(b<c):
            b=c
            s3=x
print("longest word and its length is ",s3,":",b)
