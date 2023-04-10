from tkinter import *
from tkinter.filedialog import *

## 함수 선언 부분 ##
def func_open() :
    global filename
    filename = askopenfilename(parent = window, filetypes = (("GIF 파일", "*.gif"), ("모든 파일", "*.*")))
    photo = PhotoImage(file = filename)
    print("사진의 가로 x 세로 크기: %d x %d "%(photo.width(),photo.height()))    
    print(photo.get(0,0))
    pLabel.configure(image = photo)
    pLabel.image = photo        
def func_exit() :
    window.quit()
    window.destroy()
def func_gray() :
    photo = pLabel.image
    print("%s"%photo)
    width = photo.width()
    height = photo.height()
    for i in range(0, height) :
        for k in range(0, width) :
            r, g, b = photo.get(k, i)
            grey = int((r+g+b)/3)
            photo.put("#%02x%02x%02x" % (grey, grey, grey), (k, i))
            

## 메인 코드  부분 ##
window = Tk()
window.geometry("500x500")
window.title("명화 감상하기")

photo = PhotoImage()
photo2 = PhotoImage()
pLabel = Label(window, image = photo)
pLabel2 = Label(window, image = photo2)
# pLabel.pack(expand=1, anchor = CENTER)
pLabel.pack(expand=1, anchor = E)
pLabel2.pack(expand=1, anchor = W)
mainMenu = Menu(window)
window.config(menu = mainMenu)
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "파일", menu = fileMenu)
fileMenu.add_command(label = "파일 열기", command = func_open)
fileMenu.add_command(label = "Grayscale", command = func_gray)
fileMenu.add_separator()
fileMenu.add_command(label = "프로그램 종료", command = func_exit)

window.mainloop()
