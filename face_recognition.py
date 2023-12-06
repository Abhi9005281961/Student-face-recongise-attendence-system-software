from sys import path
from tkinter import*
from tkinter  import ttk
from PIL import Image,ImageTk
import PIL
from tkinter import messagebox
import mysql.connector
from time import strftime       
from datetime import datetime
import cv2
import os
import numpy as np

class Recognition:

    def __init__(self,root):
        self.root=root 
        self.root.geometry("1350x780+0+0")
        self.root.title("Face recognition")

        title_labl=Label(self.root,text="Face Recognition",font=("times new roman",25,"bold"),bg="white",fg="red")
        title_labl.place(x=0,y=0,width=1430,height=35)

# image =1 

        img_top=Image.open(rb"college_images\face_detector1.jpg")
        img_top=img_top.resize((650,620))
        self.photo_img_top = ImageTk.PhotoImage(img_top)
        labell_top=Label(self.root, image=self.photo_img_top)
        labell_top.place(x=10,y=50,width=600,height=620)

 # image =2
          
        img_top1=Image.open(rb"college_images\BestFacialRecognition.jpg")
        img_top1=img_top1.resize((730,620))
        self.photo_img_top1 = ImageTk.PhotoImage(img_top1)
        labell_top1=Label(self.root, image=self.photo_img_top1)
        labell_top1.place(x=600,y=50,width=730,height=620)

# button

        b_6=Button( self.root,text="Face Recognition",command=self.face_recog ,cursor="hand2",font=("times new roman",18,"bold"),bg="red",fg="white")
        b_6.place(x=780,y=590,width=210,height=50)


                        

# ========================= face recognition====================================================================================


    def mark_attendance(self,i,r,n):
        with open("attendance.csv","r+",newline="\n") as f:
            myDatalist=f.readlines()
            name_list=[]
            for line in myDatalist:
                entry=line.split((","))
                name_list.append(entry[0])

            if((i not in name_list)) and ((r not in name_list)) and ((n not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i}, {r}, {n}, {dtString}, {d1}, Present")


    #================face recognition==================
    def face_recog(self):

        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            featuers=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]
            
            for (x,y,w,h) in featuers:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])

                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",username="root",password="Abhi@9889",database="face_recognizer",port=3306 )
                my_cursor=conn.cursor()

                my_cursor.execute( "SELECT Name from student1 where student_id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute( "SELECT Roll from student1 where student_id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                my_cursor.execute( "SELECT Dep from student1 where student_id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)

                if confidence > 77:
                        cv2.putText(img,f"Roll{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                        cv2.putText(img,f"Name{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                        cv2.putText(img,f"Department{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                else:
                        cv2.rectangle(img(x,y),(x+y,y+h),(0,0,255),3)
                        cv2.putText(img,f"Unknown face{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                coord=[x,y,w,y]
            
            return coord    


        #==========
        def recognize(img,clf,faceCascade):
                coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
                return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        videoCap=cv2.VideoCapture(0)

        while True:
                ret,img=videoCap.read()
                img=recognize(img,clf,faceCascade)
                cv2.imshow("Face Detector",img)

                if cv2.waitKey(1) == 13:
                        break
        videoCap.release()
        cv2.destroyAllWindows()
#     def face_recog(self):
#         def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
#                 gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#                 feature=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors=minNeighbors)

#                 coord=[]

#                 for (x,y,w,h) in feature:
#                         cv2.rectangle(img(x,y),(x+y,y+h),(0,255,0),3)
#                         id,predict=clf.predict(gray_image[y:y+h,x:x+w])
#                         confidence=int((100*(1-predict/300)))

                        # conn=mysql.connector.connect(host="localhost",username="root",password="Abhi@9889",database="face_recognizer" )
                        # my_cursor=conn.cursor()

                        # my_cursor.execute( "SELECT Name from student1 where student_id="+str(id))
                        # n=my_cursor.fetchone()
                        # n="+".join(n)

                        # my_cursor.execute( "SELECT Roll from student1 where student_id="+str(id))
                        # r=my_cursor.fetchone()
                        # r="+".join(r)

                        # my_cursor.execute( "SELECT Dep from student1 where student_id="+str(id))
                        # d=my_cursor.fetchone()
                        # d="+".join(d)

                        # if confidence > 77:
                        #         cv2.putText(img,f"Roll{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                        #         cv2.putText(img,f"Name{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                        #         cv2.putText(img,f"Department{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                        # else:
                        #         cv2.rectangle(img(x,y),(x+y,y+h),(0,0,255),3)
                        #         cv2.putText(img,f"Unknown face{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                        # coord=[x,y,w,y]

#                 return coord

#         def recognize(img,clf,faceCascade):
#                 coord=draw_boundary(img,faceCascade,1.1,10(255,25,255),"Face",clf)
#                 return img
#         faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#         clf=cv2.face_LBPHFaceRecognizer.create()
#         clf.read("classifier.xml")

#         video_cap=cv2.VideoCapture(0)
#         while True:
#                 ret,img=video_cap.read()
#                 ret, img = video_cap.read()
#                 img=recognize(img,clf,faceCascade)
#                 cv2.imshow("Welcome to Face Recognition",img)
#                 if cv2.waitKey(1)==13:
#                         break

#         video_cap.release()
#         cv2.destroyAllWindows()

        

                        

        # def recognize(img, clf, faceCascade):
        #         img = draw_boundary(img, faceCascade, 1.1, 5, (255, 25, 255), "face", clf)
        #         return img

        # faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        # clf = cv2.face_LBPHFaceRecognizer.create()
        # clf.read("classifier.xml")

        # video_cap = cv2.VideoCapture(0)

        # while True:
        #         ret, img = video_cap.read()
        #         img = recognize(img, clf, faceCascade)
        #         cv2.imshow("Welcome to Face Recognition", img)
        #         if cv2.waitKey(1) == 13:  # Press Enter to exit
        #                 break

        # video_cap.release()
        # cv2.destroyAllWindows()



                



if __name__ == "__main__":

        root=Tk()

        obj=Recognition(root)

        root.mainloop()