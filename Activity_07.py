#addition of 2 nos in list part 2
a=input()
Mylist=a.split()
res=int(a[0])+int(a[2])
print("{0}+{1}={2}".format(a[0],a[2],res))
# other way using for
a=input()
Mylist=a.split()
sum=0
for i in range(len(Mylist)):
    sum=sum+int(Mylist[i])
    print("{0}+".format(Mylist[i]))
print("={0}".format(sum))
