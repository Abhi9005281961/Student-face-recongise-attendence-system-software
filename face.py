from tkinter import*
from tkinter  import ttk
from PIL import Image,ImageTk
import PIL
import os
import tkinter
from time import strftime
from datetime import datetime
from train import Train
from face_recognition import Recognition
from student import Student
from developer import Developer
from help import Help






class face_recongnition_system:

    def __init__(self,root):
        self.root=root 
        self.root.geometry("1350x780+0+0")
        self.root.title("face Recongnition System")



       
        img1=Image.open(rb"C:\Users\Dell\Desktop\image\college_images\BestFacialRecognition.jpg")
        # self.photoimg1=ImageTk.PhotoImage(img1)
        img1=img1.resize((500, 130))
        self.img = ImageTk.PhotoImage(img1)
        labell=Label(self.root, image=self.img)
        labell.place(x=0,y=0,width=500,height=130)
        # labell.image=img
        # labell.pack()
        # first_lbl=Label(self.root,image=self.photoimg1)
        # first_lbl.place(x=0,y=0,width=500,height=130)
        # -----------------------------------------------------------------------------------------------------
        img2=Image.open(rb"C:\Users\Dell\Desktop\image\college_images\facialrecognition.png")
        img2=img2.resize((500, 130))
        self.img_1 = ImageTk.PhotoImage(img2)
        labell=Label(self.root, image=self.img_1)
        labell.place(x=500,y=0,width=500,height=130)
        # -----------------------------------------------------------------------------------------------------
        img3=Image.open(rb"C:\Users\Dell\Desktop\image\college_images\ai.jpeg")
        img3=img3.resize((500, 130))
        self.img_2 = ImageTk.PhotoImage(img3)
        labell=Label(self.root, image=self.img_2)
        labell.place(x=1000,y=0,width=400,height=130)
        # ---------bg------------------------
        img4=Image.open(rb"C:\Users\Dell\Desktop\image\college_images\ai.jpeg")
        img4=img4.resize((1450,620))
        self.img_3 = ImageTk.PhotoImage(img4)
        bg_img=Label(self.root, image=self.img_3)
        bg_img.place(x=0,y=130,width=1450,height=620)

        

#  -------for text write
        title_labl=Label(bg_img, text="FACE  RECOGNITION  ATTENDANCE  SYSTEM  SOFTWARE",font=("times new roman",25,"bold"),bg="white",fg="red")
        title_labl.place(x=0,y=0,width=1430,height=35)

        # ===========time ======

        def time():
                string=strftime("%H:%M:%S%p")
                lbl.config(text=string)
                lbl.after(1000,time)

        lbl=Label(title_labl,font=('times now romen',14,"bold"),background='white',foreground='blue')
        lbl.place(x=15,y=0)
        # lbl.pack(anchor="center")
        time()
                

#   button 1------------
        img5=Image.open(rb"C:\Users\Dell\Desktop\image\college_images\AdobeStock_303989091.jpeg")
        img5=img5.resize((160,160))
        self.photoimg4=ImageTk.PhotoImage(image=img5)
        b1=Button(self.root,command=self.student_details,image=self.photoimg4,cursor="hand2")
        b1.place(x=150,y=200,width=160,height=160)
       
        b_1=Button(self.root, text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",10,"bold"),bg="darkblue",fg="white")
        b_1.place(x=150,y=360,width=160,height=30)
    
#    detection button 2------------
        img_detection=Image.open(rb"C:\Users\Dell\Desktop\image\college_images\face_detector1.jpg")
        img_detection=img_detection.resize((160,160))
        self.photo_detection=ImageTk.PhotoImage(image=img_detection)
        b_detection=Button(self.root,image=self.photo_detection,cursor="hand2",command=self.face_data)
        b_detection.place(x=450,y=200,width=160,height=160)
       
        b_2=Button(self.root,command=self.face_data, text="Face Detection",cursor="hand2",font=("times new roman",10,"bold"),bg="darkblue",fg="white")
        b_2.place(x=450,y=360,width=160,height=30)
#    attendence button 3------------
        img_attendence=Image.open(rb"C:\Users\Dell\Desktop\image\college_images\report.jpg")
        img_attendence=img_attendence.resize((160,160))
        self.photo_attendence=ImageTk.PhotoImage(image=img_attendence)
        b_attendence=Button(self.root,image=self.photo_attendence,cursor="hand2")
        b_attendence.place(x=750,y=200,width=160,height=160)
       
        b_3=Button(self.root, text="Attendence",cursor="hand2",font=("times new roman",10,"bold"),bg="darkblue",fg="white")
        b_3.place(x=750,y=360,width=160,height=30)
#    helpdesk button 4------------
        img_helpdesk=Image.open(rb"C:\Users\Dell\Desktop\image\college_images\helpdesk1.jpg")
        img_helpdesk=img_helpdesk.resize((160,160))
        self.photo_helpdesk=ImageTk.PhotoImage(image=img_helpdesk)
        b_helpdesk=Button(self.root,image=self.photo_helpdesk,cursor="hand2",command=self.help_data,)
        b_helpdesk.place(x=1050,y=200,width=160,height=160)
       
        b_4=Button(self.root, text="Help Desk",command=self.help_data,cursor="hand2",font=("times new roman",10,"bold"),bg="darkblue",fg="white")
        b_4.place(x=1050,y=360,width=160,height=30)

# #    train_face button 5------------
        img_train_face=Image.open(rb"C:\Users\Dell\Desktop\image\college_images\Train.jpg")
        img_train_face=img_train_face.resize((160,160))
        self.photo_train_face=ImageTk.PhotoImage(image=img_train_face)
        b_train_face=Button(self.root,image=self.photo_train_face,cursor="hand2",command=self.train_data)
        b_train_face.place(x=150,y=450,width=160,height=160)
       
        b_5=Button(self.root, command=self.train_data,text="Train Data",cursor="hand2",font=("times new roman",10,"bold"),bg="darkblue",fg="white")
        b_5.place(x=150,y=610,width=160,height=30)
#    photo_face button 6------------
        img_photo_face=Image.open(rb"C:\Users\Dell\Desktop\image\college_images\photo1.jpg")
        img_photo_face=img_photo_face.resize((160,160))
        self.photo_photo_face=ImageTk.PhotoImage(image=img_photo_face)
        b_photo_face=Button(self.root,image=self.photo_photo_face,cursor="hand2",command=self.open_img)
        b_photo_face.place(x=450,y=450,width=160,height=160)
       
        b_6=Button(self.root, text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",10,"bold"),bg="darkblue",fg="white")
        b_6.place(x=450,y=610,width=160,height=30)
#    developer_face button 7------------
        img_developer_face=Image.open(rb"C:\Users\Dell\Desktop\image\college_images\developer2.jpg")
        img_developer_face=img_developer_face.resize((160,160))
        self.photo_developer_face=ImageTk.PhotoImage(image=img_developer_face)
        b_developer_face=Button(self.root,image=self.photo_developer_face,cursor="hand2",command=self.developer_data)
        b_developer_face.place(x=750,y=450,width=160,height=160)
       
        b_6=Button(self.root, text="Developer",command=self.developer_data,cursor="hand2",font=("times new roman",10,"bold"),bg="darkblue",fg="white")
        b_6.place(x=750,y=610,width=160,height=30)
#    exit button 7------------
        img_exit=Image.open(rb"C:\Users\Dell\Desktop\image\college_images\exit.jpg")
        img_exit=img_exit.resize((160,160))
        self.photo_exit=ImageTk.PhotoImage(image=img_exit)
        b_exit=Button(self.root,image=self.photo_exit,cursor="hand2",command=self.iExit)
        b_exit.place(x=1050,y=450,width=160,height=160)
       
        b_8=Button(self.root, text="Exit",cursor="hand2",command=self.iExit,font=("times new roman",10,"bold"),bg="darkblue",fg="white")
        b_8.place(x=1050,y=610,width=160,height=30)


    def open_img(self):
        os.startfile(r"C:\Users\Dell\Desktop\image\data")


    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Reconginition","Are you sure exit",parent=self.root)
        if self.iExit:
                self.root.destroy()
        else:
                return

   


        # ======Functon buttons ======

    
         
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)


    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Recogniton(self.new_window)

    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)



    

        





 










    


    
if __name__ == "__main__":

        root=Tk()

        obj=face_recongnition_system(root)

        root.mainloop()

