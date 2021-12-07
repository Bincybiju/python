n=int(input("Enter the middle limit"))
for i in range(0,n,1):
    for j in range(0,i+1,1):
        print("*",end="")
    print()
for i in range(0,n-1,1):
    for j in range(i,n-1,1):
        print("*",end="")
    print()
                      
