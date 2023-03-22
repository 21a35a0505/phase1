s=input()
p=input()
a=s
l=[]
d={}
while(1):
    for i in p:
        l.append(a.index(i))
        print(l)
    if len(l)==len(p):
        print(max(l))
        print(min(l))
        d[max(l)-min(l)]=a[min(l):max(l)+1]
        a=a[min(l)+1:max(l)+1]
        l.clear()
    else:
        break
        
print(d)
