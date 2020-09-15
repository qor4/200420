from tkinter import *
import math
import random


## 클래스 선언 부분 ##
class Shape:  # 슈퍼 클래스
    color, width = '', 0
    shX1, shY1, shX2, shY2 = [0] * 4  # 도형을 포함하는 두 점

    def drawShape(self):  # 추상 메소드
        raise NotImplementedError()  # == pass


class Rectangle(Shape):  # 서브 클래스
    objects = None  # 사각형 선분 리스트

    def __init__(self, x1, y1, x2, y2, c, w):
        self.shX1 = x1
        self.shY1 = y1
        self.shX2 = x2
        self.shY2 = y2
        self.color = c
        self.width = w
        self.drawShape()

    def __del__(self):  # 사각형의 4개 선분을 제거함
        for obj in self.objects:
            canvas.delete(obj)

    def drawShape(self):  # 사각형 그리기로 오버라이딩
        sx1 = self.shX1;
        sy1 = self.shY1;
        sx2 = self.shX2;
        sy2 = self.shY2
        squreList = []
        squreList.append(canvas.create_line(sx1, sy1, sx1, sy2, fill=self.color, width=self.width))
        squreList.append(canvas.create_line(sx1, sy2, sx2, sy2, fill=self.color, width=self.width))
        squreList.append(canvas.create_line(sx2, sy2, sx2, sy1, fill=self.color, width=self.width))
        squreList.append(canvas.create_line(sx2, sy1, sx1, sy1, fill=self.color, width=self.width))
        self.objects = squreList  # 선분 리스트(=사각형)을 objects에 넣음


class Circle(Shape):  # 서브 클래스
    objects = None

    def __init__(self, x1, y1, x2, y2, c, w):
        self.shX1 = x1
        self.shY1 = y1
        self.shX2 = x2
        self.shY2 = y2
        self.color = c
        self.width = w
        self.drawShape()

    def __del__(self):  # 원은 객체 1개만 삭제
        canvas.delete(self.objects)

    def drawShape(self):  # 원형 그리기로 오버라이딩
        sx1 = self.shX1;
        sy1 = self.shY1;
        sx2 = self.shX2;
        sy2 = self.shY2
        self.objects = canvas.create_oval(sx1, sy1, sx2, sy2, outline=self.color, width=self.width)


## 함수 선언 부분 ##
def getColor():  # 임의의 색상 선택
    r = random.randrange(16, 256)  # 16진수로 변환시 0~A는 제외
    g = random.randrange(16, 256)
    b = random.randrange(16, 256)
    return "#" + hex(r)[2:] + hex(g)[2:] + hex(b)[2:]  # '#rrggbb' 형태로 만듬


def getWidth():  # 임의의 펜 두께 선택
    return random.randrange(1, 9)


## 이벤트 함수 선언 부분 ##
def startDrawRect(event):
    global x1, y1, x2, y2, shapes_R
    x1 = event.x  # 초기 도형 좌표값 지정
    y1 = event.y
    x2 = x1 + random.randrange(20, 80)  # 도형 크기 랜덤지정
    y2 = y1 - random.randrange(20, 80)
    rect = Rectangle(x1, y1, x2, y2, getColor(), getWidth())  # 사각형 생성
    shapes_R.append(rect)


def startDrawCircle(event):
    global x1, y1, x2, y2, shapes_C
    x1 = event.x
    y1 = event.y
    x2 = x1 + random.randrange(20, 80)
    y2 = y1 - random.randrange(20, 80)
    cir = Circle(x1, y1, x2, y2, getColor(), getWidth())  # 원 생성
    shapes_C.append(cir)


def deleteShape_C(event):  # 마지막에 그린 원 제거
    global shapes_C
    if len(shapes_C) != 0:  # 화면에 도형이 있으면 마지막 도형 제거
        shp = shapes_C.pop()
        del (shp)


def deleteShape_R(event):  # 마지막에 그린 사각형 제거
    global shapes_R
    if len(shapes_R) != 0:  # 화면에 도형이 있으면 마지막 도형 제거
        shp = shapes_R.pop()
        del (shp)


## 전역  변수 선언 ##
shapes_C = []  # 화면에 그려진 전체 도형 리스트
shapes_R = []
window = None
canvas = None
x1, y1, x2, y2 = None, None, None, None  # 클릭한 두 지점의 X, Y

## 메인 코드 부분 ##
if __name__ == "__main__":
    window = Tk()
    window.title("8주차 퀴즈 도형 그리기")
    canvas = Canvas(window, height=300, width=300)  # 캔버스 크기 설정

    canvas.bind("<Button-1>", startDrawRect)  # 마우스 왼쪽 1번 클릭시 사각형 만들기

    canvas.bind("<Button-3>", startDrawCircle)  # 마우스 오른쪽 1번 클릭 시 원 만들기

    canvas.bind("<Double-Button-1>", deleteShape_C)  # 마우스 왼쪽 2번 클릭 시 마지막 원 삭제
    canvas.bind("<Double-Button-2>", deleteShape_R)  # 마우스 가운데 2번 클릭 시 마지막 사각형 삭제

    canvas.pack()
    window.mainloop()
