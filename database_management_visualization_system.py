import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import mysql.connector as sq

#Connect Mysql
con=sq.connect(host='localhost',user='root',passwd='root')
m=con.cursor()

#DATABASE MANAGEMENT AND VISUALIZATION SYSTEM 
while True:
       print('__'*40)
       print('''
          _____________________________________________________________
         |                                                                                                                 |
         |                                                                                                                 |
         |     DATABASE MANAGEMENT AND VISUALIZATION SYSTEM         |
         |                                                                                                                 |
         |_____________________________________________________________|\n''')
       
       print('__'*40)
       mke=int(input('''\n\nWhat Do You Wants To Make :

Enter 1 For DataFrame

Enter 2 For Graph

Enter 3 For Student Data In Mysql

Enter 4 For Exit

Enter Choice Number : '''))
       print('''\n''')
       print('__'*30)
       #DataFrame All Creation
       def dtaframe():
           while True:
                  print('''
                        ++++++++++++++++++++++++
                        +                                                +    
                        +   DATAFRAME DATABASE   +
                        +                                                +
                        ++++++++++++++++++++++++\n''')
                  print('__'*30)
                  print('''\n''')
                  dta_in=int(input('''What You Want.....

Enter 1 Create New DataFrame

Enter 2 For Read Csv File

Enter 3 For Main Menu

Enter Your Choice : '''))
                  print('''\n''')
                  if dta_in==1:
                      print(dta_dtaframe())
                  elif dta_in==2:
                      print(read_dta())
                  elif dta_in==3:
                         break
                  else:
                      print('Invalid Argument')
          
           
           return ''
       #Created def Functin For Dataframe
       def dta_dtaframe():
           print('''\n''')
           #Access How Many Values And Columns For Users
           print('__'*30)
           print('\n')
           print('--'*30)
           n=int(input('Enter How Many Column : '))
           print('--'*30)
           v=int(input('Enter How Many Values : '))
           
           a=[]
           b=[]
           d={}   
           #Enter Value And Column Name
           for i in range(n):
               print('--'*30)
               key=input('Enter Column Name : ')
               a=[]
               for k in range(v):
                   print('--'*30)
                   val=input('Enter Values : ')
                   a.append(val)
                   d[key]=a
               
           #Enter Label Index For DataFrame
           print('--'*30)
           print('\n')
           print('__'*30)
           ind=int(input('''\nIf You Wants To Add Label Index :

Enter 1 For Yes

Enter 2 For No

Enter Choice Number : '''))
           print('''\n''')
           print('__'*30)
           for p in range(v):
               if ind==1:
                   print('--'*30)
                   va=input('Enter Label Name : ')
                   print('--'*30)
                   b.append(va)
               elif ind==2:
                   break
               else:
                   print('Noooo...You...Are...Wrong...Please..Correct..Yourself')

           if ind==1:
               print('\n')
               print('__'*30)
               print('\n')
               df=pd.DataFrame(d,index=b)
               print(df)
           else:
               print('\n')
               print('__'*30)
               print('\n')
               df=pd.DataFrame(d)
               print(df)
          
           
           #Save DataFrame File In csv
           print('__'*30)
           print('\n')
           
           s=int(input('''\nDo You Wants To Save It :

Enter 1 For Yes

Enter 2 For No

Enter Choice Number : '''))
           print('''\n''')
           print('__'*30)
           if s==1:
               print('\n')
               print('--'*30)
               fname=input('Enter File Name : ')
               df.to_csv(fname+'.csv')
               print('--'*30)
               print('__'*40)
               print('''Check Path: C:\\Users\\Admin\\AppData\\Local\\Programs\\Python\\Python37-32\\'''+fname+'.csv')
               print('__'*40)
               print('\n')
           elif s==2:
               print('>>'*30)
               print("Be Happy....:")
               print('>>'*30)
               #Save File Read
               
           else:
               print("Be Happy....:)....Please Choose Correct Option")
          
           return ''
       #Read Dataframe File
       def read_dta():
              
           print('''\n''')
           print('--'*30)
           f_name=input('Enter File Name : ')
           print('--'*30)
           rea=pd.read_csv(f_name+'.csv',index_col=[0])
           print('__'*30)
           print('''\n''')
           print(rea)
           print('''\n''')
           print('__'*30)
           return ''
       #Created Graph Function
       def graph():
              
              while True:
                     print('__'*30)
                     print('''
                                   #>>>>>>>>>>>>>>>>>>>>>>>>>#
                                   #                                                      # 
                                   #        MATPLOTLIB GRAPH          #
                                   #                                                      #
                                   #>>>>>>>>>>>>>>>>>>>>>>>>>#\n''')
                            
                     print('__'*30)
                     print('''\n''')
                     x=[]
                     y=[]
                     g=int(input('''Which Graph You Makes :

Enter 1 For Line Graph

Enter 2 For Bar Graph

Enter 3 For Barh Graph

Enter 4 For Main Menu

Enter Choice Number : ''')) 
                     
                     if g==1 or g==2 or g==3:
                            print('--'*30)
                            n=int(input('Enter How Many Values : '))
                            #Add X And Y Axis Values In Graph
                            for i in range(n):
                                   print('--'*30)
                                   val=input("Enter Values For X-Axis : ")
                                   print('--'*30)
                                   va=eval(input("Enter Values For Y-Axis : "))
                                   print('--'*30)
                                   x.append(val)
                                   y.append(va)
                              #Access Values Which User Input
                            if g==1:
                                   plt.plot(x,y)
                            elif g==2:
                                   plt.bar(x,y)
                            elif g==3:
                                   plt.barh(x,y)
                     elif g==4 :
                           break
                     else:
                            print("Invalid Number Argument")
                            break
                   
                     
                    
                  
                     ti=int(input('''Do You Want To Enter Title :

Enter 1 For Yes

Enter 2 For No

Enter Choice Number : '''))
                            
                     print('__'*30)
                     print('''\n''')           
                     #Add Title In Graph
                     if ti==1:
                            print('--'*30)
                            title=input('Enter Title Name : ')
                            print('--'*30)
                            plt.title(title.upper())
                     elif ti==2:
                            print('__'*30)
                            print('Keep...Smile...')
                            print('__'*30)
                     else:
                            print("Don't Worry...Try It Again....")
                     print(label_graph())
                     print(sav_graph())              
                     plt.show()
                  
              return ''
       #label For Graph
       def label_graph():
              #Add X And Y Axis Labels In Graph
              print('__'*30)
              print('''\n''')
              rt =int(input('''\nDo you Want To Enter Axis Label Or Not :

Enter 1 For Yes

Enter 2 For No

Enter choice Number : '''))
              print('__'*30)
              print('''\n''')
                         

              if rt==1:                       
                     print('--'*30)
                     x1=input('Enter X-Axis Label Name : ')
                     print('--'*30)
                     y1=input('Enter Y-Axis Label Name : ')
                     print('--'*30)
                     plt.xlabel(x1.upper())
                     plt.ylabel(y1.upper())
              
              elif rt==2:
                     print('''\n''')
                     print('__'*30)
                     print("I'm...With...You....")
                     print('__'*30)
                     print('''\n''')
                     
              else:
                     print("I'm With You....Please Do It Again....")
              return ''


       #Save Graph
       def sav_graph():
           print('__'*30)
           sav=int(input('''Do You Want To Save Graph :

Enter 1 For yes

Enter 2 For no

Enter Choice Number : '''))
           print('''\n''')
           print('__'*30)
           
           if sav==1:
               print('--'*30)
               fi=input('Enter File Name : ')
               print('--'*30)
               plt.savefig(fi+'.png')
               print('--'*40)
               print('''Check Path: C:\\Users\\Admin\\AppData\\Local\\Programs\\Python\\Python37-32\\'''+fi+'.png')
               print('--'*40)
           else:
               print('__'*30)
               print('As Your Wish!....')
               print('__'*30)
           return ''
       
       #Update Mysql Data
       def update_dta():
           change=int(input('''\nWhat You Want To Change

Enter 1 For Name

Enter 2 For Class

Enter 3 For DOB

Enter 4 For Father Name 

Enter 5 For Mobile Number

Enter Your Choice : '''))
           print('__'*30)
           print('''\n''')
           if change==1:
               print('..'*30)
               new_name=input('Enter New Name : ')
               print('..'*30)
               ad_no=int(input('Enter Admission Number : '))
               print('..'*30)
               sql_1='update student_data set Name=%s Where AdmissionNo=%s'
               new_val=(new_name,ad_no)
               m.execute(sql_1,new_val)
               con.commit()
               print(m.rowcount,'Record Updated')
               print('..'*30)
           elif change==2:
               print('..'*30)
               new_clss=input('Enter New Class Format(Int) : ')
               print('..'*30)
               ad_no=int(input('Enter Admission Number : '))
               print('..'*30)
               sql_2='update student_data set Class=%s Where AdmissionNo=%s'
               new_val2=(new_clss,ad_no)
               m.execute(sql_2,new_val2)
               con.commit()       
               print(m.rowcount,'Record Updated')
               print('..'*30)
           elif change==3:
               print('..'*30)
               new_dob=input('''Enter New DOB Format('YYYY-MM-DD') : ''')
               print('..'*30)
               ad_no=int(input('Enter Admission Number : '))
               print('..'*30)
               sql_3='update student_data set dob=%s Where AdmissionNo=%s'
               new_val3=(new_dob,ad_no)
               m.execute(sql_3,new_val3)
               con.commit()
               print(m.rowcount,'Record Updated')
               print('..'*30)
           elif change==4:
               print('..'*30)
               new_fname=input('Enter Changed Father Name : ')
               print('..'*30)
               ad_no=int(input('Enter Admission Number : '))
               print('..'*30)
               sql_4='update student_data set FatherName=%s Where AdmissionNo=%s'
               new_val4=(new_fname,ad_no)
               m.execute(sql_4,new_val4)
               con.commit()
               print(m.rowcount,'Record Updated')
               print('..'*30)
           elif change==5:
               print('..'*30)
               new_mob=input('Enter New Mobile Number : ')
               print('..'*30)
               ad_no=int(input('Enter Admission Number : '))
               print('..'*30)
               sql_5='update student_data set mobileNo=%s Where AdmissionNo=%s'
               new_val5=(new_mob,ad_no)
               m.execute(sql_5,new_val5)
               con.commit()
               print(m.rowcount,'Record Updated')
               print('..'*30)
                   
           else:
               print('KEEP SMILE :).....Please Choose Correct Option.... ')
           return ''
       #Insert Data Send To Mysql
       def insert_dta():
           print('**'*30)
           n_data=int(input('Enter How Many Data : '))
           for i in range(n_data):
               print('**'*30)
               admin=int(input('Enter Your Admission Number : '))            
               print('**'*30)
               nam=input('Enter Your Name : ')
               print('**'*30)
               clss=input('Enter Your Class Format(Int) : ')
               print('**'*30)
               dob=input('Enter Your Data Of Birth Format(YYYY-MM-DD) : ')
               print('**'*30)
               father=input('Enter Your Father Name : ')
               print('**'*30)
               mob=int(input('Enter Your Mobile Number : '))
               print('**'*30)
               print('''\n''')
               print('__'*30)
               sql='insert into student_data(AdmissionNo,Name,class,dob,FatherName,mobileNo) values(%s,%s,%s,%s,%s,%s)'
               val=(admin,nam,clss,dob,father,mob)
               m.execute(sql,val)
               con.commit()
           print('Record Inserted....')
           print('__'*30)
           return ''
       #Delete Record                
       def delete_record():
           del_dta=int(input('''How Many Record You Want To Delete

Enter 1 For Specific Record

Enter 2 For Delete All Record

Enter Your Choice : '''))
           
           print('__'*30)
           print('''\n''')
           if del_dta==1:
               
               cls_dta=int(input('''How You Want To Delete

Enter 1 For Admission Number

Enter 2 For Class Wise

Enter Your choice : '''))
               print('__'*30)
               print('''\n''')
               if cls_dta==1:
                   print('<>'*30)
                   ad_in=int(input('Enter Admission Number : '))
                   print('<>'*30)
                   sql_del='delete from student_data Where AdmissionNo=%s'
                   ad_del=(ad_in,)
                   m.execute(sql_del,ad_del)
                   con.commit()
                   print(m.rowcount,'Record Deleted By Admission Number....')
                   print('<>'*30)
               elif cls_dta==2:
                   print('<>'*30)
                   ad_cl=int(input('Enter Class Name Format(Int) : '))
                   print('<>'*30)
                   sql_del2='delete from student_data Where class=%s'
                   print('<>'*30)
                   ad_del=(ad_cl,)
                   m.execute(sql_del2,ad_del)
                   con.commit()
                   print(m.rowcount,'Record Deleted By Class....')
                   print('<>'*30)
               else:
                   print('Invalid Argument....')
           elif del_dta==2:
               sql_del3='delete from student_data'
               m.execute(sql_del3,)
               con.commit()
               print('<>'*30)
               print(m.rowcount,'Record Deleted....')
               print('<>'*30)
                   
               
           else:
               print('Invalid Argument....')
           return ''
       #Tuple Convert Into List
       def f(t):
              if type(t)==list or type(t)==tuple:
                     return [f(i) for i in t]
              return t
       #Serach Record
       def serch_dta():
           ser_dta=int(input('''Search Record You Want

Enter 1 For Admission Number

Enter 2 For Class

Enter Your Choice : '''))
           print('__'*30)
           print('''\n''')
           if ser_dta==1:
               print('::'*30)
               admi=int(input('Enter Admission Number : '))
               print('::'*30)
               sel='select * from student_data where AdmissionNo=%s'
               sel_val=(admi,)
               m.execute(sel,sel_val)
               fall=m.fetchall()
               x=f(fall)
               lst2=['AdmissionNo','Name','Class','DOB','FatherName','MobileNo']
               dfx=pd.DataFrame(x,columns=lst2)
               dfx=dfx.to_string(index=False)
               print(dfx)          
               print('::'*30)
           elif ser_dta==2:
               print('::'*30)
               sel_cls=int(input('Enter Class Name : '))
               print('::'*30)
               sel2='select * from student_data where class=%s'
               sel_val2=(sel_cls,)
               m.execute(sel2,sel_val2)
               fall2=m.fetchall()
               c3=f(fall2)
               lst3=['AdmissionNo','Name','Class','DOB','FatherName','MobileNo']
               df3=pd.DataFrame(c3,columns=lst3)
               df3=df3.to_string(index=False)
               print(df3)          
               print('::'*30)
               
           else:
               print('Oo Noo...Invalid Argument....')
           
           return ''

       #Show All Data
       def show_dta():
           sel3='select * from student_data'
           m.execute(sel3)
           al=m.fetchall()
           c=f(al)
           lst=['AdmissionNo','Name','Class','DOB','FatherName','MobileNo']
           print('zz'*30)
           print('All Records Are.....')
           print('''\n''')
           df=pd.DataFrame(c,columns=lst)
           df=df.to_string(index=False)
           print(df)
           print('zz'*30)
           return ''

       #Marks Insert
       def marks_dta():
           print('**'*30)
           m_data=int(input('Enter How Many Data : '))
           for i in range(m_data):
               print('**'*30)
               admin2=int(input('Enter Your Admission Number : '))
               print('**'*30)
               t_1=int(input('Enter Total Term I Marks : '))
               print('**'*30)
               t_2=int(input('Enter Total Term II Marks : '))
               print('**'*30)
               total=t_1+t_2
               print('''\n''')
               print('__'*30)
               m_sql='insert into marks(AdmissionId,TermI,TermII,Total) values(%s,%s,%s,%s)'
               m_val=(admin2,t_1,t_2,total)
               m.execute(m_sql,m_val)
               con.commit()
           print('Record Inserted....')
           print('__'*30)
           return ''

       #marks Base Graph
       def m_graph():
           mr=pd.read_sql('select name,TermI,TermII,Total from student_data,marks where AdmissionNo=AdmissionId',con)
           x1=mr['name']
           y1=mr['TermI']
           y2=mr['TermII']
           y3=mr['Total']
           ls=np.arange(len(x1))
           plt.bar(x1,y1,width=.15,label='Term I')
           plt.bar(ls+0.15,y2,width=.15,label='Term II')
           plt.bar(ls+0.30,y3,width=.15,label='Total Marks')
           plt.title('Student Academic Performance'.upper())
           plt.xlabel('Student Name'.upper())
           plt.ylabel('Student Marks'.upper())
           plt.legend(loc='upper right')
           print(sav_graph())
           plt.show()
           return ''

       #ALL RECORD
       def std_data():
           print('''
                   |================================|
                   |                                                                     |
                   |  STUDENT DATABASE MANAGEMENT    | 
                   |                                                                     |
                   |================================|
                     ''')
           
           m.execute('create database if not exists school;')
           m.execute('use school;')
           m.execute('create table if not exists student_data(AdmissionNo int primary key,Name varchar(50),class int(2),DOB date,FatherName varchar(50),MobileNo varchar(10))')
           m.execute('create table if not exists marks(AdmissionId int primary key,TermI int(3) not null,TermII int(3) not null,Total int(3),foreign key(AdmissionId) references student_data(AdmissionNo) on delete cascade on update cascade)')
           
           while True:
              record=int(input('''\nWhat To Do.........

Enter 1 For Insert Record

Enter 2 For Update Record

Enter 3 For Delete Record

Enter 4 For Search Record

Enter 5 For Show All Student Record

Enter 6 For Add Student Marks

Enter 7 For Show Graph Student Marks Based

Enter 8 For Going Back To Main Menu

Enetr Your Choice : '''))
              print('''__'''*30)
              print('''\n''')
              try:
                     if record==1:
                            print(insert_dta())
                     else:
                            pass
              except:
                     print('Invalid...Data...Please...Check...?')
                     print('Also...Check...Admission...Number...Already...Exits...Or...Not...?')
                     print('__'*30)
              try:
                     
                     if record==2:
                            print(update_dta())
                     elif record==3:
                            print(delete_record())
                     elif record==4:
                            print(serch_dta())
                     elif record==5:
                            print(show_dta())
                     elif record==6:
                            print(marks_dta())
                     elif record==7:
                            print(m_graph())
                     elif record==8:
                            break
                     else:
                            print('Invaild Argument......')
                            print('__'*30)

              except:
                     print('Invalid...Data...Please...Check...?')
                     print('Also...Check...Admission...Number...Already...Exits...Or...Not...?')
                     print('__'*30)
           return ''

       #Call DataFrame,Matplotlib,Mysql Student Management
       if mke==1:
              print(dtaframe())

       elif mke==2:
              print(graph())
       elif mke==3:
              print(std_data())
       elif mke==4:
              print('''
        !!============================================!!
        !!                                                                                              !!
        !!  Bye...Bye...Have...A...Good...Day....:)                                   !!
        !!                                                                                               !!
        !!============================================!!\n''')
              print('__'*30)
              break
              
       else:
              print('Oo...So...Sorry...Invalid Argument....')
              print('__'*30)
       


