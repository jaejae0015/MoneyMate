import sqlite3
from datetime import datetime
from tkinter import *
from tkinter import ttk # for 콤보박스 사용
from tkinter import messagebox
import tkinter
import tkinter.ttk
import sqlite3
from datetime import datetime
    

def messageboxdef1():
    messagebox.showinfo('알림','현재 페이지입니다.')
def enrolldef():
    window4.destroy()
    import 구두제조프로그램_등록프로그램
def inputdef():
    window4.destroy()
    import 구두제조프로그램_입고처리프로그램
def outdef():
    window4.destroy()
    import 구두제조프로그램_출고처리프로그램

#조회 함수
def searchdata():
    code,name,height,color,sex="","","","",""
    sql=""
    con,cur1=None,None
    con=sqlite3.connect("A상사DB.db")
    cur1=con.cursor()
     
    code=combo1.get()
    name=combo2.get()
    sex=combo3.get()
    color=combo4.get()
    height=combo5.get()

    treeview=tkinter.ttk.Treeview(window4 , columns=("0","1","2","3","4"))
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
    treeview.place(x=30,y=220)
    treeview.place(height=340)
    Tlist=[]
    i=0
    #treeview.bind("<ButtonRelease-1>",infoput)
    if (code!=""):
        sql="SELECT * FROM 제품TB WHERE Code='"+code+"'"
        cur1.execute(sql)
        while(True):
            i=i+1
            row=cur1.fetchone()
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
            con.commit()
            
    elif (name!=""):
        if (sex==""):
            sql="SELECT * FROM 제품TB WHERE Name='"+name+"'"
            cur1.execute(sql)
            while(True):
                i=i+1
                row=cur1.fetchone()
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
                con.commit()
        elif(sex!=""):
            if (color==""and height==""):
                sql="SELECT * FROM 제품TB WHERE Name='"+name+"' And Sex='"+sex+"'"
                cur1.execute(sql)
                while(True):
                    i=i+1
                    row=cur1.fetchone()
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
                    con.commit()

                
            elif (color!=""and height==""):
                sql="SELECT * FROM 제품TB WHERE Name='"+name+"' And Sex='"+sex+"' And Color='"+color+"'"
                cur1.execute(sql)
                while(True):
                    i=i+1
                    row=cur1.fetchone()
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
                    con.commit()
            elif (color==""and height!=""):
                sql="SELECT * FROM 제품TB WHERE Name='"+name+"' And Sex='"+sex+"' And Height='"+height+"'"
                cur1.execute(sql)
                while(True):
                    i=i+1
                    row=cur1.fetchone()
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
                    con.commit()
            elif (color!=""and height!=""):
                sql="SELECT * FROM 제품TB WHERE Name='"+name+"' And Sex='"+sex+"' And Height='"+height+"' And Color='"+color+"'"
                cur1.execute(sql)
                while(True):
                    i=i+1
                    row=cur1.fetchone()
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
                    con.commit()
        elif(color!=""):
            if (height==""):
                sql="SELECT * FROM 제품TB WHERE Name='"+name+"' And Color='"+color+"'"
                cur1.execute(sql)
                while(True):
                    i=i+1
                    row=cur1.fetchone()
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
                    con.commit()
            elif(height!=""):
                sql="SELECT * FROM 제품TB WHERE Name='"+name+"' And Color='"+color+"'And Height='"+height+"'"
                cur1.execute(sql)
                while(True):
                    i=i+1
                    row=cur1.fetchone()
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
                    con.commit()
        elif(height!=""):
            sql="SELECT * FROM 제품TB WHERE Name='"+name+"' And Height='"+height+"'"
            cur1.execute(sql)
            while(True):
                i=i+1
                row=cur1.fetchone()
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
                con.commit()
    elif (sex!=""):
        if color=="" and height=="":
            sql="SELECT * FROM 제품TB WHERE Sex='"+sex+"'"
            cur1.execute(sql)
            while(True):
                i=i+1
                row=cur1.fetchone()
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
                con.commit()
        elif color!=""and height=="":
            sql="SELECT * FROM 제품TB WHERE Sex='"+sex+"' And Color='"+color+"'"
            cur1.execute(sql)
            while(True):
                i=i+1
                row=cur1.fetchone()
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
                con.commit()
        elif color==""and height!="":
            sql="SELECT * FROM 제품TB WHERE Sex='"+sex+"' And Height='"+height+"'"
            cur1.execute(sql)
            while(True):
                i=i+1
                row=cur1.fetchone()
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
                con.commit()
        elif color!=""and height!="":
            sql="SELECT * FROM 제품TB WHERE Sex='"+sex+"' And Height='"+height+"' And Color='"+color+"'"
            cur1.execute(sql)
            while(True):
                i=i+1
                row=cur1.fetchone()
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
                con.commit()
    elif (color!=""):
        if height=="":
            sql="SELECT * FROM 제품TB WHERE Color='"+color+"'"
            cur1.execute(sql)
            while(True):
                i=i+1
                row=cur1.fetchone()
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
                con.commit()
        elif height!="":
            sql="SELECT * FROM 제품TB WHERE Color='"+color+"' And Height='"+height+"'"
            cur1.execute(sql)
            while(True):
                i=i+1
                row=cur1.fetchone()
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
                con.commit()
    elif(height!=""):
        sql="SELECT * FROM 제품TB WHERE Height='"+height+"'"
        cur1.execute(sql)
        while(True):
            i=i+1
            row=cur1.fetchone()
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
            con.commit()
        
            
    con.close()

    
     
     
window4=Tk()
window4.title("A상사 구두제품조회 Page")
window4.geometry("800x600")
window4.resizable(False, False)
    
menubar=Menu(window4)
filemenu=Menu(menubar)
menubar.add_cascade(label="제품등록",command=enrolldef)
menubar.add_cascade(label="제품입고",command=inputdef)
menubar.add_cascade(label="제품출고",command=outdef)
menubar.add_cascade(label="제품조회",command=messageboxdef1)
menubar.add_cascade(label="  종료  ",command=window4.destroy)
window4.config(menu=menubar)
con,cur=None,None
con=sqlite3.connect("A상사DB.db")
cur=con.cursor()
label1=Label(window4, text="제품코드 :")
label1.config(height=3,width=10)
label1.place(x=10,y=10)
Name=StringVar()#콤보박스와 연동할 변수
combo1= ttk.Combobox(window4, width=20, textvariable=Name)#변수와 콤보박스 연동
sql="SELECT Code FROM 제품TB"
cur.execute(sql)
lstCode=['',]
while(True):
    row=cur.fetchone()
    if row==None:
        break;
    lstCode.append(row[0])
    
combo1['values'] = lstCode
con.close()
combo1.place(x=90,y=25)
combo1.current(0)

label2=Label(window4, text="제품명 :")
label2.config(height=3,width=0)
label2.place(x=280,y=10)
#label2_= Label(window2, text="제품명을 출력합니다")
#label2_.config(height=0,width=0)
#label2_.place(x=340,y=29)
Name=StringVar()#콤보박스와 연동할 변수
combo2= ttk.Combobox(window4, width=20, textvariable=Name)#변수와 콤보박스 연동
combo2['values'] = ('','로퍼', '첼시부츠', '메리제인' , '펌프스','플랫슈즈')
combo2.place(x=335,y=25)
combo2.current(0)

label3=Label(window4, text="성  별 :")
label3.config(height=3,width=0)
label3.place(x=530,y=10)
#label3_= Label(window2, text="성별을 출력합니다")
#label3_.config(height=0,width=0)
#label3_.place(x=585,y=28)
Sex=StringVar()
combo3= ttk.Combobox(window4, width=20, textvariable=Sex)#변수와 콤보박스 연동
combo3['values'] = ('','남', '여')
combo3.place(x=590,y=25)
combo3.current(0)
               
label4=Label(window4, text="제품색상 :")
label4.config(height=3,width=0)
label4.place(x=265,y=55)
#label4_= Label(window2, text="색상을 출력합니다")
#label4_.config(height=0,width=0)
#label4_.place(x=340,y=68)
Color=StringVar()
combo4= ttk.Combobox(window4, width=20, textvariable=Color)#변수와 콤보박스 연동
combo4['values'] = ('','Navy', 'Beige' , 'Wine')
combo4.place(x=335,y=70)
combo4.current(0)

label5=Label(window4, text="제품높이 :")
label5.config(height=3,width=7)
label5.place(x=525,y=50)
#label5_= Label(window2, text="높이를 출력합니다")
#label5_.config(height=0,width=0)
#label5_.place(x=585,y=68)
Height=StringVar()
combo5= ttk.Combobox(window4, width=20, textvariable=Height)#변수와 콤보박스 연동
combo5['values'] = ('','0cm', '3cm', '5cm' , '7cm')
combo5.place(x=590,y=70)
combo5.current(0)

btn1=Button(window4,text="조 회",command=searchdata)#입고 또는 출고에 해당하는 제품의 정보
btn1.place(x=650,y=130)
btn1.place(height=40,width=90)


label5=Label(window4, text="======================================================================")
label5.pack(expand=YES,fill=BOTH)
label5.place(x=50,y=170)
treeview=tkinter.ttk.Treeview(window4 , columns=("0","1","2","3","4"))
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
treeview.place(x=30,y=220)
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
    #treeview.tag_bind(i,"<ButtonRelease-1>",callback=infoput)
    #treeview.tag_bind(i,"<Double-Button-2>",callback=inputput)
#treeview.tag_bind("one",sequence="<<TreeviewSelect>>",callback=infoput)
#treeview.bind('<Button>',infoput)
con.close()




def center_window(width=300, height=200):
    # get screen width and height
    screen_width = window4.winfo_screenwidth()
    screen_height = window4.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    window4.geometry('%dx%d+%d+%d' % (width, height, x, y))
    
center_window(800,600)

window4.mainloop()

