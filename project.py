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
window.config(menu = mainMenu, background="linen")

#야구장 이미지 사진
photo = PhotoImage(file = "야구장사진.gif")
label_image = Label(window, image = photo)

#메뉴 설정
def help_top():
    help_w = Toplevel(window)
    help_w.title("도움말")
    help_w.geometry("500x500")

    label_w =Label(help_w, text="\n\n\n아마추어를 위한 타구 분석 프로그램\n\n "
                                "입력\n"
                                "주어진 항목들을 입력하여 주십시오.\n"
                                "투수 이름과 타자 이름을 입력한 뒤 입력창 옆 '입력' 버튼을 눌러주십시오.\n"
                                "투수 정보 선택, 구종 선택, 타격 결과의 선택지를 선택하여주십시오.\n"
                                "프로그램의 야구장 그림에 공이 떨어진 위치를 선택하여 주십시오.\n"
                                "위의 정보들을 모두 입력했을경우 프로그램 상단의 '입력' 버튼을 눌러주십시오.\n\n"
                                ""
                                "분석\n"
                                "분석 항목은\n"
                                "1. 투수 정보 + 타자 이름\n"
                                "2. 구종+타자 이름\n"
                                "3. 투수 이름+타자 이름\n"
                                "의 데이터를 매칭하여 공이 떨어진 위치를 보여줍니다.\n\n"
                                ""
                                "따라서 위와 같은 정보를 입력한 뒤 프로그램 상단의 '분석' 버튼을 눌러주십시오.\n\n"
                                ""
                                "수비 추천\n"
                                "수비 추천 항목은 투수 이름 + 타자 이름을\n"
                                "입력받아 구역별 수비수 위치를 추천해줍니다.\n\n"
                                ""
                                "투수 이름과 타자 이름을 입력한 뒤 프로그램 상단의 '수비 추천' 버튼을 눌러주십시오.\n\n\n")
    label_w.pack()

def close():
    window.quit()
    window.destroy()

fileMenu=Menu(mainMenu)
helpMenu=Menu(mainMenu)

mainMenu.add_cascade(label="프로그램", menu=fileMenu)
fileMenu.add_command(label="도움말", command=help_top)
fileMenu.add_separator() #메뉴 구분선
fileMenu.add_command(label="종료", command=close)

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
batSum=0
hbp=0
sto=0
gb=0
sacF=0


#분석 화면 사용 변수 선언
mainpointX = 279 #분포도에서 기준이 되는 시작 좌표의 값
mainpointY = 446 #y값

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
    #XPOINT, YPOINT = [], []
    con = sqlite3.connect(r"C:\Users\Owner\Desktop\program\sqlite\userData")
    cur = con.cursor()
    cur.execute(sql)
    while (True):
        row = cur.fetchone()
        if row == None:
            break;
        XPOINT=row[0]
        YPOINT=row[1]

        #원 표시하는 것
        #x1, y1 = (XPOINT - 1), (YPOINT - 1)
        #x2, y2 = (XPOINT + 1), (YPOINT + 1)
        #canvas.create_oval(x1, y1, x2, y2, width = 5)

        #선으로 표시하는 것
        #canvas.create_line(mainpointX, mainpointY, XPOINT, YPOINT, fill="#009770")

        #엑스 표시
        x1, y1 = (XPOINT - 3), (YPOINT - 3)
        x2, y2 = (XPOINT + 3), (YPOINT + 3)
        x3, y3 = (XPOINT + 3), (YPOINT - 3)
        x4, y4 = (XPOINT - 3), (YPOINT + 3)
        #색상은 색상 16진수 표현으로 하면됨
        canvas.create_line(x1, y1, x2, y2, width = 2, fill = "red")
        canvas.create_line(x3, y3, x4, y4, width = 2, fill = "red")

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
    sql = "SELECT xPoint, yPoint, pitcherType, pitchType FROM userData WHERE batterName='" + batterName + "' AND pitcherName='" + pitcherName + "' AND battingRes <>" + str(4)

    manType, ballType = [], []
    point = []
    con = sqlite3.connect(r"C:\Users\Owner\Desktop\program\sqlite\userData")
    cur = con.cursor()
    cur.execute(sql)
    count = 0
    while (True):
        row = cur.fetchone()
        if row == None:
            break;
        X = row[0]
        Y = row[1]
        manType.append(row[2])
        ballType.append(row[3])
        count = count + 1
        point.append([X, Y])

    Xpoint1, Xpoint2, Xpoint3, Xpoint4, Ypoint1, Ypoint2, Ypoint3, Ypoint4 = [], [], [], [], [], [], [], []
    array1, array2, array3, array4 = 0, 0, 0, 0

    for i, k in point:
        if(i < 215 and k < 200):
            Xpoint1.append(i)
            Ypoint1.append(k)
            array1 = array1 + 1
        elif (i < 345 and k < 200):
            Xpoint2.append(i)
            Ypoint2.append(k)
            array2 = array2 + 1

        elif (i < 555 and k < 200):
            Xpoint3.append(i)
            Ypoint3.append(k)
            array3 = array3 + 1

        elif (i < 280 and k < 340):
            Xpoint4.append(i)
            Ypoint4.append(k)
            array4 = array4 + 1




    if(array1 != 0):
        xaver1 = averXpoint(Xpoint1, array1)
        yaver1 = averYpoint(Ypoint1, array1)
        print_recoDefence(xaver1, yaver1)
    elif (array1 == 0):
        print_recoDefence(130, 150)

    if (array2 != 0):
        xaver2 = averXpoint(Xpoint2, array2)
        yaver2 = averYpoint(Ypoint2, array2)
        print_recoDefence(xaver2, yaver2)
    elif (array2 == 0):
        print_recoDefence(280, 100)


    if (array3 != 0):
        xaver3 = averXpoint(Xpoint3, array3)
        yaver3 = averYpoint(Ypoint3, array3)
        print_recoDefence(xaver3, yaver3)
    elif (array3 == 0):
        print_recoDefence(430, 150)


    if (array4 != 0):
        xaver4 = averXpoint(Xpoint4, array4)
        yaver4 = averYpoint(Ypoint4, array4)
        print_recoDefence(xaver4, yaver4)
    elif (array4 == 0):
        print_recoDefence(180, 250)



    manaver = avermanType(manType)
    ballaver = averballType(ballType)


def print_recoDefence(Xpoint, Ypoint):
    x1, y1 = (Xpoint - 5), (Ypoint - 5)
    x2, y2 = (Xpoint + 5), (Ypoint + 5)

    canvas.create_oval(x1, y1, x2, y2, fill="powderblue")



##x좌표 평균값
def averXpoint(XPOINT, num):
    Xsum = 0
    Xaver = 0
    for x in range(0, num):
        Xsum += XPOINT[x]
    Xaver = Xsum/len(XPOINT)
    return Xaver

##y좌표 평균값
def averYpoint(YPOINT, num):
    Ysum = 0
    Yaver = 0
    for y in range(0, num):
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
def delete_display():
    canvas.delete("all")
    canvas.create_image(280, 250, image=photo)


def bares1():
    global base1
    bares1= []
    sql=""
    sql="SELECT count(*) FROM userData WHERE battingres=1 AND batterName='" + batterName+"'"
    con = sqlite3.connect(r"C:\Users\Owner\Desktop\program\sqlite\userData")
    cur = con.cursor()
    cur.execute(sql)
    bares1=cur.fetchone()
    base1= bares1[0]
    con.close()

def bares2():
    global base2
    bares2=[]
    sql=""
    sql="SELECT count(*) FROM userData WHERE battingres=2 AND batterName='" + batterName+"'"
    con = sqlite3.connect(r"C:\Users\Owner\Desktop\program\sqlite\userData")
    cur = con.cursor()
    cur.execute(sql)
    bares2=cur.fetchone()
    base2 = bares2[0]
    con.close()

def bares3():
    global base3
    bares3=[]
    sql=""
    sql="SELECT count(*) FROM userData WHERE battingres=3 AND batterName='" + batterName+"'"
    con = sqlite3.connect(r"C:\Users\Owner\Desktop\program\sqlite\userData")
    cur = con.cursor()
    cur.execute(sql)
    bares3 = cur.fetchone()
    base3 = bares3[0]
    con.close()

def bares4():
    global base4
    bares4 = []
    sql=""
    sql="SELECT count(*) FROM userData WHERE battingres=4 AND batterName='" + batterName+"'"
    con = sqlite3.connect(r"C:\Users\Owner\Desktop\program\sqlite\userData")
    cur = con.cursor()
    cur.execute(sql)
    bares4 = cur.fetchone()
    base4 = bares4[0]
    con.close()

def bares5():
    global ball4
    bares5=[]
    sql=""
    sql="SELECT count(*) FROM userData WHERE battingres=5 AND batterName='" + batterName+"'"
    con = sqlite3.connect(r"C:\Users\Owner\Desktop\program\sqlite\userData")
    cur = con.cursor()
    cur.execute(sql)
    bares5 = cur.fetchone()
    ball4 = bares5[0]
    con.close()

def bares6():
    global hbp
    bares6=[]
    sql=""
    sql="SELECT count(*) FROM userData WHERE battingres=6 AND batterName='" + batterName+"'"
    con = sqlite3.connect(r"C:\Users\Owner\Desktop\program\sqlite\userData")
    cur = con.cursor()
    cur.execute(sql)
    bares6 = cur.fetchone()
    hbp = bares6[0]
    con.close()

def bares7():
    global fb
    bares7=[]
    sql=""
    sql="SELECT count(*) FROM userData WHERE battingres=7 AND batterName='" + batterName+"'"
    con = sqlite3.connect(r"C:\Users\Owner\Desktop\program\sqlite\userData")
    cur = con.cursor()
    cur.execute(sql)
    bares7 = cur.fetchone()
    fb = bares7[0]
    con.close()

def bares8():
    global sacF
    bares8=[]
    sql=""
    sql="SELECT count(*) FROM userData WHERE battingres=8 AND batterName='" + batterName+"'"
    con = sqlite3.connect(r"C:\Users\Owner\Desktop\program\sqlite\userData")
    cur = con.cursor()
    cur.execute(sql)
    bares8 = cur.fetchone()
    sacF = bares8[0]
    con.close()

def bares9():
    global sto
    bares9=[]
    sql=""
    sql="SELECT count(*) FROM userData WHERE battingres=9 AND batterName='" + batterName+"'"
    con = sqlite3.connect(r"C:\Users\Owner\Desktop\program\sqlite\userData")
    cur = con.cursor()
    cur.execute(sql)
    bares9 = cur.fetchone()
    sto = bares9[0]
    con.close()

def bares10():
    global sacB
    bares10=[]
    sql=""
    sql="SELECT count(*) FROM userData WHERE battingres=10 AND batterName='" + batterName+"'"
    con = sqlite3.connect(r"C:\Users\Owner\Desktop\program\sqlite\userData")
    cur = con.cursor()
    cur.execute(sql)
    bares10 = cur.fetchone()
    sacB = bares10[0]
    con.close()

def bares11():
    global gb
    bares11=[]
    sql=""
    sql="SELECT count(*) FROM userData WHERE battingres=11 AND batterName='" + batterName+"'"
    con = sqlite3.connect(r"C:\Users\Owner\Desktop\program\sqlite\userData")
    cur = con.cursor()
    cur.execute(sql)
    bares11 = cur.fetchone()
    gb = bares11[0]
    con.close()

def calcul():
#타율 계산
    global batAVG
    batAVG=0.0
    hitting=base1+base2+base3+base4
    hitSum=hitting+fb+sto+gb

    if hitSum==0:
        batAVG=0
    else:
        batAVG=hitting/hitSum #안타개수/타수
        print(batAVG)


#출루율 (obp)
    global OBP
    OBP = 0
    if batSum+ball4+hbp+sacF == 0:
        OBP=0
    else:
        OBP=(hitSum+ball4+hbp)/(batSum+ball4+hbp+sacF)

#(안타 개수 + 베이스온볼스 + 사구) ÷ (타수 + 베이스온볼스 + 사구 + 희생플라이)

#장타율 slg
    global SLG
    SLG = 0
    if hitSum==0:
        SLG=0
    else :
        SLG=(base1+2*(2*base2)+3*(base3)+4*(base4))/hitSum

#ops
    global OPS
    OPS = 0
    OPS=OBP+SLG

#BABIP
    global BABIP
    BABIP = 0

    if hitSum-sto-base4+sacF == 0:
        BABIP=0
    else :
        BABIP=(hitting-base4)/(hitSum-sto-base4+sacF)


def battingresdata():

    bares1()
    bares2()
    bares3()
    bares4()
    bares5()
    bares6()
    bares7()
    bares8()
    bares9()
    bares10()
    bares11()

    calcul()

    label6 = Label(window, text="타율:" + str(round(batAVG,5)), background="linen")
    label6.place(x=800, y=265)
    label7 = Label(window, text="장타율:" + str(round(SLG,5)), background="linen")
    label7.place(x=800, y=295)
    label8 = Label(window, text="OPS:" + str(round(OPS,5)), background="linen")
    label8.place(x=800, y=325)
    label9 = Label(window, text="BABIP:" + str(round(BABIP,5)), background="linen")
    label9.place(x=800, y=355)
    label10 = Label(window, text="출루율:" + str(round(OBP,5)), background="linen")
    label10.place(x=800, y=385)






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
        delete_display()
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
            delete_display()
            analyse_Leftpitcher()
            battingresdata()
            resetVari()


    elif pitcherType == 2:
        ans = messagebox.askquestion("확인", "투수 정보 : 우투" + "\n타자 이름 : " + batterName + "\n이 맞습니까?")
        if ans == "yes":
            delete_display()
            analyse_Rightpitcher()
            battingresdata()
            resetVari()


    elif pitchType == 1:
        ans = messagebox.askquestion("확인", "구종 : 직구" + "\n타자 이름 : " + batterName + "\n이 맞습니까?")
        if ans == "yes":
            delete_display()
            analyse_Fastball()
            battingresdata()
            resetVari()


    elif pitchType == 2:
        ans = messagebox.askquestion("확인", "구종 : 슬라이더" + "\n타자 이름 : " + batterName + "\n이 맞습니까?")
        if ans == "yes":
            delete_display()
            analyse_Slider()
            battingresdata()
            resetVari()


    elif pitcherName != None:
        ans = messagebox.askquestion("확인", "투수 이름 : " + pitcherName + "\n타자 이름 : " + batterName + "\n이 맞습니까?")
        if ans == "yes":
            delete_display()
            analyse_pitcher()
            battingresdata()
            resetVari()


def recommend_messageask():
    ans = messagebox.askquestion("확인", "투수 이름 : " + pitcherName + "\n타자 이름 : " + batterName + "\n이 맞습니까?")
    if ans == "yes":
        delete_display()
        recoDefence()

#분포도 출력
def print_batterLine(xPoint, yPoint):
    r, g, b = getRGB()
    canvas.create_line(mainpointX, mainpointY, xPoint, yPoint)

#분포도 색갈 랜덤 지정
def getRGB() :
    r, g, b = 0,0,0
    r = random.random()
    g = random.random()
    b = random.random()
    return(r, g, b)





#입력 정보
button1=Button(window, text="입력", relief="groove", bg="powderblue", command=input_messageask)
button1.place(x=570, y=20)
button2=Button(window, text="분석", relief="groove", bg="Salmon", command=analyse_messageask)
button2.place(x=610, y=20)
button3=Button(window, text="수비 추천", relief="groove", bg="PeachPuff", command =recommend_messageask)
button3.place(x=650, y=20)

label1=Label(window, text="  투수 이름  ", background="linen")
label1.place(x=570, y=80)
entry1=Entry(window, width=16) #투수정보
entry1.place(x=570, y=103)
button4=Button(window, text="입력", relief="groove", bg="PeachPuff", command=clickbutton4)
button4.place(x=690, y=100)

label2=Label(window, text=" 투수 정보 선택 ", background="linen")
label2.place(x=570, y=150)
button5=Button(window, text="   좌투   ", relief="groove", bg="lemonchiffon", command=clickbutton5)
button5.place(x=570, y=175)
button6=Button(window, text="   우투   ", relief="groove", bg="lemonchiffon", command=clickbutton6)
button6.place(x=640, y=175)


label3=Label(window, text="  구종 선택  ", background="linen")
label3.place(x=570, y=230)
button7=Button(window, text="   직구   ", relief="groove", bg="lightpink", command=clickbutton7)
button7.place(x=570, y=255)
button8=Button(window, text="슬라이더", relief="groove", bg="lightpink", command=clickbutton8)
button8.place(x=640, y=255)


label4=Label(window, text="  타자 이름  ", background="linen")
label4.place(x=570, y=310)
entry2=Entry(window, width=16) #타자정보
entry2.place(x=570, y=333)
button9=Button(window, text="입력", relief="groove", bg="PeachPuff", command=clickbutton9)
button9.place(x=690, y=330)

label5=Label(window, text=" 타격 결과 ", background="linen")
label5.place(x=800, y=20)
button10=Button(window, text="    1루타    ", relief="groove", bg="lavender", command=clickbutton10)
button10.place(x=800, y=45)
button11=Button(window, text="    2루타    ", relief="groove", bg="lavender", command=clickbutton11)
button11.place(x=890, y=45)
button12=Button(window, text="    3루타    ", relief="groove", bg="lavender", command=clickbutton12)
button12.place(x=800, y=80)
button13=Button(window, text="     홈런     ", relief="groove", bg="lavender", command=clickbutton13)
button13.place(x=890, y=80)
button14=Button(window, text="     볼넷     ", relief="groove", bg="lavender", command=clickbutton14)
button14.place(x=800, y=115)
button15=Button(window, text="     사구     ", relief="groove", bg="lavender", command=clickbutton15)
button15.place(x=890, y=115)
button16=Button(window, text="     뜬공     ", relief="groove", bg="lavender", command=clickbutton16)
button16.place(x=800, y=150)
button17=Button(window, text=" 희생플라이", relief="groove", bg="lavender", command=clickbutton17)
button17.place(x=890, y=150)
button18=Button(window, text="     삼진     ", relief="groove", bg="lavender", command=clickbutton18)
button18.place(x=800, y=185)
button18=Button(window, text="  희생번트  ", relief="groove", bg="lavender", command=clickbutton19)
button18.place(x=890, y=185)
button18=Button(window, text="     땅볼     ", relief="groove", bg="lavender", command=clickbutton20)
button18.place(x=800, y=220)


label6 = Label(window, text="타율:" + str(batAVG), background="linen")
label6.place(x=800, y=265)
label7 = Label(window, text="장타율:" + str(SLG), background="linen")
label7.place(x=800, y=295)
label8 = Label(window, text="OPS:" + str(OPS), background="linen")
label8.place(x=800, y=325)
label9 = Label(window, text="BABIP:" + str(BABIP), background="linen")
label9.place(x=800, y=355)
label10 = Label(window, text="출루율:" + str(OBP), background="linen")
label10.place(x=800, y=385)

#db 불러와서 맵핑
def Dataa():
    con = sqlite3.connect(r"C:\Users\Owner\Desktop\program\sqlite\userData")
    cur = con.cursor()
    cur.execute("SELECT * FROM userData")


#데이터베이스 설정
def SaveLine():  ##데이터베이스에 데이터 저장
    con, cur = None, None
    sql = ""

    con = sqlite3.connect(r"C:\Users\Owner\Desktop\program\sqlite\userData")  # DB가 저장된 폴더까지 지정

    cur = con.cursor()

    sql = "INSERT INTO userData VALUES('" + str(pitcherName) + "', " + str(pitcherType) + "," + str(
        pitchType) + ", '" + str(batterName) + "', " + str(battingRes) + "," + str(xPoint) + "," + str(yPoint) + ")"
    cur.execute(sql)

    con.commit()
    con.close()

def PrintData():
    con, cur = None, None
    sql = ""

    con = sqlite3.connect(r"C:\Users\Owner\Desktop\program\sqlite\userData")  # DB가 저장된 폴더까지 지정

    cur = con.cursor()

    cur.execute("SELECT * FROM userData")
    print("타자 이름     투수 정보     구종      투수 이름     투구 결과")
    print("----------------------------------------------------------")
    data1, data2, data3, data4, data5="","","","",""
    while(True):
        row=cur.fetchone()
        if row==None:
            break;
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
        data5=row[4]
        if  data5 == 1 :
            data5 = "1루타"
        if  data5 == 2 :
            data5 = "2루타"
        if  data5 == 3 :
            data5 = "3루타"
        if  data5 == 4 :
            data5 = "홈런"
        if  data5 == 5 :
            data5 = "볼넷"
        if  data5 == 6 :
            data5 = "사구"
        if  data5 == 7 :
            data5 = "뜬공"
        if  data5 == 8 :
            data5 = "희생플라이"
        if  data5 == 9 :
            data5 = "삼진"


        print("%4s   %7s    %6s    %5s   %6s"%(data1, data2, data3, data4, data5))
    con.close()


canvas.bind("<Button-1>", clickLeft)

window.mainloop()
