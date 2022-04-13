import datetime
def control(l):
    nr=[2,7,9,1,4,6,3,5,8,2,7,9]
    sum=0
    for i, value in enumerate(nr):
        sum = sum + (int(value)*int(l[i]))
    rest=sum%11
    return rest

cnp = input(" cnp-ul este: ")
list_cnp=[]
for item in cnp:
    list_cnp.append(item)
while True:
    if len(list_cnp)==13:
        if list_cnp[0]=='1' or list_cnp[0] == '2':
            print("născuți între 1 ianuarie 1900 și 31 decembrie 1999")
        elif list_cnp[0]=='3' or list_cnp[0] == '4':
            print("născuți între 1 ianuarie 1800 și 31 decembrie 1899")
        elif list_cnp[0]=='5' or list_cnp[0] == '6':
            print("născuți între 1 ianuarie 2000 și 31 decembrie 2099")
        elif list_cnp[0]=='7' or list_cnp[0] == '8':
            print("pentru persoanele străine rezidente în România")
        else:
            print("pentru persoanele străine")
        AA=int(list_cnp[1]+list_cnp[2])
        LL=int(list_cnp[3]+list_cnp[4])
        ZZ=int(list_cnp[5]+list_cnp[6])
        JJ=int(list_cnp[7]+list_cnp[8])
        NNN=int(list_cnp[9]+list_cnp[10]+list_cnp[11])
        c=int(list_cnp[12])
        data = '{}/{}/{}'.format(ZZ,LL,AA)
        print(datetime.datetime.strptime(data, '%d/%m/%y'))
        if JJ < 1 and JJ > 46 and JJ < 51 and JJ > 52:
            print("CNP-ul nu este valid")
            break
        if NNN < 1:
            print("CNP-ul nu este valid")
            break
        check_control=control(list_cnp)
        print("Check control: " + str(check_control))
        if check_control == 10:
            if c == 1:
                pass
            else:
                print("CNP-ul nu este valid")
                break
        else:
            if c==check_control:
                pass
            else:
                print("CNP-ul nu este valid")
                break
    print("CNP valid")
    break