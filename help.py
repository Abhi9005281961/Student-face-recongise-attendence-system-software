from tkinter import*
from tkinter  import ttk
from PIL import Image,ImageTk
import PIL
from tkinter import messagebox
import mysql.connector
import cv2

class Help:

    def __init__(self,root):
        self.root=root 
        self.root.geometry("1350x780+0+0")
        self.root.title("Help Desk")


        title_labl=Label(self.root,text="Help Desk",font=("times new roman",25,"bold"),bg="white",fg="red")
        title_labl.place(x=0,y=0,width=1430,height=35)


        img_top=Image.open(rb"college_images\help.jpeg")
        img_top=img_top.resize((1320,620))
        self.photo_img_top = ImageTk.PhotoImage(img_top)
        labell_top=Label(self.root, image=self.photo_img_top)
        labell_top.place(x=8,y=50,width=1320,height=620)


        dev_labl=Label(self.root,text="Email : avaishya@gmail.com",font=("times new roman",25,"bold"),bg="white",fg="red")
        dev_labl.place(x=430,y=180,)



if __name__ == "__main__":

        root=Tk()

        obj=Help(root)

        root.mainloop()