from tkinter import *
from PIL import Image, ImageTk
from googletrans import Translator
# tạo tkinter trên window
root = Tk()
root.title("Google Translate")
root.geometry("500x630")
root.iconbitmap("logo.ico")
# background
load = Image.open("den.jpg")
render = ImageTk.PhotoImage(load)
img = Label(root, image=render)
img.place(x= 0, y = 0)
# font chữ
name = Label(root, text = "Translator", fg = "#FFFFFF", bd = 0, bg = "#000000")
name.config(font = ("Transformers Movie", 30))
name.pack(pady = 10) # hàm này dùng để thụt lề, ở đây là thụ lề trên (y) xuống 10px
# hộp thoại cần dịch
box = Text(root, width=28, height=8, font=("ROBOTO", 16))
box.pack(pady = 20)
# dữ liệu nằm ở 2 cái hàm này
def clear():
    box.delete(1.0, END)
    box1.delete(1.0, END)
def translate():
    INPUT = box.get(1.0, END)
    print(INPUT)
    t = Translator()
    a = t.translate(INPUT, src = "en", dest = "vi")
    b = a.text
    box1.insert(END, b)
# hai nút dịch và xóa
button_frame = Frame(root).pack(side = BOTTOM)
clear_button = Button(button_frame, text = "Clear text", font = (("Arial"), 10, "bold"), bg = "#303030", fg = "#FFFFFF", command=clear)
clear_button.place(x = 150, y = 310)
trans_button = Button(button_frame, text = "Translate", font = (("Arial"), 10, "bold"), bg = "#303030", fg = "#FFFFFF", command=translate)
trans_button.place(x = 290, y = 310)
# hộp thoại được dịch
box1 = Text(root, width=28, height=8, font=("ROBOTO", 16))
box1.pack(pady = 50)

root.mainloop()