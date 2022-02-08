fileobj = open("file1.txt",'r+')
filelist = []
condition = True

while condition:
    x = fileobj.readline()
    filelist.append(x)
    if not x:
        print("file ended")
        condition = False

fileobjnew = open('file2.txt','a')
for i in range(0,len(filelist),2):
    fileobjnew.write(filelist[i])

fileobjnew.close()
fileobj.close()
