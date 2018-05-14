vda=["cleveland.txt","longbeach.txt","hungarian.txt","switzerland.txt"]
id=1
vc=[]
for k in range(0,len(vda)):
    data=open(vda[k],"r")
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

    for i in range(0,len(e)):
        e[i][0]=id
        id=id+1
    for i in range(0,len(e)):
        vc.append(e[i])

newdata=open("temporal.txt","w")
newdata.seek(0)
newdata.truncate()
newdata.write("@relation ecgwrist \n")
newdata.write("@attribute Id real \n")
newdata.write("@attribute ccf real \n")
newdata.write("@attribute Age real \n")
newdata.write("@attribute Sex real \n")
newdata.write("@attribute PainLocation real \n")
newdata.write("@attribute PainExertion real \n")
newdata.write("@attribute RelievedAfterRest real \n")
newdata.write("@attribute pncaden real \n")
newdata.write("@attribute ChestPainType real \n")
newdata.write("@attribute RestingBPAdmissions real \n")
newdata.write("@attribute htn real \n")
newdata.write("@attribute cholesterol real \n")
newdata.write("@attribute Smoker real \n")
newdata.write("@attribute CigsPerDay real \n")
newdata.write("@attribute YearsAsSmoker real \n")
newdata.write("@attribute FastingBloodSugar real \n")
newdata.write("@attribute Diabetes real \n")
newdata.write("@attribute FamiliarHistory real \n")
newdata.write("@attribute RestEcg real \n")
newdata.write("@attribute EcgMonth real \n")
newdata.write("@attribute EcgDay real \n")
newdata.write("@attribute EcgYear real \n")
newdata.write("@attribute DigitalisDE real \n")
newdata.write("@attribute BetaBlockerDE real \n")
newdata.write("@attribute NitratesDE real \n")
newdata.write("@attribute CalBlockerDE real \n")
newdata.write("@attribute DiureticDE real \n")
newdata.write("@attribute ExerciseProtocol real \n")
newdata.write("@attribute TestDuration real \n")
newdata.write("@attribute TimeSTnoted real \n")
newdata.write("@attribute Mets real \n")
newdata.write("@attribute MaxHR real \n")
newdata.write("@attribute RestingHR real \n")
newdata.write("@attribute PeakExerciseBP1 real \n")
newdata.write("@attribute PeakExerciseBP2 real \n")
newdata.write("@attribute dummy real \n")
newdata.write("@attribute RestingBP real \n")
newdata.write("@attribute ExcerInducedAngina real \n")
newdata.write("@attribute Hypo real \n")
newdata.write("@attribute ExcerInducedSTdepression real \n")
newdata.write("@attribute Slope real \n")
newdata.write("@attribute HeightatRest real \n")
newdata.write("@attribute HeightatPeakExer real \n")
newdata.write("@attribute Flourosopy real \n")
newdata.write("@attribute RestckmNone real \n")
newdata.write("@attribute ExerckmNone real \n")
newdata.write("@attribute RestREF real \n")
newdata.write("@attribute RestWMA real \n")
newdata.write("@attribute ExerREF real \n")
newdata.write("@attribute ExerWM real \n")
newdata.write("@attribute Thal real \n")
newdata.write("@attribute ThalsevNone real \n")
newdata.write("@attribute ThalpulNone real \n")
newdata.write("@attribute Earlobe real \n")
newdata.write("@attribute MonthCC real \n")
newdata.write("@attribute DayCC real \n")
newdata.write("@attribute YearCC real \n")
newdata.write("@attribute DiagnosisHD real \n")
newdata.write("@attribute lmt real \n")
newdata.write("@attribute ladprox real \n")
newdata.write("@attribute laddist real \n")
newdata.write("@attribute diag real \n")
newdata.write("@attribute cxmain real \n")
newdata.write("@attribute ramus real \n")
newdata.write("@attribute om1 real \n")
newdata.write("@attribute om2 real \n")
newdata.write("@attribute rcaprox real \n")
newdata.write("@attribute rcadist real \n")
newdata.write("@attribute lvx1None real \n")
newdata.write("@attribute lvx2None real \n")
newdata.write("@attribute lvx3None real \n")
newdata.write("@attribute lvx4None real \n")
newdata.write("@attribute lvfNone real \n")
newdata.write("@attribute cathefNone real \n")
newdata.write("@attribute junk real \n")


for i in range(0,len(vc)):
    for j in range(0,len(vc[i])-1):
        newdata.write(str(vc[i][j]))
        if j==len(vc[i])-2:
            newdata.write("\n")
        else:
            newdata.write(",")
