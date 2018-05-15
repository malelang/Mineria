import numpy as np

def moda(vector):
    ceros=0
    unos=0
    for i in range(0,len(vector)):
        if(vector[i]=='0'):
            ceros=ceros+1
        if(vector[i]=='1'):
            unos=unos+1
    resul=[ceros,unos]
    return resul

def modatres(vector):
    ceros=0
    unos=0
    dos=0
    for i in range(0,len(vector)):
        if(vector[i]=='0'):
            ceros=ceros+1
        elif (vector[i]=='1'):
            unos=unos+1
        elif(vector[i]=='2'):
            dos=dos+1
    vdd=[ceros,unos,dos]
    resul=vdd.index(max(vdd))
    return resul

def media(vector):
    nv=[]
    for i in range(0,len(vector)):
        if vector[i]!= "-9":
            nv.append(float(vector[i]))
    resul=np.mean(nv, dtype=np.float32)
    return resul

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

#AQUI QUITAMOS TODOS AQUELLOS ATRIBUTOS QUE TENGAN MAS DEL 40 PORCIENTO DE
#INFORMACION PERDIDA

#Inicialize list of -9s by 75 attributes
#vfaltas is set for all raws in d
vfaltas=[0]*75
Errors = 0
TotalValues = 0

for i in range(0,len(d)): 
    
    for j in range(0,len(d[i])):
        
        TotalValues = TotalValues + 1
        
        if(d[i][j]=="-9"):
            #Count number of -9s in dst
            vfaltas[j]=vfaltas[j]+1
            Errors = Errors +1
print("%%%%%%%%%%%%%%%  ANALYSIS  %%%%%%%%%%%%%%%%%%%")
print("1. Total Missing Values: "+str(Errors))
print("2. Total Values from temporal.txt: "+str(TotalValues))
print("3. % Missing Values (-9): "+str(100*Errors/TotalValues)+"%")

borrar=[]
for i in range(0,len(vfaltas)):
    if(vfaltas[i]>(0.4*len(d))):
        borrar.append(i)
borrar.sort(reverse=True)
for i in range(0,len(d)):
    for j in borrar:
        del(d[i][j])
for i in borrar:
    del(titulo[i+1])
#AQUI QUITAMOS TODOS AQUELLOS ATRIBUTOS QUE NO ESTAN BIEN DESCRITOS Y POR LO
#TANTO NO APORTAN INFORMACION IMPORTANTE O ESCLARECEDORA

borrar=[1,9,23,28,39,40,41,42,43,44,45,46,47,48,49,50]
borrar.sort(reverse=True)
for i in range(0,len(d)):
    for j in borrar:
        del(d[i][j])
for i in borrar:
    del(titulo[i+1])


vfaltas=[0]*36
for i in range(0,len(d)):
    for j in range(0,len(d[i])):
        if(d[i][j]=="-9"):
            vfaltas[j]=vfaltas[j]+1
            
#VAMOS A MIRAR UN ATRIBUTO POR UNO
#comenzamos por PainLocation donde puede ser 0 o 1
painloc=[]
for i in range(0,len(d)):
    painloc.append(d[i][3])
vb=moda(painloc)
ceros,unos=vb[0],vb[1]
cf=round((vfaltas[3]*ceros)/(len(d)-vfaltas[3]))
uf=vfaltas[3]-cf
for i in range(0,len(d)):
    if(d[i][3]=="-9"):
        if(cf==0):
            d[i][3]="1"
            uf=uf-1
        else:
            d[i][3]="0"
            cf=cf-1
#seguimos con PainExertion donde puede ser 0 o 1
painexe=[]
for i in range(0,len(d)):
    painexe.append(d[i][4])
vb=moda(painexe)
ceros,unos=vb[0],vb[1]

cf=round((vfaltas[4]*ceros)/(len(d)-vfaltas[4]))
uf=vfaltas[4]-cf
for i in range(0,len(d)):
    if(d[i][4]=="-9"):
        if(cf==0):
            d[i][4]="1"
            uf=uf-1
        else:
            d[i][4]="0"
            cf=cf-1
#seguimos con RelievedAfterRest donde puede ser 0 o 1
painrar=[]
for i in range(0,len(d)):
    painrar.append(d[i][5])
vb=moda(painrar)
ceros,unos=vb[0],vb[1]

cf=round((vfaltas[5]*ceros)/(len(d)-vfaltas[5]))
uf=vfaltas[5]-cf
for i in range(0,len(d)):
    if(d[i][5]=="-9"):
        if(cf==0):
            d[i][5]="1"
            uf=uf-1
        else:
            d[i][5]="0"
            cf=cf-1

#seguimos con RestingBPAdmissions donde debemos sacar la media
restbpa=[]
for i in range(0,len(d)):
    restbpa.append(d[i][7])
med=media(restbpa)
for i in range(0,len(d)):
    if(d[i][7]=="-9"):
        d[i][7]=str(med)

#seguimos con cholesterol donde debemos sacar la media
cholesterol=[]
for i in range(0,len(d)):
    cholesterol.append(d[i][8])
med=media(cholesterol)
for i in range(0,len(d)):
    if(d[i][8]=="-9"):
        d[i][8]=str(med)

#seguimos con FastingBloodSugar donde puede ser 0 o 1
fbs=[]
for i in range(0,len(d)):
    fbs.append(d[i][9])
vb=moda(fbs)
ceros,unos=vb[0],vb[1]
cf=round((vfaltas[9]*ceros)/(len(d)-vfaltas[9]))
uf=vfaltas[9]-cf
for i in range(0,len(d)):
    if(d[i][9]=="-9"):
        if(cf==0):
            d[i][9]="1"
            uf=uf-1
        else:
            d[i][9]="0"
            cf=cf-1

#seguimos con RestEcg donde puede ser 0 ,1 o 2
recg=[]
for i in range(0,len(d)):
    recg.append(d[i][10])
vb=modatres(recg)
for i in range(0,len(d)):
    if(d[i][10]=="-9"):
        d[i][10]=str(vb)

#seguimos con EcgMonth donde debemos sacar la media
month=[]
for i in range(0,len(d)):
    month.append(d[i][11])
med=round(media(month))
for i in range(0,len(d)):
    if(d[i][11]=="-9"):
        d[i][11]=str(med)

#seguimos con EcgDay donde debemos sacar la media
day=[]
for i in range(0,len(d)):
    day.append(d[i][12])
med=round(media(day))
for i in range(0,len(d)):
    if(d[i][12]=="-9"):
        d[i][12]=str(med)

#seguimos con EcgYear donde debemos sacar la media
year=[]
for i in range(0,len(d)):
    year.append(d[i][13])
med=round(media(year))
for i in range(0,len(d)):
    if(d[i][13]=="-9"):
        d[i][13]=str(med)

#seguimos con DigitalisDE donde puede ser 0 o 1
dig=[]
for i in range(0,len(d)):
    dig.append(d[i][14])
vb=moda(dig)
ceros,unos=vb[0],vb[1]
cf=round((vfaltas[14]*ceros)/(len(d)-vfaltas[14]))
uf=vfaltas[14]-cf
for i in range(0,len(d)):
    if(d[i][14]=="-9"):
        if(cf==0):
            d[i][14]="1"
            uf=uf-1
        else:
            d[i][14]="0"
            cf=cf-1

#seguimos con BetaBlockerDE donde puede ser 0 o 1
beta=[]
for i in range(0,len(d)):
    beta.append(d[i][15])
vb=moda(beta)
ceros,unos=vb[0],vb[1]
cf=round((vfaltas[15]*ceros)/(len(d)-vfaltas[15]))
uf=vfaltas[15]-cf
for i in range(0,len(d)):
    if(d[i][15]=="-9"):
        if(cf==0):
            d[i][15]="1"
            uf=uf-1
        else:
            d[i][15]="0"
            cf=cf-1

#seguimos con NitratesDE donde puede ser 0 o 1
nit=[]
for i in range(0,len(d)):
    nit.append(d[i][16])
vb=moda(nit)
ceros,unos=vb[0],vb[1]
cf=round((vfaltas[16]*ceros)/(len(d)-vfaltas[16]))
uf=vfaltas[16]-cf
for i in range(0,len(d)):
    if(d[i][16]=="-9"):
        if(cf==0):
            d[i][16]="1"
            uf=uf-1
        else:
            d[i][16]="0"
            cf=cf-1

#seguimos con CalBlockerDE donde puede ser 0 o 1
calcium=[]
for i in range(0,len(d)):
    calcium.append(d[i][17])
vb=moda(calcium)
ceros,unos=vb[0],vb[1]
cf=round((vfaltas[17]*ceros)/(len(d)-vfaltas[17]))
uf=vfaltas[17]-cf
for i in range(0,len(d)):
    if(d[i][17]=="-9"):
        if(cf==0):
            d[i][17]="1"
            uf=uf-1
        else:
            d[i][17]="0"
            cf=cf-1

#seguimos con DiureticDE donde puede ser 0 o 1
diuretic=[]
for i in range(0,len(d)):
    diuretic.append(d[i][18])
vb=moda(diuretic)
ceros,unos=vb[0],vb[1]
cf=round((vfaltas[18]*ceros)/(len(d)-vfaltas[18]))
uf=vfaltas[18]-cf
for i in range(0,len(d)):
    if(d[i][18]=="-9"):
        if(cf==0):
            d[i][18]="1"
            uf=uf-1
        else:
            d[i][18]="0"
            cf=cf-1

#seguimos con ExerciseProtocol donde debemos sacar la media
proto=[]
for i in range(0,len(d)):
    proto.append(d[i][19])
med=round(media(proto))
for i in range(0,len(d)):
    if(d[i][19]=="-9"):
        d[i][19]=str(med)

#seguimos con TestDuration donde debemos sacar la media
test=[]
for i in range(0,len(d)):
    test.append(d[i][20])
med=round(media(test))
for i in range(0,len(d)):
    if(d[i][20]=="-9"):
        d[i][20]=str(med)

#seguimos con MaxHR donde debemos sacar la media
hr=[]
for i in range(0,len(d)):
    hr.append(d[i][21])
med=round(media(hr))
for i in range(0,len(d)):
    if(d[i][21]=="-9"):
        d[i][21]=str(med)

#seguimos con RestingHR donde debemos sacar la media
rhr=[]
for i in range(0,len(d)):
    rhr.append(d[i][22])
med=round(media(rhr))
for i in range(0,len(d)):
    if(d[i][22]=="-9"):
        d[i][22]=str(med)

#seguimos con PeakExerciseBP1 donde debemos sacar la media
pbp1=[]
for i in range(0,len(d)):
    pbp1.append(d[i][23])
med=round(media(pbp1))
for i in range(0,len(d)):
    if(d[i][23]=="-9"):
        d[i][23]=str(med)

#seguimos con PeakExerciseBP2 donde debemos sacar la media
pbp2=[]
for i in range(0,len(d)):
    pbp2.append(d[i][24])
med=round(media(pbp2))
for i in range(0,len(d)):
    if(d[i][24]=="-9"):
        d[i][24]=str(med)

#seguimos con RestingBP donde debemos sacar la media
rbp=[]
for i in range(0,len(d)):
    rbp.append(d[i][25])
med=round(media(rbp))
for i in range(0,len(d)):
    if(d[i][25]=="-9"):
        d[i][25]=str(med)

#seguimos con ExcerInducedAngina donde puede ser 0 o 1
eia=[]
for i in range(0,len(d)):
    eia.append(d[i][26])
vb=moda(eia)
ceros,unos=vb[0],vb[1]
cf=round((vfaltas[26]*ceros)/(len(d)-vfaltas[26]))
uf=vfaltas[26]-cf
for i in range(0,len(d)):
    if(d[i][26]=="-9"):
        if(cf==0):
            d[i][26]="1"
            uf=uf-1
        else:
            d[i][26]="0"
            cf=cf-1

#seguimos con Hypo donde puede ser 0 o 1
hyp=[]
for i in range(0,len(d)):
    hyp.append(d[i][27])
vb=moda(hyp)
ceros,unos=vb[0],vb[1]
cf=round((vfaltas[27]*ceros)/(len(d)-vfaltas[27]))
uf=vfaltas[27]-cf
for i in range(0,len(d)):
    if(d[i][27]=="-9"):
        if(cf==0):
            d[i][27]="1"
            uf=uf-1
        else:
            d[i][27]="0"
            cf=cf-1

#seguimos con ExcerInducedSTdepression donde debemos sacar la media
eird=[]
for i in range(0,len(d)):
    eird.append(d[i][28])
med=round(media(eird))
for i in range(0,len(d)):
    if(d[i][28]=="-9"):
        d[i][28]=str(med)

#seguimos con Slope donde debemos sacar la media
slope=[]
for i in range(0,len(d)):
    slope.append(d[i][29])
med=round(media(slope))
for i in range(0,len(d)):
    if(d[i][29]=="-9"):
        d[i][29]=str(med)

slope=[]
for i in range(0,len(d)):
    slope.append(d[i][30])
med=round(media(slope))
for i in range(0,len(d)):
    if(d[i][30]=="-9"):
        d[i][30]=str(med)

slope=[]
for i in range(0,len(d)):
    slope.append(d[i][31])
med=round(media(slope))
for i in range(0,len(d)):
    if(d[i][31]=="-9"):
        d[i][31]=str(med)

slope=[]
for i in range(0,len(d)):
    slope.append(d[i][32])
med=round(media(slope))
for i in range(0,len(d)):
    if(d[i][32]=="-9"):
        d[i][32]=str(med)

slope=[]
for i in range(0,len(d)):
    slope.append(d[i][33])
med=round(media(slope))
for i in range(0,len(d)):
    if(d[i][33]=="-9"):
        d[i][33]=str(med)

newdata=open("ecgwrist.txt","w")
newdata.seek(0)
newdata.truncate()
for i in range(0,len(titulo)):
    for j in range(0,len(titulo[i])):
        newdata.write(str(titulo[i][j]))
        if j==len(titulo[i])-1:
            newdata.write("\n")
newdata.write("@data\n")
for i in range(0,len(d)):
    for j in range(0,len(d[i])):
        newdata.write(str(d[i][j]))
        if j==len(d[i])-1:
            newdata.write("\n")
        else:
            newdata.write(",")