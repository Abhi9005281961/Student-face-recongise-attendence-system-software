from tkinter import*
from tkinter  import ttk
from PIL import Image,ImageTk
import PIL
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:

    def __init__(self,root):
        self.root=root 
        self.root.geometry("1350x780+0+0")
        self.root.title("Face Train ")

        title_labl=Label(self.root,text="Train Data Set",font=("times new roman",25,"bold"),bg="white",fg="red")
        title_labl.place(x=0,y=0,width=1430,height=35)


        img_top=Image.open(rb"college_images\facialrecognition.png")
        img_top=img_top.resize((1350,325))
        self.photo_img_top = ImageTk.PhotoImage(img_top)
        labell_top=Label(self.root, image=self.photo_img_top)
        labell_top.place(x=8,y=50,width=1350,height=290)

        img_bottom=Image.open(rb"college_images\facialrecognition.png")
        img_bottom=img_bottom.resize((1350,325))
        self.photo_img_bottom = ImageTk.PhotoImage(img_bottom)
        labell_bottom=Label(self.root, image=self.photo_img_bottom)
        labell_bottom.place(x=8,y=400,width=1350,height=290)
#  button
        b_6=Button(self.root, text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",20,"bold"),bg="darkblue",fg="white")
        b_6.place(x=8,y=330,width=1350,height=85)      

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') # convert gray scale
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)
        # ===========train the classifire

        clf=cv2.face_LBPHFaceRecognizer.create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        messagebox.showinfo("Result","Training data set completed",parent=top)
        cv2.destroyAllWindows()
        




if __name__ == "__main__":

        root=Tk()

        obj=Train(root)

        root.mainloop()