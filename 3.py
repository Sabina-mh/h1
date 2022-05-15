infile=open("t.txt",'r')
s=infile.readlines()
infile.close()
count=0
for i in s:
   print(i.rstrip().split(',')[0])
   a=input("enter answer")
   if a==i.rstrip().split(',')[1]:
       count+=1
       print("true")
   else:
      print("false")

name=input("enter user name")
s=name+'   resault= '+str(count)
print(s)
outfile=open("user result.txt","w")
outfile.write(s)
outfile.close()
