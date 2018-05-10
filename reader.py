data=open("cleveland.txt","r")
cont=data.read()
b=cont.splitlines()
d=[]
e=[]
for i in range(0,len(b)):
    c=b[i].split()
    d.append(c)
for i in range(0,len(d)):
    #print "enter"
    #print len(d[i])
    #print d[i]
    for j in range (0,len(d[i])):
        if (d[i][j]=="name"):
            flag=1
        else:
            flag=0
    if flag==0:
        d[i+1]=d[i]+d[i+1]
    else:
        """print "this is the last line"
        print d[i]
        print len(d[i])
        d[i].pop()
        print d[i]
        print len(d[i])"""
        e.append(d[i])
        d[i]=[]
        flag=0
with open("dataset.txt","w") as newdata:
    newdata.seek(0)
    newdata.truncate()
    for i in range(0,len(e)):
        t=len(e[i])
        print t
        for j in range(0,t):
            newdata.write(str(e[i][j])
            if (j==t):
                newdata.write("\n")
            else:
                newdata.write(",")
