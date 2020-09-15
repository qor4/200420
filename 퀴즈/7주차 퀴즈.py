from tkinter import *
from tkinter.filedialog import *

## 함수 선언 부분 ##

def brighter() : #사진을 밝게 해주는 함수
    global inImage, XSIZE, YSIZE
    rgbString = ""
    for i in range(0, XSIZE) :
        tmpString = ""
        for k in range(0, YSIZE) :
            data = inImage[i][k] + 100
            if data > 255:
                data = 255
            tmpString += "#%02x%02x%02x " % (data, data, data) # x 뒤에 한칸 공백, 16진수 문자열로 만듦
        rgbString += "{" + tmpString +  "} " # } 뒤에 한칸 공백
    paper.put(rgbString)

def darker() : #사진을 어둡게 해주는 함수
    global inImage, XSIZE, YSIZE
    rgbString = ""
    for i in range(0, XSIZE) :
        tmpString = ""
        for k in range(0, YSIZE) :
            data = inImage[i][k] - 100
            if data < 0:
                data = 0
            tmpString += "#%02x%02x%02x " % (data, data, data) # x 뒤에 한칸 공백, 16진수 문자열로 만듦
        rgbString += "{" + tmpString +  "} " # } 뒤에 한칸 공백
    paper.put(rgbString)

def reverse():
    global inImage, XSIZE, YSIZE
    rgbString = ""
    for i in range(0, XSIZE):
        tmpString = ""
        for k in range(0, YSIZE):
            data = 255 - inImage[i][k]
            tmpString += "#%02x%02x%02x " % (data, data, data)  # x 뒤에 한칸 공백, 16진수 문자열로 만듦
        rgbString += "{" + tmpString + "} "  # } 뒤에 한칸 공백
    paper.put(rgbString)

def loadImage(fname) :
    global inImage, XSIZE, YSIZE
    fp = open(fname, 'rb')

    for i in range(0, XSIZE) :
        tmpList = []
        for k in range(0, YSIZE) :
            data = int(ord(fp.read(1)))
            tmpList.append(data)
        inImage.append(tmpList)

    fp.close()

def displayImage(image) :
    global XSIZE, YSIZE
    rgbString = ""
    for i in range(0, XSIZE) :
        tmpString = ""
        for k in range(0, YSIZE) :
            data = image[i][k]
            tmpString += "#%02x%02x%02x " % (data, data, data) # x 뒤에 한칸 공백, 16진수 문자열로 만듦
        rgbString += "{" + tmpString +  "} " # } 뒤에 한칸 공백
    paper.put(rgbString)

def func_open() :
    filename = askopenfilename(parent = window, filetypes = (("raw 파일", "*.raw"), ("모든 파일", "*.*")))
    loadImage(filename)
    displayImage(inImage)

## 전역 변수 선언 부분 ##
window = None
canvas = None
XSIZE, YSIZE=256,256
inImage=[] # 2차원 리스트 (메모리)

## 메인 코드 부분 ##
window = Tk()
window.title("흑백 사진 보기")
canvas = Canvas(window, height = XSIZE, width = YSIZE)
paper = PhotoImage(width = XSIZE, height = YSIZE)
canvas.create_image((XSIZE/2, YSIZE/2), image = paper, state = "normal")

mainmenu=Menu(window)
window.config(menu = mainmenu)
filemenu = Menu(mainmenu)
effectmenu = Menu(mainmenu)

mainmenu.add_cascade(label = "파일", menu = filemenu)
mainmenu.add_cascade(label = "사진효과", menu = effectmenu)
filemenu.add_command(label = "파일 열기", command = func_open)
effectmenu.add_command(label = "밝게 하기", command = brighter)
effectmenu.add_separator()
effectmenu.add_command(label = "어둡게 하기", command = darker)
effectmenu.add_separator()
effectmenu.add_command(label = "반전 이미지", command = reverse)
effectmenu.add_separator()

# 메모리 --> 화면

canvas.pack()


window.mainloop()
