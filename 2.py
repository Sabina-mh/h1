num=int(input('enter decimal number'))
l=[]
while num>0:
    l.append(num%2)
    num//=2
l.reverse()
for i in l:
    print(i,end='')

