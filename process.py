import numpy as np

data=open("temporal.txt","r")
cont=data.read()
b=cont.splitlines()
c=[]
d=[]
nuevo=[]
titulo=[]
title=0
nueves=0
for i in range(0,len(b)):
    c=b[i].split(",")
    if title>=76:
        d.append(c)
    else:
        titulo.append(c)
    title=title+1

#AQUI QUITAMOS TODOS AQUELLOS REGISTROS QUE TENGAN MAS DEL 40 PORCIENTO DE
#INFORMACION PERDIDA
"""
for i in range(0,len(d)):
    longitud=len(d[i])
    for j in range(0,len(d[i])):
        if(d[i][j]=="-9"):
            nueves=nueves+1
    if(nueves<(0.4*longitud)):
        nuevo.append(d[i])
    nueves=0
"""
vfaltas=[0]*75
for i in range(0,len(d)):
    for j in range(0,len(d[i])):
        if(d[i][j]=="-9"):
            vfaltas[j]=vfaltas[j]+1

borrar=[]
for i in range(0,len(vfaltas)):
    if(vfaltas[i]>(0.4*len(d))):
        borrar.append(i)

borrar.sort(reverse=True)
print borrar
for i in range(0,len(d)):
    for j in borrar:
        del(d[i][j])
for i in borrar:
    del(titulo[i+1])

borrar=[1,9,28,39,40,41,42,43,44,45,46,47,48,49,50]
borrar.sort(reverse=True)
for i in range(0,len(d)):
    for j in borrar:
        del(d[i][j])
for i in borrar:
    del(titulo[i+1])

print len(d[1])
#AQUI QUITAMOS TODOS AQUELLOS ATRIBUTOS QUE NO ESTABAN BIEN EXPLICADOS EN LA
#PAGINA DEL DATASET O LOS QUE SE DICE QUE SON IRRELEVANTES O QUE NO SE USARON
"""
borrar=[,72,71,70,69,68,67,66,,64
for i in range(0,len(nuevo)):
    for j in borrar:
        del(nuevo[i][j])
for i in borrar:
    del(titulo[i+1])

#AQUI VAMOS A VER CUALES ATRIBUTOS TIENEN DATOS PERDIDOS PARA MIRAR COMO LOS MANEJAMOS
vfaltas=[0]*(75-len(borrar))
for i in range(0,len(nuevo)):
    for j in range(0,len(nuevo[i])):
        if(d[i][j]=="-9"):
            vfaltas[j]=vfaltas[j]+1

borrar=[]
for i in range(0,len(vfaltas)):
    if(vfaltas[i]>277):
        borrar.append(i)

print borrar

for i in range(0,len(vfaltas)):
    print("el atributo numero "+str(i+1)+" tiene "+str(vfaltas[i])+" datos faltantes")

print len(nuevo)

"""
"""
newdata=open("ecgwrist.txt","w")
newdata.seek(0)
newdata.truncate()
for i in range(0,len(titulo)):
    for j in range(0,len(titulo[i])):
        newdata.write(str(titulo[i][j]))
        if j==len(titulo[i])-1:
            newdata.write("\n")

for i in range(0,len(nuevo)):
    for j in range(0,len(nuevo[i])):
        newdata.write(str(nuevo[i][j]))
        if j==len(nuevo[i])-1:
            newdata.write("\n")
        else:
            newdata.write(",")
"""
