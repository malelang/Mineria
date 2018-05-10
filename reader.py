data=open("cleveland.txt","r")
cont=data.read()
b=cont.splitlines()
d=[]
e=[]
for i in range(0,len(b)):
    c=b[i].split()
    d.append(c)
for i in range(0,len(d)):
    for j in range (0,len(d[i])):
        if (d[i][j]=="name"):
            flag=1
        else:
            flag=0
    if flag==0:
        d[i+1]=d[i]+d[i+1]
    else:
        e.append(d[i])
        d[i]=[]
        flag=0

newdata=open("dataset.txt","w")
newdata.seek(0)
newdata.truncate()

for i in range(0,len(e)):
    for j in range(0,len(e[i])-1):
        newdata.write(str(e[i][j]))
        if j==len(e[i])-2:
            print "salto de linea"
            newdata.write("\n")
        else:
            print "coma"
            print j
            newdata.write(",")
