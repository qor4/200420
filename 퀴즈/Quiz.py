from tkinter import *
from tkinter.filedialog import *
from tkinter.simpledialog import *

## 함수 선언 부분 ##
def func_open() :
    global photo
    filename = askopenfilename(parent = window, filetypes = (("GIF 파일", "*.gif"), ("모든 파일", "*.*")))
    photo = PhotoImage(file = filename)
    pLabel.configure(image = photo)
    pLabel.image = photo

def func_exit() :
    window.quit()
    window.destroy()

def func_zoom():
    global photo
    value = askinteger("확대 배수", "확대할 배수를 입력하세요(2~8)", minvalue=2, maxvalue=8)
    photo = photo.zoom(value, value)
    pLabel.configure(image = photo)
    pLabel.image = photo


def func_subsample():
    global photo
    value = askinteger("축소 배수", "축소할 배수를 입력하세요(2~8)", minvalue=2, maxvalue=8)
    photo = photo.subsample(value, value)
    pLabel.configure(image = photo)
    pLabel.image = photo

## 메인 코드  부분 ##
window = Tk()
window.geometry("1000x1000")
window.title("명화 감상하기")


photo = PhotoImage()
pLabel = Label(window, image = photo)
pLabel.pack(expand=1, anchor = CENTER)

mainMenu = Menu(window)
window.config(menu = mainMenu)
fileMenu1 = Menu(mainMenu)
fileMenu2 = Menu(mainMenu)

mainMenu.add_cascade(label = "파일", menu = fileMenu1)
mainMenu.add_cascade(label = "이미지 효과", menu = fileMenu2)
fileMenu1.add_command(label = "파일 열기", command = func_open)
fileMenu1.add_separator()
fileMenu1.add_command(label = "프로그램 종료", command = func_exit)
fileMenu2.add_command(label = "확대하기", command = func_zoom)
fileMenu2.add_separator()
fileMenu2.add_command(label = "축소하기", command = func_subsample)

window.mainloop()

