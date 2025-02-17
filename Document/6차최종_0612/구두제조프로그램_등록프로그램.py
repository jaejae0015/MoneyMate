import sqlite3 #db import
from tkinter import *
from tkinter import ttk # for 콤보박스 사용
from tkinter import messagebox
import tkinter
import tkinter.ttk

#con, cur=None,None #연결자,커서
#Code,Name,Sex,Color,Height=None,None,None,None,None #전역변수
#sql=""#DB명령어변수

con,cur=None,None
con=sqlite3.connect("A상사DB.db")
cur=con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS 제품TB (Code char(5) PRIMARY KEY , Name char(6), Sex char(2), Color char(7), Height char(4),Quantity int, Input int, Output int)")


#메세지 함수
def messageboxdef1():
    messagebox.showinfo('알림','현재 페이지입니다.')
def messageboxdef3():
    messagebox.showinfo('알림','제품이 삭제되었습니다.')
def messageboxdef4():
    messagebox.showinfo('알림','제품등록이 취소되었습니다.')
#def exitdef():
#    window1.quit()
#    import 구두제조프로그램_서지애
def inputdef():
    window1.destroy()
    import 구두제조프로그램_입고처리프로그램
def outdef():
    window1.destroy()
    import 구두제조프로그램_출고처리프로그램
def checkdef():
    window1.destroy()
    import 구두제조프로그램_조회처리프로그램_복사본


#데이터 입력함수
    
def insertdata():
    con, cur=None,None #연결자,커서
    Code,Name,Sex,Color,Height="","","","",""#전역변수
    sql=""
    con=sqlite3.connect("A상사DB.db")
    cur=con.cursor()
    
    Codedata=[]

    sql="SELECT Code FROM 제품TB"
    cur.execute(sql)
    
    #Code=combo5.get()
    Code=edt1.get()
    Name=combo1.get()
    Sex=combo4.get()
    Color=combo2.get()
    Height=combo3.get()    
    Codedata.append("제품코드")

    
    while(True):
        row=cur.fetchone()
        if row==None:
            break;
        
        Codedata.append(row[0])

    for i in Codedata:
        
        if (Code == i):
            messagebox.showerror('오류','제품 정보 존재')
            break
        
        elif (Code==""):
            messagebox.showinfo('오류',"코드를 입력하세요.")
            break
        
        else:    
            try:
                sql="INSERT INTO 제품TB VALUES('"+Code+"','"+Name+"','"+Sex+"','"+Color+"','"+Height+"',0,0,0)"
                cur.execute(sql)
                
            except:
                messagebox.showerror('오류','제품 정보 존재')
                break
                
            else:
                messagebox.showinfo('성공','제품 등록 성공.')
                treeview=tkinter.ttk.Treeview(window1, columns=("0","1","2","3","4"))
                treeview.pack()

                treeview.column("#0", width=160)
                treeview.heading("#0", text="제품코드")
                treeview.column("#1", width=150)
                treeview.heading("#1", text="제품명")
                treeview.column("#2", width=80)
                treeview.heading("#2", text="성별")
                treeview.column("#3", width=160)
                treeview.heading("#3", text="제품색상")
                treeview.column("#4", width=80)
                treeview.heading("#4", text="제품높이")
                treeview.column("#5", width=90)
                treeview.heading("#5", text="제품재고")
                treeview.place(x=30,y=180)
                treeview.place(height=340)
                Tlist=[]


                sql="SELECT * FROM 제품TB"
                cur.execute(sql)

                while(True):
                    row=cur.fetchone()
                    if row==None:
                        break;
                    Code1=row[0]
                    Name1=row[1]
                    Sex1=row[2]
                    Color1=row[3]
                    Height1=row[4]
                    Quantity1=row[5]
                    
                    Tlist=[(Name1,Sex1,Color1,Height1,Quantity1)]
                    treeview.insert("",'end',text=Code1,values=Tlist[0])
    
                break
    
                
    con.commit()
    con.close()
    
#데이터 취소함수

    
#데이터 삭제함수-리스트에 코드를 담고, 돌린다음에 그거랑 일치하면 삭제함.    
def deletedata():
    
    con,cur,cur1,cur2=None,None,None,None
    con=sqlite3.connect("A상사DB.db")
    
    Quantity=[]
    Codein=edt1.get()
    
    cur=con.cursor()
    cur1=con.cursor()
    cur2=con.cursor()
    
    sql="SELECT Quantity FROM 제품TB WHERE Code='"+Codein+"'"
    cur.execute(sql)

    while(True):
        row=cur.fetchone()
        if row==None:
            break
        Quantity.append(row[0])
    
    su=Quantity[0]
    su=int(su)
    if(su>0):
        mms= messagebox.askokcancel("확인","현재 재고량이 존재합니다.\n 삭제하시겠습니까?")
        if mms==True:
                sql="DELETE FROM 제품TB WHERE Code='"+Codein+"'"
                cur.execute(sql)
                sql="DELETE FROM 입고TB WHERE Code='"+Codein+"'"
                cur1.execute(sql)
                sql="DELETE FROM 출고TB WHERE Code='"+Codein+"'"
                cur2.execute(sql)
                
                treeview=tkinter.ttk.Treeview(window1, columns=("0","1","2","3","4"))
                treeview.pack()

                treeview.column("#0", width=160)
                treeview.heading("#0", text="제품코드")
                treeview.column("#1", width=150)
                treeview.heading("#1", text="제품명")
                treeview.column("#2", width=80)
                treeview.heading("#2", text="성별")
                treeview.column("#3", width=160)
                treeview.heading("#3", text="제품색상")
                treeview.column("#4", width=80)
                treeview.heading("#4", text="제품높이")
                treeview.column("#5", width=90)
                treeview.heading("#5", text="제품재고")
                treeview.place(x=30,y=180)
                treeview.place(height=340)
                Tlist=[]


                sql="SELECT * FROM 제품TB"
                cur.execute(sql)

                while(True):
                    row=cur.fetchone()
                    if row==None:
                        break;
                    Code1=row[0]
                    Name1=row[1]
                    Sex1=row[2]
                    Color1=row[3]
                    Height1=row[4]
                    Quantity1=row[5]
                    
                    Tlist=[(Name1,Sex1,Color1,Height1,Quantity1)]
                    treeview.insert("",'end',text=Code1,values=Tlist[0])
        else:
                treeview=tkinter.ttk.Treeview(window1, columns=("0","1","2","3","4"))
                treeview.pack()

                treeview.column("#0", width=160)
                treeview.heading("#0", text="제품코드")
                treeview.column("#1", width=150)
                treeview.heading("#1", text="제품명")
                treeview.column("#2", width=80)
                treeview.heading("#2", text="성별")
                treeview.column("#3", width=160)
                treeview.heading("#3", text="제품색상")
                treeview.column("#4", width=80)
                treeview.heading("#4", text="제품높이")
                treeview.column("#5", width=90)
                treeview.heading("#5", text="제품재고")
                treeview.place(x=30,y=180)
                treeview.place(height=340)
                Tlist=[]


                sql="SELECT * FROM 제품TB"
                cur.execute(sql)

                while(True):
                    row=cur.fetchone()
                    if row==None:
                        break;
                    Code1=row[0]
                    Name1=row[1]
                    Sex1=row[2]
                    Color1=row[3]
                    Height1=row[4]
                    Quantity1=row[5]
                    
                    Tlist=[(Name1,Sex1,Color1,Height1,Quantity1)]
                    treeview.insert("",'end',text=Code1,values=Tlist[0])
            
            
    else:
                mms=messagebox.showinfo("확인","현재 재고량이 없으므로 삭제를 진행합니다.")
                sql="DELETE FROM 제품TB WHERE Code='"+Codein+"'"
                cur.execute(sql)
                treeview=tkinter.ttk.Treeview(window1, columns=("0","1","2","3","4"))
                treeview.pack()

                treeview.column("#0", width=160)
                treeview.heading("#0", text="제품코드")
                treeview.column("#1", width=150)
                treeview.heading("#1", text="제품명")
                treeview.column("#2", width=80)
                treeview.heading("#2", text="성별")
                treeview.column("#3", width=160)
                treeview.heading("#3", text="제품색상")
                treeview.column("#4", width=80)
                treeview.heading("#4", text="제품높이")
                treeview.column("#5", width=90)
                treeview.heading("#5", text="제품재고")
                treeview.place(x=30,y=180)
                treeview.place(height=340)
                Tlist=[]


                sql="SELECT * FROM 제품TB"
                cur.execute(sql)

                while(True):
                    row=cur.fetchone()
                    if row==None:
                        break;
                    Code1=row[0]
                    Name1=row[1]
                    Sex1=row[2]
                    Color1=row[3]
                    Height1=row[4]
                    Quantity1=row[5]
                    
                    Tlist=[(Name1,Sex1,Color1,Height1,Quantity1)]
                    treeview.insert("",'end',text=Code1,values=Tlist[0])
            
    con.commit()#반드시 있어야함
    con.close()
    
#데이터전체 삭제함수-리스트에 코드를 담고, 돌린다음에 그거랑 일치하면 삭제함.    
def deletealldata():
    
    con,cur=None,None
     
    sql=""
    con=sqlite3.connect("A상사DB.db")
    cur=con.cursor()
    
    sql="SELECT * FROM 제품TB"
    cur.execute(sql)
    sql="DELETE FROM 제품TB"
    cur.execute(sql)
    messagebox.showinfo('성공','전체 제품 삭제 성공.')

    
    con.commit()#반드시 있어야함
    con.close()
     
#데이터 조회함수
#def selectdata():
   # LabelFont=('times',13,'bold')
   # fontlist=('굴림',10,'normal')
   # row=None
   # con, cur=None,None
   # sql=""
   # #Codedata,Namedata,Sexdata,Colordata,Heightdata=[],[],[],[],[]
    
   # con=sqlite3.connect("A상사DB.db")
   # cur=con.cursor()
   # sql="SELECT * FROM 제품TB"
   # cur.execute(sql)
    
   
    
    
    
    #lab1=Label(window, text="          제품코드                              제품명                        성별                      제품색상                    높이   ")
    #lab1.config(font=LabelFont)    
    #lab1.place(x=40,y=180)
    #lab2=Label(window, text="---------------------------------------------------------------------------------------------------------------------")
    #lab2.config(font=LabelFont)
    #lab2.place(x=40,y=200)
    #while(True):
    #    row=cur.fetchone()
    #    if row==None:
    #        break;
    #    Codedata.append(row[0])
    #    Namedata.append(row[1])
    #    Sexdata.append(row[2]) 
    #    Colordata.append(row[3])
    #    Heightdata.append(row[4])

        
    #listdata1=Listbox(window,bg='#D4F4FA',font=fontlist)#코드
    #listdata1.place(x=40,y=225)
    #listdata1.config(height=20,width=25)
    #listdata2=Listbox(window,bg='#D4F4FA',font=fontlist)#제품명
    #listdata2.place(x=220,y=225)
    #listdata2.config(height=20,width=25)
    #listdata3=Listbox(window,bg='#D4F4FA',font=fontlist)#성별
    #listdata3.place(x=400,y=225)
    #listdata3.config(height=20,width=12)
    #listdata4=Listbox(window,bg='#D4F4FA',font=fontlist)#색상
    #listdata4.place(x=490,y=225)
    #listdata4.config(height=20,width=25)
    #listdata5=Listbox(window,bg='#D4F4FA',font=fontlist)#높이
    #listdata5.place(x=670,y=225)
    #listdata5.config(height=20,width=12)
    
    #for item1,item2,item3,item4,item5 in zip(Codedata,Namedata,Sexdata,Colordata,Heightdata):
        #listdata1.insert(END,item1)
        #listdata2.insert(END,item2)
        #listdata3.insert(END,item3)
        #listdata4.insert(END,item4)
        #listdata5.insert(END,item5)


   # con.close()
        
#정보띄우기함수
#def infoput():
#    item=treeview.focus()
#    print (treeview.item)

#def infoput(event):
#           curitem=treeview.focus()
#           it=treeview.item(curitem)
#           
#           Code=it['text']
#           VA=it['values']
#           
#           edt1=Entry(window1)
#           edt1.insert(0,Code)
#           edt1.place(x=125,y=25)#
#
#           edt2=Entry(window1)
#           edt2.insert(0,VA.pop(0))
#           edt2.place(x=385,y=25)
##
#
#           edt3=Entry(window1)
#           edt3.config(width=10)
#           edt3.insert(0,VA.pop(0))
#           edt3.place(x=125,y=65)
#
#           edt4=Entry(window1)
#           edt4.insert(0,VA.pop(0))
#           edt4.place(x=350,y=65)

#           edt5=Entry(window1)
#           edt5.insert(0,VA.pop(0))
#           edt5.config(width=10)
#           edt5.place(x=620,y=65)

def infoput(Code):
    
        curitem=treeview.focus()
        it=treeview.item(curitem)
           
        Code=it['text']
        edt1.insert(0,Code)
        edt1.place(x=125,y=25)

        return Code

window1=Tk()
window1.title("A상사 구두제품등록 Page")
window1.geometry("800x600")
window1.resizable(False, False)

#con=sqlite3.connect("c:\A상사\등록DB")
#cur=con.cursor()
#cur.execute("CREATE TABLE 제품TB (Code char(5) PRIMARY KEY , Name char(6), Sex char(2), Color char(7), Height char(4),Quantity int)")


    
menubar=Menu(window1)
filemenu=Menu(menubar)
menubar.add_cascade(label="제품등록",command=messageboxdef1)
menubar.add_cascade(label="제품입고",command=inputdef)
menubar.add_cascade(label="제품출고",command=outdef)
menubar.add_cascade(label="제품조회",command=checkdef)
menubar.add_cascade(label="  종료  ",command=window1.destroy)
window1.config(menu=menubar)

label1=Label(window1, text="제품코드 :")
label1.config(height=3,width=10)
label1.place(x=40,y=5)
#Code=StringVar()#콤보박스와 연동할 변수
#combo5= ttk.Combobox(window, width=10, textvariable=Code)#변수와 콤보박스 연동
#combo5['values'] = ('0001','0002','0003','0004','0005','0006','0007','0008','0009','0010','0011','0012','0013','0014','0015')
#combo5.place(x=120,y=25)
#combo5.current(0)#기본값 설정
edt1=Entry(window1)
Code=edt1.get()
edt1.place(x=125,y=25)


label2=Label(window1, text="제품명 :")
label2.config(height=0,width=0)
label2.place(x=320,y=25)
Name=StringVar()#콤보박스와 연동할 변수
combo1= ttk.Combobox(window1, width=20, textvariable=Name)#변수와 콤보박스 연동
combo1['values'] = ('로퍼', '첼시부츠', '메리제인' , '펌프스','플랫슈즈')
combo1.place(x=385,y=25)
combo1.current(0)#기본값을 로퍼로 설정
#combo1=Entry(window1)
#combo1.place(x=385,y=25)

label3=Label(window1, text="성  별 :")
label3.config(height=3,width=10)
label3.place(x=45,y=50)
Sex=StringVar()#콤보박스와 연동할 변수
combo4= ttk.Combobox(window1, width=10, textvariable=Sex)#변수와 콤보박스 연동
combo4['values'] = ('남', '여')
combo4.place(x=130,y=65)
combo4.current(0)#기본값 설정
#combo4=Entry(window1)
#combo4.place(x=125,y=65)

label4=Label(window1, text="제품색상 :")
label4.config(height=3,width=7)
label4.place(x=275,y=50)
#콤보박스와 연동할 변수
Color=StringVar()
combo2= ttk.Combobox(window1, width=20, textvariable=Color)#변수와 콤보박스 연동
combo2['values'] = ('Navy', 'Beige' , 'Wine')
combo2.place(x=350,y=65)
combo2.current(0)#기본값 설정
#combo2=Entry(window1)
#combo2.place(x=375,y=65)

label5=Label(window1, text="제품높이 :")
label5.config(height=3,width=7)
label5.place(x=550,y=50)
Height=StringVar()#콤보박스와 연동할 변수
combo3= ttk.Combobox(window1, width=10, textvariable=Height)#변수와 콤보박스 연동
combo3['values'] = ('0cm', '3cm', '5cm' , '7cm')
combo3.place(x=620,y=65)
combo3.current(0)#기본값 설정
#combo3=Entry(window1)
#combo3.place(x=620,y=65)

btn1=Button(window1,text="등 록",command=insertdata)
btn1.place(x=540,y=110)
btn1.place(height=40,width=100)


btn2=Button(window1,text="삭 제",command=deletedata)
btn2.place(x=640,y=110)
btn2.place(height=40,width=100)

#btn4=Button(window1,text="제품 LIST 확인",command=selectdata)
#btn4.place(x=640,y=110)
#btn4.place(height=40,width=100)

#btn5=Button(window1,text="제품 LIST 삭제",command=deletealldata)
#btn5.place(x=640,y=520)
#btn5.place(height=40,width=100)

 
treeview=tkinter.ttk.Treeview(window1, columns=("0","1","2","3","4"))
treeview.pack()

treeview.column("#0", width=160)
treeview.heading("#0", text="제품코드")
treeview.column("#1", width=150)
treeview.heading("#1", text="제품명")
treeview.column("#2", width=80)
treeview.heading("#2", text="성별")
treeview.column("#3", width=160)
treeview.heading("#3", text="제품색상")
treeview.column("#4", width=80)
treeview.heading("#4", text="제품높이")
treeview.column("#5", width=90)
treeview.heading("#5", text="제품재고")
treeview.place(x=30,y=180)
treeview.place(height=340)
Tlist=[]
i=0
#treeview.bind("<ButtonRelease-1>",infoput)

con,cur=None,None
con=sqlite3.connect("A상사DB.db") 
cur=con.cursor()

sql="SELECT * FROM 제품TB"
cur.execute(sql)

while(True):
    i=i+1
    row=cur.fetchone()
    if row==None:
        break;
    Code=row[0]
    Name=row[1]
    Sex=row[2]
    Color=row[3]
    Height=row[4]
    Quantity=row[5]
    
    Tlist=[(Name,Sex,Color,Height,Quantity)]
    treeview.insert("",'end',text=Code, values=Tlist[0],tags=i)
    treeview.tag_bind(i,"<ButtonRelease-1>",callback=infoput)
    
    #treeview.tag_bind(i,"<Double-Button-2>",callback=inputput)
#treeview.tag_bind("one",sequence="<<TreeviewSelect>>",callback=infoput)
#treeview.bind('<Button>',infoput)
con.close()



#btn6=Button(window1,text="취 소",command=resetdata)
#btn6.place(x=340,y=100)
#btn6.place(height=40,width=80)

label5=Label(window1, text="====================================================================")
label5.pack(expand=YES,fill=BOTH)
label5.place(x=50,y=150)

def center_window(width=300, height=200):
    # get screen width and height
    screen_width = window1.winfo_screenwidth()
    screen_height = window1.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    window1.geometry('%dx%d+%d+%d' % (width, height, x, y))
    
center_window(800,600)



window1.mainloop()
