from tkinter import*

from tkinter  import ttk
from tkPDFViewer import tkPDFViewer as pdf
  
from PIL import Image,ImageTk
import PIL
from tkinter import messagebox
import mysql.connector
import cv2

class Developer:

    def __init__(self,root):
        self.root=root 
        self.root.geometry("1350x780+0+0")
        self.root.title("Developer Details")


        title_labl=Label(self.root,text="DEVELOPER DETAILS",font=("times new roman",25,"bold"),bg="white",fg="red")
        title_labl.place(x=0,y=0,width=1430,height=35)


        img_top=Image.open(rb"college_images\dev.jpg")
        img_top=img_top.resize((1320,620))
        self.photo_img_top = ImageTk.PhotoImage(img_top)
        labell_top=Label(self.root, image=self.photo_img_top)
        labell_top.place(x=8,y=50,width=1320,height=620)


        img_top1=Image.open(rb"college_images\Abhi.jpg")
        img_top1=img_top1.resize((350,450))
        self.photo_img_top1 = ImageTk.PhotoImage(img_top1)
        labell_top1=Label(self.root, image=self.photo_img_top1)
        labell_top1.place(x=300,y=100,width=350,height=450)


        img_top2=Image.open(rb"college_images\abhishek.jpg")
        img_top2=img_top2.resize((520,550))
        self.photo_img_top2 = ImageTk.PhotoImage(img_top2)
        labell_top2=Label(self.root, image=self.photo_img_top2)
        labell_top2.place(x=700,y=100,width=520,height=550)



        # developer_frame=Frame(img_top,bd=2,bg="white" )
        # developer_frame,Place(x=100,y=0,width=1350,height=630)vc4 .   g





if __name__ == "__main__":

        root=Tk()

        obj=Developer(root)

        root.mainloop()