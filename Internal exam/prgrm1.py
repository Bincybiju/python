import csv 
dict_value = [
{"name":"Bincy","MFC":53,"DC":39,"DS":90,"ASE":44},
{"name":"Arya","MFC":76,"DC":78,"DS":50,"ASE":79},
{"name":"Anusree","MFC":67,"DC":78,"DS":67,"ASE":99},
{"name":"Akhila","MFC":45,"DC":98,"DS":95,"ASE":65},
{"name":"Diya","MFC":56,"DC":99,"DS":100,"ASE":94},
{"name":"Sony","MFC":45,"DC":99,"DS":70,"ASE":94},
{"name":"Sneha","MFC":36,"DC":90,"DS":59,"ASE":93},
{"name":"Chinnu","MFC":66,"DC":97,"DS":80,"ASE":76},
{"name":"Amrutha","MFC":56,"DC":99,"DS":95,"ASE":94},
{"name":"Varsha","MFC":36,"DC":59,"DS":76,"ASE":84},]

fields = ["name","MFC","DC","DS","ASE"]

with open('student.csv','w') as c:
    writer = csv.DictWriter(c,fieldnames=fields)
    writer.writeheader()
    writer.writerows(dict_value)
    c.close()
mfc=0
dc=0
ase=0
ds=0
with open('student.csv','r') as cfiles:
     reader = csv.DictReader(cfiles)
     for row in reader:
         print(row['name'],":",(int(int(row['MFC'])+int(row['DC'])+int(row['DS'])+int(row['ASE']))/400)*100)
         mfc=mfc+int(row['MFC'])
         dc=dc+int(row['DC'])
         ase=ase+int(row['ASE'])
         ds=ds+int(row['DS'])
print("\n\nAverage of subjcts")
print("MFC",mfc/10)
print("DC",dc/10)
print("DS",ds/10)
print("ASE",ase/10)
