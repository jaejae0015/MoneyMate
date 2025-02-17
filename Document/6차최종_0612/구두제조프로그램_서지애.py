#메인프로그램 작성
from tkinter import *

def enroll():
    import 구두제조프로그램_등록프로그램
def inputdef():
    import 구두제조프로그램_입고처리프로그램
def outdef():
    
    import 구두제조프로그램_출고처리프로그램
def checkdef():
    
    import 구두제조프로그램_조회처리프로그램_복사본

def center_window(width=300, height=200):
    # get screen width and height
    screen_width = window0.winfo_screenwidth()
    screen_height = window0.winfo_screenheight()

    # 크기 조절하기
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    window0.geometry('%dx%d+%d+%d' % (width, height, x, y))
    


window0=Tk()
window0.title("A상사 구두제조관리 Program")
window0.geometry("900x600")
window0.resizable(False, False)


#환영문구삽입
LabelFont=('times',20,'bold')
LabelFont2=('times',15,'bold')

widget=Label(window0,text="☆A상사 구두제조관리 Program 방문을 환영합니다☆")
widget.config(fg='black',font=LabelFont)
widget.config(height=3,width=20)
widget.pack(expand=NO,fill=BOTH)
#버튼 등록/입고/출고/조회/종료
btn1=Button(window0,text="제품등록",command=enroll)
btn1.config(font=LabelFont2,fg='#993800')
btn1.place(x=100,y=100)
btn1.place(height=40,width=100)

btn2=Button(window0,text="제품입고",command=inputdef)
btn2.config(font=LabelFont2,fg='#993800')
btn2.place(x=250,y=100)
btn2.place(height=40,width=100)

btn3=Button(window0,text="제품출고",command=outdef)
btn3.config(font=LabelFont2,fg='#993800')
btn3.place(x=400,y=100)
btn3.place(height=40,width=100)

btn4=Button(window0,text="제품조회",command=checkdef)
btn4.config(font=LabelFont2,fg='#993800')
btn4.place(x=550,y=100)
btn4.place(height=40,width=100)

btn5=Button(window0,text="종료",command=window0.destroy)
btn5.config(font=LabelFont2,fg='#993800')
btn5.place(x=700,y=100)
btn5.place(height=40,width=100)

widget2=Label(window0,text="=====================================================================================================")
widget2.config(height=3)
widget2.pack(expand=YES,fill=BOTH)
widget2.place(x=50,y=150)

#회사 문구 / 이미지
img1=PhotoImage(file="신발이미지.png", height=300, width=300)
label1=Label(window0,image=img1)
label1.place(x=510,y=200)

contents="""

저희 A상사 구두는
고객 여러분께 최고의 품질로 제공됩니다.

저희 A상사 구두와 함께,
고객님과
좋은 길을 걸을 수 있다면 좋겠습니다.

늘 열심히 좋은 구두를 만드는 A상사가 되겠습니다.


"""
label2=Label(window0,fg="#FF5E00",font="Times 15 bold italic",justify=LEFT,padx=10, text=contents)
label2.place(x=50,y=200)
center_window(900,600)
window0.mainloop()
