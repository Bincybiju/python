l=[1,2,3,4,5,6]
even=[]
odd=[]
for i in l:
    if i%2==0:
        even.append(i)
    else:
            odd.append(i)
print("even numbers are",even)
print("odd numbers are",odd)
