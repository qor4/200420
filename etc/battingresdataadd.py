from tkinter import *
from tkinter import messagebox
import sqlite3
import turtle
import random

window = Tk()

window.title("아마추어를 위한 타구 분석 프로그램")
window.geometry("1040x500")
window.resizable(False, False)

mainMenu = Menu(window)
window.config(menu = mainMenu)

#야구장 이미지 사진
photo = PhotoImage(file = "야구장사진.gif")
label_image = Label(window, image = photo)

#변수설정
pitcherName =None
pitcherType =None
pitchType =None
batterName =None
xPoint =None
yPoint =None
pitcherTypetext=None
pitchTypetext=None
battingRes = None
battingRestext = None

base1=0
base2=0
base3=0
base4=0
OPS=0
OBP=0
BABIP=0
SLG=0
batAVG=0
fb=0
ball4=0
hitting=0
hitsum=0
hbp=0
sto=0
gb=0

#분석 화면 사용 변수 선언
con, cur = None, None
row = None
mainpointX = 279 #분포도에서 기준이 되는 시작 좌표의 값
mainpointY = 445 #y값

#데이터베이스 설정

#캔버스 설정
canvas = Canvas(window, bd=2, width=550, height=400)
canvas.create_image(280, 250, image = photo)

canvas.pack(fill="both", side=LEFT)


#그림 클릭
def clickLeft(event) :
    print(event.x, event.y)
    canvas.create_oval(event.x - 3, event.y - 3, event.x + 3, event.y + 3, fill="red")
    global xPoint
    xPoint=event.x
    global yPoint
    yPoint=event.y

#버튼 클릭
def clickbutton4(): #투수 이름
    global pitcherName
    pitcherName=entry1.get()
    print(entry1.get())

def clickbutton5(): #좌투
    global pitcherType
    pitcherType=1
    global pitcherTypetext
    pitcherTypetext="좌투"
    print(pitcherType)
    print(pitcherTypetext)


def clickbutton6(): #우투
    global pitcherType
    pitcherType = 2
    global pitcherTypetext
    pitcherTypetext="우투"
    print(pitcherType)
    print(pitcherTypetext)


def clickbutton7(): #직구
    global pitchType
    pitchType=1
    global pitchTypetext
    pitchTypetext="직구"
    print(pitchType)
    print(pitchTypetext)

def clickbutton8(): #슬라이더
    global pitchType
    pitchType=2
    global pitchTypetext
    pitchTypetext="슬라이더"
    print(pitchType)
    print(pitchTypetext)

def clickbutton9(): #타자 이름
    global batterName
    batterName=entry2.get()
    print(entry2.get())

def clickbutton10(): #1루타
    global battingRes
    battingRes = 1
    global battingRestext
    battingRestext = "1루타"
    print(battingRes)
    print(battingRestext)

def clickbutton11(): #2루타
    global battingRes
    battingRes = 2
    global battingRestext
    battingRestext = "2루타"
    print(battingRes)
    print(battingRestext)

def clickbutton12(): #3루타
    global battingRes
    battingRes = 3
    global battingRestext
    battingRestext = "3루타"
    print(battingRes)
    print(battingRestext)

def clickbutton13(): #홈런
    global battingRes
    battingRes = 4
    global battingRestext
    battingRestext = "홈런"
    print(battingRes)
    print(battingRestext)

def clickbutton14(): #볼넷
    global battingRes
    battingRes = 5
    global battingRestext
    battingRestext = "볼넷"
    print(battingRes)
    print(battingRestext)

def clickbutton15(): #사구
    global battingRes
    battingRes = 6
    global battingRestext
    battingRestext = "사구"
    print(battingRes)
    print(battingRestext)

def clickbutton16(): #뜬공
    global battingRes
    battingRes = 7
    global battingRestext
    battingRestext = "뜬공"
    print(battingRes)
    print(battingRestext)

def clickbutton17(): #희생플라이
    global battingRes
    battingRes = 8
    global battingRestext
    battingRestext = "희생플라이"
    print(battingRes)
    print(battingRestext)

def clickbutton18(): #삼진
    global battingRes
    battingRes = 9
    global battingRestext
    battingRestext = "삼진"
    print(battingRes)
    print(battingRestext)
def clickbutton19(): #희생번트
    global battingRes
    battingRes = 10
    global battingRestext
    battingRestext = "희생번트"
    print(battingRes)
    print(battingRestext)
def clickbutton20(): #땅볼
    global battingRes
    battingRes = 11
    global battingRestext
    battingRestext = "땅볼"
    print(battingRes)
    print(battingRestext)


##데이터 select(고정값: 타자 이름/ 변수: 투수포지션/구종/투수이름)

##select함수
def selectData(sql):
    XPOINT, YPOINT = [], []
    con = sqlite3.connect("C:/Users/한서영/PycharmProjects/untitled4/userData")
    cur = con.cursor()
    cur.execute("SELECT * FROM userData")
    while (True):
        row = cur.fetchone()
        if row == None:
            break
        XPOINT.append(row[0])
        YPOINT.append(row[1])

    print_batterLine(XPOINT, YPOINT)
    con.close()

##좌투sql
def analyse_Leftpitcher():
    sql = ""
    sql = "SELECT xPoint, yPoint FROM userData WHERE batterName='" + batterName + "' AND pitcherType=1"
    selectData(sql)

##우투sql
def analyse_Rightpitcher():
    sql = ""
    sql = "SELECT xPoint, yPoint FROM userData WHERE batterName='" + batterName + "' AND pitcherType=2"
    selectData(sql)

##직구sql
def analyse_Fastball():
    sql = ""
    sql = "SELECT xPoint, yPoint FROM userData WHERE batterName='" + batterName + "' AND pitchType=1"
    selectData(sql)

##슬라이더(변화구)sql
def analyse_Slider():
    sql = ""
    sql = "SELECT xPoint, yPoint FROM userData WHERE batterName='" + batterName + "' AND pitchType=2"
    selectData(sql)

##투수이름sql
def analyse_pitcher():
    sql = ""
    sql = "SELECT xPoint, yPoint FROM userData WHERE batterName='" + batterName + "' AND pitcherName='" + pitcherName +"'"
    selectData(sql)

##수비 추천
def recoDefence():
    sql = ""
    sql = "SELECT xPoint, yPoint, pitcherType, pitchType FROM userData WHERE batterName='" + batterName + "' AND pitcherName='" + pitcherName + "'"

    XPOINT, YPOINT, manType, ballType = [], [], [], []
    con = sqlite3.connect(r"C:\Users\Owner\Desktop\program\sqlite\userData")
    cur = con.cursor()
    cur.execute(sql)
    count = 0
    while (True):
        row = cur.fetchone()
        if row == None:
            break;
        XPOINT.append(row[0])
        YPOINT.append(row[1])
        manType.append(row[2])
        ballType.append(row[3])
        count = count + 1


    Xpoint1, Xpoint2, Xpoint3, Xpoint4, Ypoint1, Ypoint2, Ypoint3, Ypoint4 = [], [], [], [], [], [], [], []
    array1, array2, array3, array4 = 0, 0, 0, 0

    for i in XPOINT:
        if(XPOINT[i]<215 and YPOINT[i]<200):
            Xpoint1[array1] = XPOINT[i]
            Ypoint1[array1] = YPOINT[i]
            array1 = array1 + 1
        elif (XPOINT[i] < 345 and YPOINT[i] < 200):
            Xpoint2[array2] = XPOINT[i]
            Ypoint2[array2] = YPOINT[i]
            array2 = array2 + 1

        elif (XPOINT[i] < 555 and YPOINT[i] < 200):
            Xpoint3[array3] = XPOINT[i]
            Ypoint3[array3] = YPOINT[i]
            array3 = array3 + 1

        elif (XPOINT[i] < 280 and YPOINT[i] < 340):
            Xpoint4[array4] = XPOINT[i]
            Ypoint4[array4] = YPOINT[i]
            array4 = array4 + 1


    xaver1 = averXpoint(Xpoint1)
    yaver1 = averYpoint(Ypoint1)
    xaver2 = averXpoint(Xpoint2)
    yaver2 = averYpoint(Ypoint2)
    xaver3 = averXpoint(Xpoint3)
    yaver3 = averYpoint(Ypoint3)
    xaver4 = averXpoint(Xpoint4)
    yaver4 = averYpoint(Ypoint4)
    print_recoDefence(xaver1, yaver1)
    print_recoDefence(xaver2, yaver2)
    print_recoDefence(xaver3, yaver3)
    print_recoDefence(xaver4, yaver4)

    manaver = avermanType(manType)
    ballaver = averballType(ballType)


def print_recoDefence(Xpoint, Ypoint):
    x1, y1 = (Xpoint - 3), (Ypoint - 3)
    x2, y2 = (Xpoint + 3), (Ypoint + 3)

    canvas.create_rectangle(x1, y1, x2, y2, width=2, fill="blue")



##x좌표 평균값
def averXpoint(XPOINT):
    Xsum = 0
    Xaver = 0
    for x in range(0, len(XPOINT)):
        Xsum += XPOINT[x]
    Xaver = Xsum/len(XPOINT)
    return Xaver

##y좌표 평균값
def averYpoint(YPOINT):
    Ysum = 0
    Yaver = 0
    for y in range(0, len(YPOINT)):
        Ysum += YPOINT[y]
    Yaver = Ysum/len(YPOINT)
    return Yaver

##투수정보 확률
def avermanType(manType):
    leftType = manType.count(1)/len(manType)
    rightType = manType.count(2)/ len(manType)

    if leftType > rightType:
        return leftType
    else:
        return rightType

##구종 확률
def averballType(ballType):
    fastball = ballType.count(1)/len(ballType)
    slider = ballType.count(2)/len(ballType)

    if fastball > slider:
        return fastball
    else:
        return slider


def resetVari():
    global pitcherName
    global pitcherType
    global pitchType
    global batterName
    global xPoint
    global yPoint
    global pitcherTypetext
    global pitchTypetext
    global battingRes
    global battingRestext

    pitcherName = None
    pitcherType = None
    pitchType = None
    batterName = None
    xPoint = None
    yPoint = None
    pitcherTypetext = None
    pitchTypetext = None
    battingRes = None
    battingRestext = None

#맨 위 입력 버튼으로 데이터베이스에 데이터 저장


def input_messageask():
    global pitcherName
    global pitcherType
    global pitchType
    global batterName
    global xPoint
    global yPoint
    global pitcherTypetext
    global pitchTypetext

    ans=messagebox.askquestion("확인", "투수 이름 : " + pitcherName  + "\n투수 정보 : " + pitcherTypetext + "\n구종 : " + pitchTypetext + "\n타자 이름 : " + batterName + "\n타격 결과 : " + battingRestext + "\n이 맞습니까?")
    if ans == "yes":
        canvas.delete("all")
        canvas.create_image(280, 200, image=photo)
        print("확인") #단계별로 코드 실행되는지 확인하기 위해서 추가한 코드
        SaveLine()
        print("저장됨") #단계별로 코드 실행되는지 확인하기 위해서 추가한 코드
        PrintData() #데이터가 제대로 저장됐는지 확인하기 위해서 추가한 함수
        print("출력") #단계별로 코드 실행되는지 확인하기 위해서 추가한 코드

        resetVari()



def analyse_messageask():

    if pitcherType == 1:
        ans = messagebox.askquestion("확인", "투수 정보 : 좌투" + "\n타자 이름 : " + batterName + "\n이 맞습니까?")
        if ans == "yes":
            analyse_Leftpitcher()
            resetVari()

    elif pitcherType == 2:
        ans = messagebox.askquestion("확인", "투수 정보 : 우투" + "\n타자 이름 : " + batterName + "\n이 맞습니까?")
        if ans == "yes":
            analyse_Rightpitcher()
            resetVari()

    elif pitchType == 1:
        ans = messagebox.askquestion("확인", "구종 : 직구" + "\n타자 이름 : " + batterName + "\n이 맞습니까?")
        if ans == "yes":
            analyse_Fastball()
            resetVari()

    elif pitchType == 2:
        ans = messagebox.askquestion("확인", "구종 : 슬라이더" + "\n타자 이름 : " + batterName + "\n이 맞습니까?")
        if ans == "yes":
            analyse_Slider()
            resetVari()

    elif pitcherName != None:
        ans = messagebox.askquestion("확인", "투수 이름 : " + pitcherName + "\n타자 이름 : " + batterName + "\n이 맞습니까?")
        if ans == "yes":
            analyse_pitcher()
            resetVari()


def recommend_messageask():
    ans = messagebox.askquestion("확인", "투수 이름 : " + pitcherName + "\n타자 이름 : " + batterName + "\n이 맞습니까?")
    if ans == "yes":
        recoDefence()

#분포도 출력
def print_batterLine(xPoint, yPoint):
    r, g, b = getRGB()
    turtle.pencolor((r, g, b))

    t = turtle.Turtle()
    tur.shape("circle")
    t.shapesize(0.5, 0.5)

    t.up()
    t.goto(mainpointX, mainpointY)
    t.down()
    t.goto(xPoint, yPoint)
    t.done()

#분포도 색갈 랜덤 지정
def getRGB() :
    r, g, b = 0,0,0
    r = random.random()
    g = random.random()
    b = random.random()
    return(r, g, b)

#메뉴 설정
fileMenu=Menu(mainMenu)
helpMenu=Menu(mainMenu)

mainMenu.add_cascade(label="파일", menu=fileMenu)
fileMenu.add_command(label="입력")
fileMenu.add_separator() #메뉴 구분선
fileMenu.add_command(label="분석")

mainMenu.add_cascade(label="Help", menu=helpMenu)
helpMenu.add_command(label="도움말")




#입력 정보
button1=Button(window, text="입력", relief="groove", bg="skyblue", command=input_messageask)
button1.place(x=570, y=20)
button2=Button(window, text="분석", relief="groove", bg="red", command=analyse_messageask)
button2.place(x=610, y=20)
button3=Button(window, text="수비 추천", relief="groove", bg="gray", command =recommend_messageask)
button3.place(x=650, y=20)

label1=Label(window, text="  투수 이름  ", relief="groove")
label1.place(x=570, y=80)
entry1=Entry(window, width=16) #투수정보
entry1.place(x=570, y=103)
button4=Button(window, text="입력", relief="groove", bg="gray", command=clickbutton4)
button4.place(x=690, y=100)

label2=Label(window, text=" 투수 정보 선택 ", relief="groove")
label2.place(x=570, y=150)
button5=Button(window, text="   좌투   ", relief="groove", bg="gray", command=clickbutton5)
button5.place(x=570, y=175)
button6=Button(window, text="   우투   ", relief="groove", bg="gray", command=clickbutton6)
button6.place(x=640, y=175)


label3=Label(window, text="  구종 선택  ", relief="groove")
label3.place(x=570, y=230)
button7=Button(window, text="   직구   ", relief="groove", bg="gray", command=clickbutton7)
button7.place(x=570, y=255)
button8=Button(window, text="슬라이더", relief="groove", bg="gray", command=clickbutton8)
button8.place(x=640, y=255)


label4=Label(window, text="  타자 이름  ", relief="groove")
label4.place(x=570, y=310)
entry2=Entry(window, width=16) #타자정보
entry2.place(x=570, y=333)
button9=Button(window, text="입력", relief="groove", bg="gray", command=clickbutton9)
button9.place(x=690, y=330)

label5=Label(window, text=" 타격 결과 ", relief="groove")
label5.place(x=800, y=20)
button10=Button(window, text="    1루타    ", relief="groove", bg="gray", command=clickbutton10)
button10.place(x=800, y=45)
button11=Button(window, text="    2루타    ", relief="groove", bg="gray", command=clickbutton11)
button11.place(x=890, y=45)
button12=Button(window, text="    3루타    ", relief="groove", bg="gray", command=clickbutton12)
button12.place(x=800, y=80)
button13=Button(window, text="     홈런     ", relief="groove", bg="gray", command=clickbutton13)
button13.place(x=890, y=80)
button14=Button(window, text="     볼넷     ", relief="groove", bg="gray", command=clickbutton14)
button14.place(x=800, y=115)
button15=Button(window, text="     사구     ", relief="groove", bg="gray", command=clickbutton15)
button15.place(x=890, y=115)
button16=Button(window, text="     뜬공     ", relief="groove", bg="gray", command=clickbutton16)
button16.place(x=800, y=150)
button17=Button(window, text=" 희생플라이", relief="groove", bg="gray", command=clickbutton17)
button17.place(x=890, y=150)
button18=Button(window, text="     삼진     ", relief="groove", bg="gray", command=clickbutton18)
button18.place(x=800, y=185)
button18=Button(window, text="  희생번트  ", relief="groove", bg="gray", command=clickbutton19)
button18.place(x=890, y=185)
button18=Button(window, text="     땅볼     ", relief="groove", bg="gray", command=clickbutton19)
button18.place(x=800, y=220)



label6=Label(window, text="타율:"+str(batAVG))
label6.place(x=800, y=265)
label7=Label(window, text="장타율:"+str(SLG))
label7.place(x=800, y=295)
label8=Label(window, text="OPS:"+str(OPS))
label8.place(x=800, y=325)
label9=Label(window, text="BABIP:"+str(BABIP))
label9.place(x=800, y=355)
label10=Label(window, text="출루율:"+str(OBP))
label10.place(x=800, y=385)

#db 불러와서 맵핑
def Dataa():
    con = sqlite3.connect("C:/Users/한서영/PycharmProjects/untitled4/userData")
    cur = con.cursor()
    cur.execute("SELECT * FROM userData")


def bares1():
    sql=""
    sql="SELECT count(IF(battingRes=1 AND batterName='"+batterName+"')) FROM userData"
    cur.execute(sql)
    base1=cursor.fetchone()
def bares2():
    sql=""
    sql="SELECT count(IF(battingRes=2 AND batterName='"+batterName+"')) FROM userData"
    cur.execute(sql)
    base2=cursor.fetchone()
def bares3():
    sql=""
    sql="SELECT count(IF(battingRes=3 AND batterName='"+batterName+"')) FROM userData"
    cur.execute(sql)
    base3=cursor.fetchone()
def bares4():
    sql=""
    sql="SELECT count(IF(battingRes=4 AND batterName='"+batterName+"')) FROM userData"
    cur.execute(sql)
    base4=cursor.fetchone()
def bares5():
    sql=""
    sql="SELECT count(IF(battingRes=5 AND batterName='"+batterName+"')) FROM userData"
    cur.execute(sql)
    ball4=cursor.fetchone()
def bares6():
    sql=""
    sql="SELECT count(IF(battingRes=6 AND batterName='"+batterName+"')) FROM userData"
    cur.execute(sql)
    hbp=cursor.fetchone()
def bares7():
    sql=""
    sql="SELECT count(IF(battingRes=7 AND batterName='"+batterName+"')) FROM userData"
    cur.execute(sql)
    fb=cursor.fetchone()
def bares8():
    sql=""
    sql="SELECT count(IF(battingRes=8 AND batterName='"+batterName+"')) FROM userData"
    cur.execute(sql)
    sacF=cursor.fetchone()
    con.close()
def bares9():
    sql=""
    sql="SELECT count(IF(battingRes=9 AND batterName='"+batterName+"')) FROM userData"
    cur.execute(sql)
    sto=cursor.fetchone()
    con.close()
def bares10():
    sql=""
    sql="SELECT count(IF(battingRes=9 AND batterName='"+batterName+"')) FROM userData"
    cur.execute(sql)
    sacB=cursor.fetchone()
    con.close()
def bares10():
    sql=""
    sql="SELECT count(IF(battingRes=9 AND batterName='"+batterName+"')) FROM userData"
    cur.execute(sql)
    gb=cursor.fetchone()
    con.close()
#타율 계산
batAVG=0.0
hitting=base1+base2+base3+base4
hitSum=hitting+fb+sto+gb
if hitSum==0:
   batAVG=0
else:
    batAVG=hitting/hitSum #안타개수/타수


#출루율 (obp)
if batSum+ball4+hbp+sacF == 0:
    OBP=0
else:
    OBP=(hitSum+ball4+hbp)/(batSum+ball4+hbp+sacF)

#(안타 개수 + 베이스온볼스 + 사구) ÷ (타수 + 베이스온볼스 + 사구 + 희생플라이)

#장타율 slg
if hitSum==0:
    SLG=0
else :
    SLG={base1+2*(2*base2)+3*(base3)+4*(base4)}/hitSum

#ops
OPS=OBP+SLG

#BABIP
if hitSum-so-base4+scarf == 0:
    BABIP=0
else :
    BABIP=(hitting-base4)/(hitSum-so-base4+scarf)






#데이터베이스 설정
def SaveLine():  ##데이터베이스에 데이터 저장
    con, cur = None, None
    sql = ""

    con = sqlite3.connect("C:/Users/한서영/PycharmProjects/untitled4/userData")  # DB가 저장된 폴더까지 지정
    con = sqlite3.connect(r"C:/Users/한서영/PycharmProjects/untitled4/userData")  # DB가 저장된 폴더까지 지정

    cur = con.cursor()

    sql = "INSERT INTO userData VALUES('" + str(pitcherName) + "', " + str(pitcherType) + "," + str(
        pitchType) + ", '" + str(batterName) + "', " + str(xPoint) + "," + str(yPoint) + ")"
    cur.execute(sql)

    con.commit()
    con.close()

def PrintData():
    con, cur = None, None
    sql = ""

    con = sqlite3.connect("C:/Users/한서영/PycharmProjects/untitled4/userData")  # DB가 저장된 폴더까지 지정
    con = sqlite3.connect(r"C:/Users/한서영/PycharmProjects/untitled4/userData")  # DB가 저장된 폴더까지 지정

    cur = con.cursor()

    cur.execute("SELECT * FROM userData")
    print("타자 이름     투수 정보     구종      투수 이름")
    print("-----------------------------------------------")
    data1, data2, data3, data4="","","",""
    while(True):
        row=cur.fetchone()
        if row==None:
            break
        data1=row[0]
        data2=row[1]
        if data2 == 1 :
            data2 = "좌투"
        if  data2 == 2 :
            data2 = "우투"
        data3=row[2]
        if  data3 == 1 :
            data3 = "직구"
        if  data3 == 2 :
            data3 = "슬라이더"
        data4=row[3]
        print("%4s   %7s    %6s    %5s"%(data1, data2, data3, data4))
    con.close()


canvas.bind("<Button-1>", clickLeft)

window.mainloop()
