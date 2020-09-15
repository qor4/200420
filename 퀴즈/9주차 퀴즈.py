import turtle
import random
import sqlite3


def SaveLine():  ##데이터베이스에 데이터 저장
    con, cur = None, None
    sql = " "

    con = sqlite3.connect("Turtle")  # DB가 저장된 폴더까지 지정
    cur = con.cursor()

    sql = "INSERT INTO Turtle VALUES(" + str(ID) + "," + str(r) + "," + str(g) + "," + str(b) + "," + str(
        Turn) + "," + str(curX) + "," + str(curY) + ")"
    cur.execute(sql)

    con.commit()
    con.close()


def ReversePaint():  ##순서 거꾸로 그리기
    sql = ""
    con = sqlite3.connect("Turtle")  # DB가 저장된 폴더까지 지정
    cur = con.cursor()
    sql = "SELECT R, G, B, X, Y FROM Turtle WHERE lineID=" + str(ID) + " AND Turn=" + str(j)
    cur.execute(sql)

    row = cur.fetchone()
    r = row[0]
    g = row[1]
    b = row[2]
    curx = row[3]
    cury = row[4]

    if (j == turn[ID]):
        turtle.penup()
        turtle.goto(curx, cury)
        turtle.pendown()
        turtle.pencolor((r, g, b))

    elif (j == 2):
        turtle.goto(curx, cury)
        turtle.pencolor((r, g, b))
        turtle.goto(0, 0)

    else:
        turtle.goto(curx, cury)
        turtle.pencolor((r, g, b))

    con.close()


## 전역 변수 선언 부분 ##
swidth, sheight, pSize, exitCount, ID, Turn = 300, 300, 3, 0, 1, 2
r, g, b, angle, dist, curX, curY = [0] * 7
turn = [0, 0, 0, 0, 0, 0]

## 메인 코드 부분 ##
turtle.title('거북이가 맘대로 다니기')
turtle.shape('turtle')
turtle.pensize(pSize)
turtle.setup(width=swidth + 30, height=sheight + 30)
turtle.screensize(swidth, sheight)

while True:
    r = random.random()
    g = random.random()
    b = random.random()
    turtle.pencolor((r, g, b))

    angle = random.randrange(0, 360)
    dist = random.randrange(1, 100)
    turtle.left(angle)
    turtle.forward(dist)
    curX = turtle.xcor()
    curY = turtle.ycor()

    SaveLine()
    Turn += 1

    if (-swidth / 2 <= curX and curX <= swidth / 2) and (-sheight / 2 <= curY and curY <= sheight / 2):
        pass
    else:
        turtle.penup()
        turtle.goto(0, 0)
        turtle.pendown()
        turn[ID] = Turn - 1

        ID += 1
        Turn = 2

        exitCount += 1
        if exitCount >= 5:
            ID -= 1
            break

turtle.clear()

for i in range(ID, 0, -1):
    for j in range(turn[ID], 1, -1):
        ReversePaint()
    ID -= 1

turtle.done()
