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
    #sql="SELECT * FROM 제품TB"
    con,cur1=None,None
    con=sqlite3.connect("A상사DB.db")
    cur1=con.cursor()
    NAME=label11.get()
    SEX=label22.get()
    COLOR=label33.get()
    HEIGHT=label44.get()
    if label11!="" and label22!="" and label33!="" and label44!="":
            sql="SELECT * FROM 제품TB WHERE Sex='"+SEX+"'AND Color='"+COLOR+"'AND Name='"+NAME+"' AND Height='"+HEIGHT+"' "
            cur1.execute(sql)
            treeview=tkinter.ttk.Treeview(window4, columns=("0","1","2","3","4"))
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
                #treeview.tag_bind(i,"<ButtonRelease-1>",callback=infoput)
                #treeview.tag_bind(i,"<ButtonRelease-1>",callback=insertdata)
                #treeview.tag_bind(i,"<Double-Button-2>",callback=inputput)
            #treeview.tag_bind("one",sequence="<<TreeviewSelect>>",callback=infoput)
            #treeview.bind('<Button>',infoput)
    elif label11!="" and label22!="" and label33!="" and label44=="":
            sql="SELECT * FROM 제품TB WHERE Sex='"+SEX+"'AND Color='"+COLOR+"'AND Name='"+NAME+"' "
            cur1.execute(sql)
            treeview=tkinter.ttk.Treeview(window4, columns=("0","1","2","3","4"))
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
                #treeview.tag_bind(i,"<ButtonRelease-1>",callback=infoput)
                #treeview.tag_bind(i,"<ButtonRelease-1>",callback=insertdata)
                #treeview.tag_bind(i,"<Double-Button-2>",callback=inputput)
            #treeview.tag_bind("one",sequence="<<TreeviewSelect>>",callback=infoput)
            #treeview.bind('<Button>',infoput)
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

con, cur1,cur2,cur3=None,None,None,None #연결자,커서
sql=""
con=sqlite3.connect("A상사DB.db")

cur1=con.cursor()
sql="SELECT * FROM 제품TB"
cur1.execute(sql)


Namedata,Sexdata,Heightdata,Colordata=[],[],[],[]


while(True):
    row=cur1.fetchone()
    if row==None:
        break;
    Namedata.append(row[1])
    Sexdata.append(row[2])
    Colordata.append(row[3])
    Heightdata.append(row[4])

    

FONT=('굴림',15,'bold')
label0=Label(window4, text="[조회 조건]")
label0.config(height=0,width=0 ,font=FONT)
label0.place(x=40,y=10)


label1=Label(window4, text="제품이름 :")
label1.config(height=3,width=10)
label1.place(x=30,y=35)
label11=ttk.Combobox(window4, width=20)
label11['values'] = Namedata
label11.place(x=110,y=52)


label2=Label(window4, text="성별 :")
label2.config(height=3,width=10)
label2.place(x=300,y=35)
label22=ttk.Combobox(window4, width=10)
label22['values'] =('남','여')
label22.place(x=380,y=52)


label3=Label(window4, text="색상 :")
label3.config(height=3,width=10)
label3.place(x=35,y=80)
label33=ttk.Combobox(window4, width=10)
label33['values'] =Colordata
label33.place(x=110,y=100)


label4=Label(window4, text="높이 :")
label4.config(height=3,width=5)
label4.place(x=250,y=80)
label44=ttk.Combobox(window4, width=10)
label44['values'] =Heightdata
label44.place(x=310,y=100)


#label5=Label(window4, text="선택조건 :")
#label5.config(height=3,width=7)
#label5.place(x=440,y=80)
#label5_=ttk.Combobox(window4, width=10)
#label5_['values'] =('입고','출고','입출고')
#label5_.place(x=520,y=100)





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

