import sqlite3
from datetime import datetime
from tkinter import *
from tkinter import ttk # for 콤보박스 사용
from tkinter import messagebox
import tkinter
import tkinter.ttk

con,cur=None,None
con=sqlite3.connect("A상사DB.db")
cur=con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS 출고TB (Code char(5), Date char(20), Quantity int)")

    

def messageboxdef1():
    messagebox.showinfo('알림','현재 페이지입니다.')
def enrolldef():
    window3.destroy()
    import 구두제조프로그램_등록프로그램
def inputdef():
    window3.destroy()
    import 구두제조프로그램_입고처리프로그램

def checkdef():
    window3.destroy()
    import 구두제조프로그램_조회처리프로그램_복사본

#데이터 조회함수
def selectdata():
    LabelFont=('times',13,'bold')
    fontlist=('굴림',10,'normal')
    row=None
    con, cur=None,None#등록TB
    sql=""
    Codedata,Namedata,Sexdata,Colordata,Heightdata,Datedata,Quantitydata=[],[],[],[],[],[],[]
    
    con=sqlite3.connect("A상사DB.db") 
    cur=con.cursor()
    sql="SELECT * FROM 제품TB"
    cur.execute(sql)
    
    Code=label1_.get()
    Quanti=label8_.get()

    if Code=="제품코드":
        
            
        
        lab1=Label(window, text="       제품코드                 제품명            성별   /   제품색상   /  높이             출고일자                  수량")
        lab1.config(font=LabelFont)    
        lab1.place(x=40,y=250)
        lab1.config(height=0,width=0)
        lab2=Label(window, text="----------------------------------------------------------------------------------------------------------------------")
        lab2.config(font=LabelFont)
        lab2.config(height=0,width=0)
        lab2.place(x=40,y=269)
        while(True):
            row=cur.fetchone()
            if row==None:
                break;
            Codedata.append(row[0])
            Namedata.append(row[1])
            Sexdata.append(row[2]) 
            Colordata.append(row[3])
            Heightdata.append(row[4])
            Quantitydata.append(row[5])

        

            
        listdata1=Listbox(window,bg='#D4F4FA',font=fontlist)#코드
        listdata1.place(x=50,y=290)
        listdata1.config(height=20,width=15)
        listdata2=Listbox(window,bg='#D4F4FA',font=fontlist)#제품명
        listdata2.place(x=160,y=290)
        listdata2.config(height=20,width=20)
        listdata3=Listbox(window,bg='#D4F4FA',font=fontlist)#성별
        listdata3.place(x=305,y=290)
        listdata3.config(height=20,width=5)
        listdata4=Listbox(window,bg='#D4F4FA',font=fontlist)#색상
        listdata4.place(x=345,y=290)
        listdata4.config(height=20,width=15)
        listdata5=Listbox(window,bg='#D4F4FA',font=fontlist)#높이
        listdata5.place(x=457,y=290)
        listdata5.config(height=20,width=5)
        listdata6=Listbox(window,bg='#F78181',font=fontlist)#입고일자
        listdata6.place(x=500,y=290)
        listdata6.config(height=20,width=23)
        listdata7=Listbox(window,bg='#D4F4FA',font=fontlist)#수량
        listdata7.place(x=670,y=290)
        listdata7.config(height=20,width=10)
        for item1,item2,item3,item4,item5,item6 in zip(Codedata,Namedata,Sexdata,Colordata,Heightdata,Quantitydata):
            listdata1.insert(END,item1)
            listdata2.insert(END,item2)
            listdata3.insert(END,item3)
            listdata4.insert(END,item4)
            listdata5.insert(END,item5)
            listdata7.insert(END,item6)
    else:
        cur1=con.cursor()
        sql="SELECT * FROM 출고TB WHERE Code='"+Code+"'"
        cur1.execute(sql)
        
        lab1=Label(window, text="       제품코드                 제품명            성별   /   제품색상   /  높이             입고일자                  수량")
        lab1.config(font=LabelFont)    
        lab1.place(x=40,y=250)
        lab1.config(height=0,width=0)
        lab2=Label(window, text="----------------------------------------------------------------------------------------------------------------------")
        lab2.config(font=LabelFont)
        lab2.config(height=0,width=0)
        lab2.place(x=40,y=269)
        while(True):
            row=cur1.fetchone()
            if row==None:
                break;
            Codedata.append(row[0])
            Datedata.append(row[1])
            Quantitydata.append(row[2])
        #while(True):
         #   row=cur1.fetchone()
          #  if row==None:
           #     break;
            #Datedata.append(row[0])
       

            
        listdata1=Listbox(window,bg='#D4F4FA',font=fontlist)#코드
        listdata1.place(x=50,y=290)
        listdata1.config(height=20,width=15)
        listdata2=Listbox(window,bg='#F78181',font=fontlist)#제품명
        listdata2.place(x=160,y=290)
        listdata2.config(height=20,width=20)

        listdata3=Listbox(window,bg='#F78181',font=fontlist)#성별
        listdata3.place(x=305,y=290)
        listdata3.config(height=20,width=5)
        listdata4=Listbox(window,bg='#F78181',font=fontlist)#색상
        listdata4.place(x=345,y=290)
        listdata4.config(height=20,width=15)
        listdata5=Listbox(window,bg='#F78181',font=fontlist)#높이
        listdata5.place(x=457,y=290)
        listdata5.config(height=20,width=5)
        listdata6=Listbox(window,bg='#D4F4FA',font=fontlist)#입고일자
        listdata6.place(x=500,y=290)
        listdata6.config(height=20,width=23)
        listdata7=Listbox(window,bg='#D4F4FA',font=fontlist)#수량
        listdata7.place(x=670,y=290)
        listdata7.config(height=20,width=10)
        for item1,item7,item6 in zip(Codedata,Quantitydata,Datedata):
            listdata1.insert(END,item1)
            listdata7.insert(END,item7)
            listdata6.insert(END,item6)
    
   
    con.close()

#제품정보확인함수
def checkdata():
    CodeCode,NameName,SexSex,ColorColor,HeightHeight,QuantityQuantity=[],[],[],[],[],[]
    Code=label1_.get()
    row=None
    con, cur,cur1,cur2=None,None,None,None
    sql=""
    con=sqlite3.connect("A상사DB.db")
    cur1=con.cursor()
    sql="SELECT * FROM 제품TB WHERE Code='"+Code+"'"
    cur1.execute(sql)

    while(True):
                row=cur1.fetchone()
                if row==None:
                    break;
                CodeCode.append(row[0])
                NameName.append(row[1])
                SexSex.append(row[2])
                ColorColor.append(row[3])
                HeightHeight.append(row[4])
                QuantityQuantity.append(row[5])

    Co=CodeCode[0]
    Na=NameName[0]
    Se=SexSex[0]
    Col=ColorColor[0]
    He=HeightHeight[0]
    Q=QuantityQuantity[0]
            
    label2_= Label(window, text=Na)
    label2_.config(height=0,width=0)
    label2_.place(x=340,y=29)
    label3_= Label(window, text=Se)
    label3_.config(height=0,width=0)
    label3_.place(x=585,y=28)
    label4_= Label(window, text=Col)
    label4_.config(height=0,width=0)
    label4_.place(x=340,y=68)
    label5_= Label(window, text=He)
    label5_.config(height=0,width=0)
    label5_.place(x=585,y=68)
    label7_= Label(window, text=Q)
    label7_.config(height=0,width=2)
    label7_.place(x=620,y=140)       
                
    con.commit()
    con.close()


#출고 정보 저장 함수
def insertdata():
    con, cur=None,None #연결자,커서
    #Code,Date.Quantity="","",""#전역변수
    Quantitydata,Outputdata=[],[]
    sql=""
    con=sqlite3.connect("A상사DB.db")
    cur=con.cursor()
    sql="SELECT Code, Quantity FROM 제품TB"
    cur.execute(sql)
    global Code
    Code=str(infoput(Code))
    print(Code)
    Quantity=label8_.get()
    print(Quantity)
    Date=label6_.get()
    sql="SELECT Quantity,Output FROM 제품TB WHERE Code='"+Code+"'"
    cur.execute(sql)
    
    while(True):
        row=cur.fetchone()
        if row==None:
            break;
        Quantitydata.append(row[0])
        Outputdata.append(row[1])
    try:
        sql="INSERT INTO 출고TB VALUES('"+Code+"','"+Date+"',"+Quantity+")"
        cur.execute(sql)
                
    except:
        messagebox.showerror('오류','제품 등록 실패')
        
                
    else:
        Quantity=int(Quantity)
        su=Quantitydata[0]
        out=Outputdata[0]
        su=int(su)
        out=int(out)
        Quan=su-Quantity
        Quan=int(Quan)
        outp=out+Quantity
        outp=int(outp)

        if (Quan<0):
            messagebox.showerror('오류','제품 기준 수량 미달입니다')
            sql="DELETE FROM 출고TB WHERE Quantity="+str(Quan)+""
            cur.execute(sql)      
        else:  
            sql="UPDATE 제품TB SET Quantity="+str(Quan)+", Output="+str(outp)+"  WHERE Code='"+Code+"'"
            cur.execute(sql)
            messagebox.showinfo('성공','제품 출고 처리 성공.')
            treeview=tkinter.ttk.Treeview(window3, columns=("0","1","2","3","4","5"))
            treeview.pack()

            treeview.column("#0", width=70,anchor=CENTER)
            treeview.heading("#0", text="제품코드")
            treeview.column("#1", width=100,anchor=CENTER)
            treeview.heading("#1", text="제품명")
            treeview.column("#2", width=50,anchor=CENTER)
            treeview.heading("#2", text="성별")
            treeview.column("#3", width=100,anchor=CENTER)
            treeview.heading("#3", text="제품색상")
            treeview.column("#4", width=80,anchor=CENTER)
            treeview.heading("#4", text="제품높이")
            treeview.column("#5", width=70,anchor=CENTER)
            treeview.heading("#5", text="제품재고")
            treeview.column("#6",width=70,anchor=CENTER)
            treeview.heading("#6",text="출고누적")
            treeview.place(x=30,y=240)
            treeview.place(height=340)
            Tlist=[]
            i=0
            #treeview.bind("<ButtonRelease-1>",infoput)

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
                Output=row[7]
                
                Tlist=[(Name,Sex,Color,Height,Quantity,Output)]
                treeview.insert("",'end',text=Code, values=Tlist[0],tags=i)
                treeview.tag_bind(i,"<ButtonRelease-1>",callback=infoput)
                #treeview.tag_bind(i,"<ButtonRelease-1>",callback=insertdata)
                #treeview.tag_bind(i,"<Double-Button-2>",callback=inputput)
            #treeview.tag_bind("one",sequence="<<TreeviewSelect>>",callback=infoput)
            #treeview.bind('<Button>',infoput)
                
            Code=str(infoput(Code))    
            tree=tkinter.ttk.Treeview(window3, columns=("0","1"))
            tree.pack()

            tree.column("#0", width=100,anchor=CENTER)
            tree.heading("#0", text="제품코드")
            tree.column("#1", width=170,anchor=CENTER)
            tree.heading("#1", text="출고날짜")
            tree.column("#2", width=100,anchor=CENTER)
            tree.heading("#2", text="출고량")
            tree.place(x=600,y=240)
            tree.place(height=340)
            Tlist1=[]
            i=0
            #treeview.bind("<ButtonRelease-1>",infoput)

            cur1=None
            cur1=con.cursor()
            print(Code)
            sql1="SELECT * FROM 출고TB WHERE Code='"+Code+"'"
            cur1.execute(sql1)

            while(True):
                i=i+1
                row=cur1.fetchone()
                if row==None:
                    break;
                Code=row[0]
                Date=row[1]
                Quantity=row[2]
                
                Tlist1=[(Date,Quantity)]
                tree.insert("",'end',text=Code, values=Tlist1[0],tags=i)
                tree.tag_bind(i,"<ButtonRelease-1>",callback=infoput)
                #treeview.tag_bind(i,"<Double-Button-2>",callback=inputput)
            #treeview.tag_bind("one",sequence="<<TreeviewSelect>>",callback=infoput)
            #treeview.bind('<Button>',infoput)
    

 
    con.commit()
    con.close()
#데이터 삭제함수-리스트에 코드를 담고, 돌린다음에 그거랑 일치하면 삭제함.    
def deletedata():
    
    con,cur,cur1,cur2=None,None,None,None
    Code="" 
    sql=""
    Quantitydata=[]
    con=sqlite3.connect("A상사DB.db")
    cur=con.cursor()
    cur1=con.cursor()
    cur2=con.cursor()
    

    Code=label1_.get()
    Quantity=label8_.get()


    sql="SELECT Quantity FROM 제품TB WHERE Code='"+Code+"'"
    cur2.execute(sql)
    
    while(True):
        row=cur2.fetchone()
        if row==None:
            break;
        Quantitydata.append(row[0])

    sql="SELECT Quantity FROM 출고TB WHERE Code='"+Code+"'"
    cur.execute(sql)
    while(True):
        row=cur.fetchone()
        if row==None:
            break;
        Quantitydata.append(row[0])
    

    if Quantity=="":
        try:
            sql="DELETE FROM 출고TB WHERE Code='"+Code+"'"
            cur.execute(sql)
        except:
            messagebox.showerror('오류','해당 제품 출고 정보 전체 삭제 실패.')
        else:
            su=0
            
            for i in Quantitydata:
                i=int(i)
                su=int(su)
                su+=i
                

            
            sql="UPDATE 제품TB SET Quantity="+str(su)+" WHERE Code='"+Code+"'"
            cur1.execute(sql)
            messagebox.showinfo('성공','해당 제품 출고 정보 전체 삭제 성공.')
    else:
        try:
            sql="DELETE FROM 출고TB WHERE Code='"+Code+"' and Quantity="+Quantity+""
            cur.execute(sql)
        except:
            messagebox.showerror('오류','해당 제품 출고 정보 삭제 실패.')
        else:
            Quantity=int(Quantity)
            su=Quantitydata[0]
            su=int(su)
            Quan=su+Quantity
            Quan=int(Quan)
            sql="UPDATE 제품TB SET Quantity="+str(Quan)+"  WHERE Code='"+Code+"'"
            cur1.execute(sql)
            messagebox.showinfo('성공','해당 제품 출고 정보 삭제 성공.')
    
            
    con.commit()#반드시 있어야함
    con.close()

def infoput(Code):
    
        curitem=treeview.focus()
        it=treeview.item(curitem)
           
        Code=it['text']
        VA=it['values']
           
        edt1=Entry(window3)
        edt1.config(width=15)
        edt1.insert(0,Code)
        edt1.place(x=125,y=25)

        #edt2=Entry(window2)
        #edt2.insert(0,VA.pop(0))
        #edt2.place(x=340,y=29)


        #edt3=Entry(window2)
        #edt3.config(width=10)
        #edt3.insert(0,VA.pop(0))
        #edt3.place(x=125,y=65)

        #edt4=Entry(window2)
        #edt4.insert(0,VA.pop(0))
        #edt4.place(x=350,y=65)

        #edt5=Entry(window2)
        #edt5.insert(0,VA.pop(0))
        #edt5.config(width=10)
        #edt5.place(x=620,y=65)
        #label1_=Label(window2,text=Code)
        #label1_.place(x=110,y=28)
        #label1_.config(height=0,width=0)

        label2_= Label(window3, text=VA.pop(0))
        label2_.config(height=0,width=0)
        label2_.place(x=340,y=28)
        label3_= Label(window3, text=VA.pop(0))
        label3_.config(height=0,width=0)
        label3_.place(x=585,y=28)
        label4_= Label(window3, text=VA.pop(0))
        label4_.config(height=0,width=0)
        label4_.place(x=340,y=68)
        label5_= Label(window3, text=VA.pop(0))
        label5_.config(height=0,width=0)
        label5_.place(x=585,y=68)
        label7_= Label(window3, text=VA.pop(0))
        label7_.config(height=0,width=5)
        label7_.place(x=120,y=150)
        #label8=Label(window2, text="입고수량 :")
        #label8.config(height=0,width=0)
        #label8.place(x=250,y=150)
        #label8_= Entry(window2)
        #label8_.place(x=320,y=150)
        
        
        return Code

window3=Tk()
window3.title("A상사 구두제품출고 Page")
window3.geometry("800x600")
window3.resizable(False, False)
    
menubar=Menu(window3)
filemenu=Menu(menubar)
menubar.add_cascade(label="제품등록",command=enrolldef)
menubar.add_cascade(label="제품입고",command=inputdef)
menubar.add_cascade(label="제품출고",command=messageboxdef1)
menubar.add_cascade(label="제품조회",command=checkdef)
menubar.add_cascade(label="  종료  ",command=window3.destroy)
window3.config(menu=menubar)

con, cur=None,None #연결자,커서
sql=""
con=sqlite3.connect("A상사DB.db")
cur=con.cursor()
sql="SELECT Code FROM 제품TB"
cur.execute(sql)
Codedata=[]
Codedata.append("제품코드")


#con=sqlite3.connect("c:\A상사\등록DB")
#cur=con.cursor()
#cur.execute("CREATE TABLE 출고TB (Code char(5) , Date char(20), Quantity int)")    



    
while(True):
    row=cur.fetchone()
    if row==None:
        break;
    Codedata.append(row[0])
    
date=datetime.today().strftime("%Y-%m-%d ")
    

label1=Label(window3, text="제품코드 :")
label1.config(height=3,width=10)
label1.place(x=30,y=10)
#label1_=Entry(window)
#label1_.place(x=120,y=25)
#label1_=ttk.Combobox(window3, width=15)#콤보박스와 연동할 변수
#label1_['values'] = Codedata
#label1_.place(x=110,y=28)
#label1_.current(0)
edt1=Entry(window3)
edt1.config(width=15)
edt1.place(x=125,y=25)

label2=Label(window3, text="제품명 :")
label2.config(height=3,width=0)
label2.place(x=280,y=10)
#label2_= Entry(window)
#label2_.place(x=340,y=28)

label3=Label(window3, text="성  별 :")
label3.config(height=3,width=0)
label3.place(x=530,y=10)
#label3_= Entry(window)
#label3_.place(x=585,y=28)
               
label4=Label(window3, text="제품색상 :")
label4.config(height=3,width=0)
label4.place(x=265,y=50)
#label4_= Entry(window)
#label4_.place(x=340,y=68)

label5=Label(window3, text="제품높이 :")
label5.config(height=3,width=7)
label5.place(x=520,y=50)
#label5_= Entry(window)
#label5_.place(x=585,y=68)

label6=Label(window3, text="출고일자 :")
label6.config(height=3,width=7)
label6.place(x=45,y=90)
#label6_= Entry(window)
#label6_.place(x=125,y=115)
label6_=Entry(window3)
#label6_.config(height=0,width=0)
label6_.place(x=120,y=110)
label6_.insert(0,date)


label8=Label(window3, text="출고수량 :")
label8.config(height=0,width=0)
label8.place(x=250,y=150)
label8_= Entry(window3)
label8_.place(x=320,y=150)

label7=Label(window3, text="현재수량 :")
label7.config(height=0,width=0)
label7.place(x=40,y=150)
#label7_= Entry(window)
#label7_.place(x=600,y=140)

btn1=Button(window3,text="등 록",command=insertdata)
btn1.place(x=520,y=140)
btn1.place(height=40,width=80)

#btn2=Button(window3,text="삭 제",command=deletedata)
#btn2.place(x=600,y=140)
#btn2.place(height=40,width=80)

#btn4=Button(window,text="제품 LIST 확인", command=selectdata)
#btn4.place(x=640,y=180)
#btn4.place(height=40,width=120)

#btn5=Button(window,text="제품정보확인",command=checkdata)
#btn5.place(x=108,y=60)
#btn5.place(height=40,width=145)

treeview=tkinter.ttk.Treeview(window3, columns=("0","1","2","3","4","5"))
treeview.pack()

treeview.column("#0", width=70,anchor=CENTER)
treeview.heading("#0", text="제품코드")
treeview.column("#1", width=100,anchor=CENTER)
treeview.heading("#1", text="제품명")
treeview.column("#2", width=50,anchor=CENTER)
treeview.heading("#2", text="성별")
treeview.column("#3", width=100,anchor=CENTER)
treeview.heading("#3", text="제품색상")
treeview.column("#4", width=80,anchor=CENTER)
treeview.heading("#4", text="제품높이")
treeview.column("#5", width=70,anchor=CENTER)
treeview.heading("#5", text="제품재고")
treeview.column("#6",width=70,anchor=CENTER)
treeview.heading("#6",text="출고누적")
treeview.place(x=30,y=240)
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
    Output=row[7]
    
    Tlist=[(Name,Sex,Color,Height,Quantity,Output)]
    treeview.insert("",'end',text=Code, values=Tlist[0],tags=i)
    treeview.tag_bind(i,"<ButtonRelease-1>",callback=infoput)
    #treeview.tag_bind(i,"<ButtonRelease-1>",callback=insertdata)
    #treeview.tag_bind(i,"<Double-Button-2>",callback=inputput)
#treeview.tag_bind("one",sequence="<<TreeviewSelect>>",callback=infoput)
#treeview.bind('<Button>',infoput)
con.close()


tree=tkinter.ttk.Treeview(window3, columns=("0","1"))
tree.pack()

tree.column("#0", width=100,anchor=CENTER)
tree.heading("#0", text="제품코드")
tree.column("#1", width=170,anchor=CENTER)
tree.heading("#1", text="출고날짜")
tree.column("#2", width=100,anchor=CENTER)
tree.heading("#2", text="출고량")
tree.place(x=600,y=240)
tree.place(height=340)
Tlis1t=[]
i=0
#treeview.bind("<ButtonRelease-1>",infoput)

con,cur1=None,None
con=sqlite3.connect("A상사DB.db") 
cur1=con.cursor()

sql="SELECT * FROM 출고TB"
cur1.execute(sql)

while(True):
    i=i+1
    row=cur1.fetchone()
    if row==None:
        break;
    Code=row[0]
    Date=row[1]
    Quantity=row[2]
    
    Tlist1=[(Date,Quantity)]
    tree.insert("",'end',text=Code, values=Tlist1[0],tags=i)
    tree.tag_bind(i,"<ButtonRelease-1>",callback=infoput)
    #treeview.tag_bind(i,"<Double-Button-2>",callback=inputput)
#treeview.tag_bind("one",sequence="<<TreeviewSelect>>",callback=infoput)
#treeview.bind('<Button>',infoput)
con.close()



label5=Label(window3, text="=========================================================================================")
label5.pack(expand=YES,fill=BOTH)
label5.place(x=50,y=200)

def center_window(width=300, height=200):
    # get screen width and height
    screen_width = window3.winfo_screenwidth()
    screen_height = window3.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    window3.geometry('%dx%d+%d+%d' % (width, height, x, y))
    
center_window(1000,600)

window3.mainloop()
