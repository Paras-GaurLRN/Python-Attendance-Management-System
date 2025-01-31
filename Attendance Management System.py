#Attendance Management System

import mysql.connector
import time

pawd = input('Enter Your MySQL Password: ')
connected = mysql.connector.connect(passwd=pawd,user='root',host='localhost')
cursor = connected.cursor()
cursor.execute('use attendance;')

print('# Put The File Students.txt In The Folder Where The File Is #')
print('# Attendance Management System #')

filestudent = open('Students.txt','r')
studentslistdot = filestudent.readlines()
studentslist = []

def listToString(s):
    str1 = ""
    for ele in s:
        str1 += ele
    return str1

for i in range(0,len(studentslistdot)):
    if '\n' in studentslistdot[i]:
        alpha =  studentslistdot[i]
        z = list(alpha)
        z.pop(-1)
        studentname = listToString(z)
        studentslist.append(studentname)
    else:
        studentslist.append(studentslistdot[i])

def saver():
    monthdateyearv = monthdateyear()
    global studentslist,cursor,connected
    tabname = f"{monthdateyearv}"
    tablecommand = f"create table {tabname}( \nName varchar(255) Not Null, \nAttendance char(1) Not Null); "
    #tablecommanddrop = f"drop table {tabname};"
    #cursor.execute(tablecommanddrop)
    cursor.execute(tablecommand)
    print('Type A/P for Absent/Present')
    for studentnumber in range(0,len(studentslist)):
        time.sleep(0.05)
        instext = f"'{studentslist[studentnumber]}' Present or Absent : "
        aorp = str(input(instext))
        if aorp.upper() == 'P':
            a :str = 'P'
        else:
            a :str = 'A'
        attendance = a
        inserttext = f"insert into {tabname} values(Name='{studentslist[studentnumber]}',Attendance='{attendance}');"
        cursor.execute(inserttext)
        connected.commit()
    return True

def monthdateyear():
    months = ('January','February','March','April','May','June','July','August','September','October','November','December')
    st31months = {31:('January','March','May','July','August','October','December')}
    st31monthslist :list = []
    st31monthslist.extend(st31months[31])
    st30months = {30:('April','June','September','November')}
    st30monthslist :list = []
    st30monthslist.extend(st30months[30])
    year = int(input('Enter Year In YYYY Form: '))
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                stfebmonth = {29:('February'),28:''}
                stfebmonthlist :list = []
                stfebmonthlist.extend(stfebmonth[29])
            else:
                stfebmonth = {28:('February'),29:''}
                stfebmonthlist :list = []
                stfebmonthlist.extend(stfebmonth[28])
        else:
            stfebmonth = {29:('February'),28:''}
            stfebmonthlist :list = []
            stfebmonthlist.extend(stfebmonth[29])
    else:
        stfebmonth = {28:('February'),29:''}
        stfebmonthlist :list = []
        stfebmonthlist.extend(stfebmonth[28])
    monthnumber = int(input('Enter Month Number (1 to 12) : '))
    monthname = months[monthnumber-1]
    for p in range(0,7):
        if monthname in st31monthslist:
            maxday=31
        elif monthname in st30monthslist:
            maxday=30
        elif monthname in stfebmonthlist:
            if stfebmonth[28] != '': 
                maxday=28
            elif stfebmonth[29] != '':
                maxday=29
    userdaytext = f'Enter The Day (Number 1 to {maxday}): '
    userday = int(input(userdaytext))
    if userday>=1 and userday <=maxday:
        pass
    else:
        userday = 00
    newday = '0'+str(userday)
    day = int(newday[len(newday)-2:len(newday)])
    if str(day)[-1] == '1':
        monthdateyear = f'{monthname}{day}st{year}'
    elif str(day)[-1] == '2':
        monthdateyear = f'{monthname}{day}nd{year}'
    elif str(day)[-1] == '3':
        monthdateyear = f'{monthname}{day}rd{year}'
    elif day == 00:
        monthdateyear = f'{monthname}00{year}'
    else:
        monthdateyear = f'{monthname}{day}th{year}'
    return monthdateyear

def viewer():
    monthdateyearv = monthdateyear()
    global cursor
    printertext = f"Attendence Of {monthdateyearv}"
    print('#',printertext,'#')
    monthdateyeartosearch = f"{monthdateyearv}"
    searchcommand = f"select * from {monthdateyeartosearch};"
    cursor.execute(searchcommand)
    lengtherlist = cursor.fetchall()
    lengther = len(lengtherlist)
    cursor.execute(searchcommand)
    studentnumber = 0
    while studentnumber<lengther:
        studentattendance = cursor.fetchone()
        print(studentattendance)
        studentnumber+=1
    return True


whilelooper = 1
time.sleep(0.5)
while whilelooper == 1:
    preintertextwhileloop = "Please Select An Operation: \n1) Create An Attendance Table \n2) View The Attendance A Day \n--> "
    operation = int(input(preintertextwhileloop))
    if operation == 1:
        done = saver()
        if done:
            pass
        else:
            whilelooper = 0
    elif operation == 2:
        done = viewer()
        if done:
            pass
        else:
            whilelooper = 0
    else:
        whilelooper = 0
    time.sleep(0.5)  