import sqlite3
import turtle

#변수 선언
con, cur = None, None
row = None

batterinput = input() #사용자로 부터 입력받은 타자 이름 변수 -> 구체화 필요
pitcherTypeinput = input() #사용자로부터 입력받은 투수종류 변수
pitchTypeinput = input() #사용자로부터 입력받은 투구종류의 변수
pitcherNameinput = input() #사용자로부터 입력받은 투수이름의 변수

mainpointX = 279 #분포도에서 기준이 되는 시작 좌표의 값
mainpointY = 445 #y값

#메인 코드
con = sqlite3.connect(r"C:\sqlite\userData")
cur = con.cursor()
cursor.execute("SELECT * FROM userData")

## 타자이름 + 투수종류
def print_pitcherType_1() :

    while (True) :
        row = cur.fetchone()
        if row == None : #행이 비었으면 종료
            break;

        batter = row[3] #타자 이름을 저장
        pitcherType = row[1] #투수 종류를 저장
        pointX = row[4]
        pointY = row[5]

        if batter == batterinput :#타자이름을 비교함
            if pitcherType == 1 : #투수 종류를 비교

                r, g, b = getRGB()
                turtle.pencolor((r, g, b))

                t.shape("circle")
                t.shapesize(1, 1)

                t.up()
                t.goto(mainpointX, mainpointY)
                t.down()
                t.goto(pointX, pointY)
                t.done()

def print_pitcherType_2(Xpoint, Ypoint) :

    while (True) :
        row = cur.fetchone()
        if row == None : #행이 비었으면 종료
            break;

        batter = row[3] #타자 이름을 저장
        pitcherType = row[1] #투수 종류를 저장
        pointX = row[4]
        pointY = row[5]

        if batter == batterinput :#타자이름을 비교함
            if pitcherType == pitcherTypeinput : #투수 종류를 비교

                r, g, b = getRGB()
                turtle.pencolor((r, g, b))

                t.shape("circle")
                t.shapesize(1,1)

                t.up()
                t.goto(mainpointX, mainpointY)
                t.down()
                t.goto(pointX, pointY)
                t.done()

## 타자이름 + 투구 종류
def print_pitchType() :

   while (True):
        row = cur.fetchone()
        if row == None:  # 행이 비었으면 종료
            break;

        batter = row[3]  #타자 이름을 저장
        pitchTpye = row[2]  #타구 종류를 저장

        pointX = row[4]
        pointY = row[5]

        if batter == batterinput:# 타자이름을 비교함
            if pitchTpye == pitcherTypeinput : #타구를 비교
                r, g, b = getRGB()
                turtle.pencolor((r, g, b))

                t.shape("circle")
                t.shapesize(1, 1)

                t.up()
                t.goto(mainpointX, mainpointY)
                t.down()
                t.goto(pointX, pointY)
                t.done()




##타자이름 + 투수 이름
def print_pitcherName() :

    while (True):
        row = cur.fetchone()
        if row == None:  # 행이 비었으면 종료
            break;

        batter = row[3]  #타자 이름을 저장
        pitchername = row[0]  #투수 이름을 저장

        pointX = row[4]
        pointY = row[5]

        if batter == batterinput: # 타자이름을 비교함
            if pitchername == pitcherNameinput : #투수 이름을 비교
                r, g, b = getRGB()
                turtle.pencolor((r, g, b))

                t.shape("circle")
                t.shapesize(1, 1)

                t.up()
                t.goto(mainpointX, mainpointY)
                t.down()
                t.goto(pointX, pointY)
                t.done()

def print(Xpoint, Ypoint) :

        r, g, b = getRGB()
        turtle.pencolor((r, g, b))

        t.shape("circle")
        t.shapesize(1,1)

        t.up()
        t.goto(mainpointX, mainpointY)
        t.down()
        t.goto(Xpoint, Ypoint)
        t.done()

def getRGB() :
    r, g, b = 0,0,0
    r = random.random()
    g = random.random()
    b = random.random()
    return(r, g, b)
