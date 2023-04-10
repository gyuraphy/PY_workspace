from tkinter import *
window = Tk()
#gif, png 파일 이미지 확인 해보기
photo = PhotoImage(file = "gif/dog13.gif")
photo2 = PhotoImage(file = "gif/cat4.gif")
label1 = Label(window, image = photo)
label2 = Label(window, image = photo2)
label1.pack(side=LEFT);
label2.pack();

window.mainloop()
