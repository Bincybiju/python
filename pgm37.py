s=input("Enter a string")
n={}
for i in s:
    if i in n:
        n[i]+=1
    else:
            n[i]=1
print("count of all characters in",s,"is:",str(n))
