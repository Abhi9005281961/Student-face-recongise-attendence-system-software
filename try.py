import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import cv2
import mysql.connector
from datetime import datetime

class Recognition:

    def __init__(self, root):
        self.root = root 
        self.root.geometry("1350x780+0+0")
        self.root.title("Face recognition")

        title_label = tk.Label(self.root, text="Face Recognition", font=("times new roman", 25, "bold"), bg="white", fg="red")
        title_label.place(x=0, y=0, width=1430, height=35)

        img_top = Image.open("college_images/face_detector1.jpg")
        img_top = img_top.resize((650, 620))
        self.photo_img_top = ImageTk.PhotoImage(img_top)
        label_top = tk.Label(self.root, image=self.photo_img_top)
        label_top.place(x=10, y=50, width=600, height=620)

        img_top1 = Image.open("college_images/BestFacialRecognition.jpg")
        img_top1 = img_top1.resize((730, 620))
        self.photo_img_top1 = ImageTk.PhotoImage(img_top1)
        label_top1 = tk.Label(self.root, image=self.photo_img_top1)
        label_top1.place(x=600, y=50, width=730, height=620)

        button = tk.Button(self.root, text="Face Recognition", command=self.face_recog, cursor="hand2", font=("times new roman", 18, "bold"), bg="red", fg="white")
        button.place(x=780, y=590, width=210, height=50)

    def mark_attendance(self, i, r, n, d):
        with open("Abhi.csv", "r+", newline="\n") as f:
            mydatalist = f.readlines()
            name_list = []
            for line in mydatalist:
                entry = line.split(",")
                name_list.append(entry[0])
                if (i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list):
                    now = datetime.now()
                    d1 = now.strftime("%d/%M/%m/%Y %H:%M:%S")
                    f.writelines(f"\n{i},{r},{n},{d},{d1},Present")

    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            feature = classifier.detectMultiScale(gray_image, scaleFactor=scaleFactor, minNeighbors=minNeighbors)

            for (x, y, w, h) in feature:
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(host="localhost", username="root", password="Abhi@9889", database="face_recognizer")
                my_cursor = conn.cursor()

                my_cursor.execute("SELECT Name from student1 where student_id=" + str(id))
                n = my_cursor.fetchone()
                n = "+".join(n)

                my_cursor.execute("SELECT Roll from student1 where student_id=" + str(id))
                r = my_cursor.fetchone()
                r = "+".join(r)

                my_cursor.execute("SELECT Dep from student1 where student_id=" + str(id))
                d = my_cursor.fetchone()
                d = "+".join(d)

                if confidence > 77:
                    cv2.putText(img, f"Roll: {r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Name: {n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Department: {d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, f"Unknown face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face_LBPHFaceRecognizer.create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)
        
        while True:
            ret, img = video_cap.read()
            
            # Call the draw_boundary function to perform face recognition
            img = draw_boundary(img, faceCascade, 1.1, 10, (0, 255, 0), "face", clf)
            
            # Display the processed image
            cv2.imshow("Welcome to Face Recognition", img)
            
            if cv2.waitKey(1) == 13:  # Press Enter key to exit
                break

        video_cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = tk.Tk()
    obj = Recognition(root)
    root.mainloop()

