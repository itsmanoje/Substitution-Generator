import csv
import random

masterlist=[]       #list holding all teacher name along with free period
sublist=[]      #list having free period number
mast_list=[]    #list with one tr name and free period

day_chk=True
while day_chk:          #for checking whether the entered day is valid of not
    day=str(input("Enter the day: "))
    if day.lower()=='monday':
        file_to_open= r'G:\Time Table\monday.csv'
        day_chk=False
    elif day.lower()=='tuesday':
        file_to_open= r'G:\Time Table\tuesday.csv'
        day_chk=False
    elif day.lower()=='wednesday':
        file_to_open= r'G:\Time Table\wednesday.csv'
        day_chk=False
    elif day.lower()=='thursday':
        file_to_open= r'G:\Time Table\thursday.csv'
        day_chk=False
    elif day.lower()=='friday':
        file_to_open= r'G:\Time Table\friday.csv'
        day_chk=False
    elif day.lower()=='saturday':
        file_to_open= r'G:\Time Table\saturday.csv'
        day_chk=False
    else:
        print("Check the day entered !!")
        print()



P1=[]       #List having all teachers substituted for period 1 of a particular day
P2=[]       #List having all teachers substituted for period 2 of a particular day
P3=[]       #List having all teachers substituted for period 3 of a particular day
P4=[]       #List having all teachers substituted for period 4 of a particular day
P5=[]       #List having all teachers substituted for period 5 of a particular day
P6=[]       #List having all teachers substituted for period 6 of a particular day
P7=[]       #List having all teachers substituted for period 7 of a particular day
P8=[]       #List having all teachers substituted for period 8 of a particular day

no=int(input("Enter the number of substitution be given: "))

named=[]  #list of absentee
for zd in range(0,no):          #loop for getting the teachers name

    name2=str(input("Enter the teacher name: "))
    name1=name2.lower()
    named.append(name1)


for name in named:          #using one name of all entered name for putting substitution

    t=open (file_to_open,'r')
    f=csv.reader(t)
    fla=0       #just for confirming name is available of not
    for row in f:
        if name == row[0].lower():
            bp=[]       #busy periods
            for j in range(0,len(row)):         #getting the busy periods of the absentee
                if row[j]=='1':
                    bp.append(j)
            fla=1
    
    t.close()

    #Finding the corresponding teacher who is free
    if fla==1:
        u=open(file_to_open,'r')
        g=csv.reader(u)
        sub_tr={}

        for arow in g:
            for k in bp:
                if arow[k]=='0':
                    sub_tr[k]=arow[0]
            
            if sub_tr != {}:
                
                subl=sub_tr.keys()
                sublist=list(subl)

                #collecting and converting into a nested list

                mast_list.append(arow[0])
                mast_list.append(sublist)
                masterlist.append(mast_list)
                mast_list=[]        #has teacher name and their free period in 2D list
                
            sub_tr={}   # clearing for getting another teachers free period
           

        #getting all the teachers free at  a period at a single list
        p1=[]
        p2=[]
        p3=[]
        p4=[]
        p5=[]
        p6=[]
        p7=[]
        p8=[]
        for tr in range(0,len(masterlist)):
            for bpp in bp:
                if bpp in masterlist[tr][1]:
                    if bpp==1:
                        p1.append(masterlist[tr][0])
                    elif bpp==2:
                        p2.append(masterlist[tr][0])
                    elif bpp==3:
                        p3.append(masterlist[tr][0])
                    elif bpp==4:
                        p4.append(masterlist[tr][0])
                    elif bpp==5:
                        p5.append(masterlist[tr][0])
                    elif bpp==6:
                        p6.append(masterlist[tr][0])
                    elif bpp==7:
                        p7.append(masterlist[tr][0])
                    else:
                        p8.append(masterlist[tr][0])


        #The final organised list of substituted teachers name
        final_list=['-','-','-','-','-','-','-','-']


        #creating a defintion
        def tr_selector(fap,alreadytr,abse):  #free at period
            flag=True
            con=0
            xa=len(fap)-1
            while flag:
                P=random.randint(0,xa)
                ya=fap[P]
                
                if ya not in alreadytr:
                    con+=1
                    if ya not in abse:
                        con+=1
                        if con ==2:
                            alreadytr.append(ya)
                            return ya
                            flag=False
                        else:
                            break
                

        #_for period 1
        if p1 != []:
            tchr1=tr_selector(p1,P1,named)
            if tchr1 != None:
                final_list[0]=tchr1
            else:
                final_list[0]="self study"

        #_for period 2
        if p2 != []:
            tchr2=tr_selector(p2,P2,named)
            if tchr2 != None:
                final_list[1]=tchr2
            else:
                final_list[1]="self study"

        #_for period 3
        if p3 != []:
            tchr3=tr_selector(p3,P3,named)
            if tchr3 != None:
                final_list[2]=tchr3
            else:
                final_list[2]="self study"

        #_for period 4
        if p4 != []:
            tchr4=tr_selector(p4,P4,named)
            if tchr4 != None:
                final_list[3]=tchr4
            else:
                final_list[3]="self study"

        #_for period 5
        if p5 != []:
            tchr5=tr_selector(p5,P5,named)
            if tchr5 != None:
                final_list[4]=tchr5
            else:
                final_list[4]="self study"

        #_for period 6
        if p6 != []:
            tchr6=tr_selector(p6,P6,named)
            if tchr6 != None:
                final_list[5]=tchr6
            else:
                final_list[5]="self study"
        #_for period 7
        if p7 != []:
            tchr7=tr_selector(p7,P7,named)
            if tchr7 != None:
                final_list[6]=tchr7
            else:
               final_list[6]="self study"

        #_for period 8
        if p8 != []:
            tchr8=tr_selector(p8,P8,named)
            if tchr8 != None:
                final_list[7]=tchr8
            else:
                final_list[7]="self study"

        #The grand total list is: "
        print()
        print("The substitution for ",name ," is: ", final_list)
        
    

        # writing these in a excel file

        ttp=open(r'G:\Time Table\print table.csv','w')
        writer=csv.writer(ttp)
        
            
        st="The name of teacher: ", name
        writer.writerow(st)
        

        writer.writerow(final_list)
        
        writer.writerows('')
        u.close()
        ttp.close()

        t.close()

    else:
        print()
        print("The entered name ",name," not found in the teachers list" )
