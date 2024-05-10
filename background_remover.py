import tkinter
import customtkinter
# from tkinter import filedialog
from customtkinter import filedialog
from rembg import remove
from PIL import Image,ImageTk

output=''
def openfile():
    global file1
    global output
    file1=filedialog.askopenfilename(filetypes=[('JPG image','.jpg'),('PNG image','.png'),('JEPG image','.jepg')],title="Open Image File")
    img=ImageTk.PhotoImage(Image.open(file1).resize((box1.winfo_width(), box1.winfo_height())))
    box1.configure(image=img)
    #box1.image=img
def backr():
    global output
    input=Image.open(file1)
    output=remove(input)
    img2=ImageTk.PhotoImage(output.resize((380,260)))
    box2.configure(image=img2)
    # box2.image=img2

def savef():
    global output
    file2=filedialog.asksaveasfilename(filetypes=[('PNG image','.png'),('JPG image','.jpg'),('JEPG image','.jepg')],defaultextension=".png",title="Save The Image")
    output.save(file2)

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()
app.geometry("1140x560")
app.resizable(False,False)
app.title("IBR(Image Background Remover)")

default_image=ImageTk.PhotoImage(Image.new("RGB",(380,260),"white"))
# my_image=customtkinter.CTkImage(dark_image=Image.open("/home/hardik/Downloads/IMG20240321230938_00.jpg"),size=(100,200))
# my="/home/hardik/Downloads/IMG20240321230938_00.jpg"

box1=customtkinter.CTkLabel(app,image=default_image,text=" ")
box1.grid(column=0,row=0,padx=50,pady=70)

button3=customtkinter.CTkButton(app,width=10, height=60,text="Remove Background", corner_radius=220,border_width=2,command=backr)
button3.grid(column=1,row=0)

box2=customtkinter.CTkLabel(app,image=default_image,text=" ")
box2.grid(column=2,row=0,padx=50,pady=70)

button1=customtkinter.CTkButton(app, text="Select Image", width=200,height=50,command=openfile)
button1.grid(column=0,row=1)

button2=customtkinter.CTkButton(app, text="Save Image",width=200,height=50,command=savef)
button2.grid(column=2,row=1)

app.mainloop()
