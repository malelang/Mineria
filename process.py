data=open("ecgwrist.txt","r")
cont=data.read()
b=cont.splitlines()
c=[]
d=[]
title=0
nueves=0
for i in range(0,len(b)):
    c=b[i].split(",")
    if title>=76:
        d.append(c)
    title=title+1
for i in range(0,len(d)):
    longitud=len(d[i])
    for j in range(0,len(d[i])):
        if(d[i]=="-9"):
            nueves=nueves+1
    if(nueves>0.4*longitud):
        
