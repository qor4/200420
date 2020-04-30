from tkinter import*

window = Tk()

window.title("아마추어를 위한 타구 분석 프로그램")
window.geometry("640x400")
window.resizable(False, False)

mainMenu = Menu(window)
window.config(menu=mainMenu)

#야구장 이미지 사진
photo = PhotoImage(file="야구장사진.gif")
label_image = Label(window, image=photo, bg="PINK", width=500, height=400)



#캔버스 설정
canvas = Canvas(window, bd=2, width=500, height=400)
canvas.create_image(250, 200, image = photo)
canvas.pack(fill="both", side="left")

#마우스 클릭
def clickLeft(event) :
    print(event.x, event.y)
    canvas.create_oval(event.x-2, event.y-2, event.x+2, event.y+2, fill = "red")


#메뉴 설정
fileMenu=Menu(mainMenu)
mainMenu.add_cascade(label="파일", menu=fileMenu)
fileMenu.add_command(label="입력")
fileMenu.add_separator() #메뉴 구분선
fileMenu.add_command(label="분석")



i=1 #list 순서
ls=Listbox(window, width=140, height=400, relief="sunken") #리스트 크기 지정
ls.insert(1, "ㅇㅇㅇ") #리스트 뜨는지 안뜨는지

#list 추가, 삭제 함수
def insert(number, name, i):
    ls.insert(i, name)
    i=i+1
def delete(i):
    ls.delete(ANCHOR) #ANCHOR 첫번째가 지워짐
    i=i-1


window.bind("<Button-1>", clickLeft)


#label_image.pack(side=LEFT)
ls.pack(side=RIGHT)


window.mainloop()
