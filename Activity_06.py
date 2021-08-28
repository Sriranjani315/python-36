#slicing and replacing 
a=input()
Mylist=a.split()
slicedlist=Mylist[:3]
print("slicedlist = ",slicedlist)
for i in range(len(Mylist)):
    Mylist[0]="0"
    Mylist[4]="0"
print("replaced list-1", Mylist)
for i in range(len(slicedlist)):
    slicedlist[0]="0"
    slicedlist[2]="0"
print("replaced list-2", slicedlist)
