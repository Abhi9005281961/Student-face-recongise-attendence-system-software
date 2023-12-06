from tkinter import*

from tkinter  import ttk

from PIL import Image,ImageTk
import PIL
from tkinter import messagebox
import mysql.connector
import cv2

class Student:

    def __init__(self,root):
        self.root=root 
        self.root.geometry("1350x780+0+0")
        self.root.title("Student Details")

        # ======variables =================================

        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()


        img1=Image.open(rb"C:\Users\Dell\Desktop\image\college_images\gettyimages-1022573162.jpg")
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
        img2=Image.open(rb"C:\Users\Dell\Desktop\image\college_images\developer2.jpg")
        img2=img2.resize((500, 130))
        self.img_1 = ImageTk.PhotoImage(img2)
        labell=Label(self.root, image=self.img_1)
        labell.place(x=500,y=0,width=500,height=130)
        # -----------------------------------------------------------------------------------------------------
        img3=Image.open(rb"C:\Users\Dell\Desktop\image\college_images\iStock-1163542789-945x630.jpg")
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
        title_labl=Label(bg_img, text="Student Detail Management system",font=("times new roman",25,"bold"),bg="darkblue",fg="white")
        title_labl.place(x=0,y=0,width=1430,height=35)

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=4,y=46,width=1330,height=520 )

        # left label frame

        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student detail")
        left_frame.place(x=10,y=10,width=650,height=505)

        img_left=Image.open(rb"C:\Users\Dell\Desktop\image\college_images\gettyimages-1022573162.jpg")
        # self.photoimg1=ImageTk.PhotoImage(img1)
        img_left=img_left.resize((630, 120))
        self.img_left1 = ImageTk.PhotoImage(img_left)

        labell_left=Label(left_frame, image=self.img_left1)
        labell_left.place(x=5,y=6,width=630,height=120)

        # curent course information

        left_frame1=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current course information")
        left_frame1.place(x=5,y=110,width=630,height=100)
#  department
        dep_label=Label(left_frame1,text="Department",font=("times new roman",9,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10 )
        dep_combo=ttk.Combobox(left_frame1,textvariable=self.var_dep,font=("times new roman",9),state="readonly",width=15)
        dep_combo["values"]=("select department","computer","IT","civil")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        # course

        course_label=Label(left_frame1,text="Course",font=("times new roman",9,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,pady=10)

        course_combo=ttk.Combobox(left_frame1,textvariable=self.var_course,font=("times new roman",9),state="readonly",width=15)
        course_combo["values"]=("select course","FE","SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        # year

        year_label=Label(left_frame1,text="Year",font=("times new roman",9,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=8,sticky=W)

        year_combo=ttk.Combobox(left_frame1,textvariable=self.var_year,font=("times new roman",9),state="readonly",width=15)
        year_combo["values"]=("select your year","2020-21","2021-22","2022-2023","2023-2024")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #  semester

        semester_label=Label(left_frame1,text="Semester",font=("times new roman",9,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,pady=7 )

        semester_combo=ttk.Combobox(left_frame1,textvariable=self.var_semester,font=("times new roman",9),state="readonly",width=15)
        semester_combo["values"]=("select department","Fisrt year","second year","third year","fourth year")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        # class student information

        left_frame2=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Class student information")
        left_frame2.place(x=5,y=210,width=630,height=270)
#       student id
        StudentId_label=Label(left_frame2,text="StudentId",font=("times new roman",9,"bold"),bg="white")
        StudentId_label.grid(row=0,column=0,padx=10,sticky=W )
  
        student_entery=ttk.Entry(left_frame2,textvariable=self.var_std_id,width=17,font=("times new roman",9,"bold"))
        student_entery.grid(row=0,column=1,padx=6,pady=5,sticky=W)

#       student name

        Student_name_label=Label(left_frame2,text="Student Name",font=("times new roman",9,"bold"),bg="white")
        Student_name_label.grid(row=0,column=2,padx=10,sticky=W )
        student_name_entery=ttk.Entry(left_frame2,textvariable=self.var_std_name,width=17,font=("times new roman",9,"bold"))
        student_name_entery.grid(row=0,column=3,padx=6,pady=5,sticky=W)

        # class division

        student_class_label=Label(left_frame2,text="Student Division",font=("times new roman",9,"bold"),bg="white")
        student_class_label.grid(row=1,column=0,padx=10,sticky=W )
  
        # student_class_entery=ttk.Entry(left_frame2,textvariable=self.var_div,width=17,font=("times new roman",9,"bold"))
        # student_class_entery.grid(row=1,column=1,padx=6,pady=5,sticky=W)

        division_combo=ttk.Combobox(left_frame2,textvariable=self.var_div,font=("times new roman",9),state="readonly",width=14)
        division_combo["values"]=("A","B","C","D","E","F")
        division_combo.current(0)
        division_combo.grid(row=1,column=1,padx=5,pady=6,sticky=W)

        # roll no.ab

        Student_roll_label=Label(left_frame2,text="Student Roll No.",font=("times new roman",9,"bold"),bg="white")
        Student_roll_label.grid(row=1,column=2,padx=10,sticky=W )
  
        student_roll_entery=ttk.Entry(left_frame2,textvariable=self.var_roll,width=17,font=("times new roman",9,"bold"))
        student_roll_entery.grid(row=1,column=3,padx=6,pady=5,sticky=W)

        # Gender

        Student_gender_label=Label(left_frame2,text="Gender",font=("times new roman",9,"bold"),bg="white")
        Student_gender_label.grid(row=2,column=0,padx=10,sticky=W )
  
        # gender_entery=ttk.Entry(left_frame2,textvariable=self.var_gender,width=17,font=("times new roman",9,"bold"))
        # gender_entery.grid(row=2,column=1,padx=6,pady=5,sticky=W)

        gender_combo=ttk.Combobox(left_frame2,textvariable=self.var_gender,font=("times new roman",9),state="readonly",width=14)
        gender_combo["values"]=("Male","Female","other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=6,pady=5,sticky=W)

        # date of birth
        birth_label=Label(left_frame2,text="Date OF Birth",font=("times new roman",9,"bold"),bg="white")
        birth_label.grid(row=2,column=2,padx=10,sticky=W )
  
        birth_entery=ttk.Entry(left_frame2,textvariable=self.var_dob,width=17,font=("times new roman",9,"bold"))
        birth_entery.grid(row=2,column=3,padx=6,pady=5,sticky=W)

        # Email
        Email_label=Label(left_frame2,text=" Email ID",font=("times new roman",9,"bold"),bg="white")
        Email_label.grid(row=3,column=0,padx=10,sticky=W )
  
        Email_entery=ttk.Entry(left_frame2,textvariable=self.var_email,width=17,font=("times new roman",9,"bold"))
        Email_entery.grid(row=3,column=1,padx=6,pady=5,sticky=W)

        # phone number

        phone_label=Label(left_frame2,text="Phone Number",font=("times new roman",9,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,sticky=W )
  
        phone_entery=ttk.Entry(left_frame2,textvariable=self.var_phone,width=17,font=("times new roman",9,"bold"))
        phone_entery.grid(row=3,column=3,padx=6,pady=5,sticky=W)

        # address

        address_label=Label(left_frame2,text="Address :",font=("times new roman",9,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,sticky=W )
  
        address_entery=ttk.Entry(left_frame2,textvariable=self.var_address,width=17,font=("times new roman",9,"bold"))
        address_entery.grid(row=4,column=1,padx=6,pady=5,sticky=W)
        #
        # Teacher name

        teacher_label=Label(left_frame2,text="Teacher Name :",font=("times new roman",9,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,sticky=W )
  
        teacher_entery=ttk.Entry(left_frame2,textvariable=self.var_teacher,width=17,font=("times new roman",9,"bold"))
        teacher_entery.grid(row=4,column=3,padx=6,pady=5,sticky=W)

        # radio button

        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(left_frame2,variable=self.var_radio1,text="Take Photo sample",value="Yes")
        radiobtn1.grid(row=5,column=0,padx=10,pady=5)

        # 
        radiobtn2=ttk.Radiobutton(left_frame2,variable=self.var_radio1,text="No Photo sample",value="No")
        radiobtn2.grid(row=5,column=1,padx=10,pady=5)

        #  button frame

        
        btn_frame=Frame(left_frame2,bd=2,relief=RIDGE)
        btn_frame.place(x=5,y=190,width=615,height=55)

        save_btn=Button(btn_frame,width=21,text="Save",command=self.add_data,font=("times new roman",10,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,width=20,text="Update",command=self.update_data,font=("times new roman",10,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,width=21,text="Delete",command=self.delete_data,font=("times new roman",10,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,width=20,text="Reset",command=self.reset_data,font=("times new roman",10,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        btn_frame2=Frame(left_frame2,bd=2,relief=RIDGE)
        btn_frame2.place(x=5,y=220,width=615,height=25)



        photo_btn=Button(btn_frame2,width=45,command=self.generate_dataset,text="Take Photo Sample",font=("times new roman",10,"bold"),bg="blue",fg="white")
        photo_btn.grid(row=1,column=0)

        update_btn=Button(btn_frame2,width=45,text="Update Photo",font=("times new roman",10,"bold"),bg="blue",fg="white")
        update_btn.grid(row=1,column=1)

         

        # right label frame

        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student detail")
        right_frame.place(x=670,y=10,width=650,height=510)

        img_right=Image.open(rb"C:\Users\Dell\Desktop\image\college_images\gettyimages-1022573162.jpg")
        # self.photoimg1=ImageTk.PhotoImage(img1)
        img_right=img_right.resize((630, 120))
        self.img_right1 = ImageTk.PhotoImage(img_right)

        labell_right=Label(right_frame, image=self.img_right1)
        labell_right.place(x=5,y=6,width=630,height=105)

        # =======seaching system=======

        search_frame2=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Class student information")
        search_frame2.place(x=5,y=115,width=630,height=60)

        search_label=Label(search_frame2,text="Search By :",font=("times new roman",10,"bold"),bg="white",fg="blue")
        search_label.grid(row=0,column=0,padx=5,sticky=W )

        search_combo=ttk.Combobox(search_frame2,font=("times new roman",10),state="readonly",width=15)
        search_combo["values"]=("select Roll No.","Phone No." )
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        # entry fill

        entry1_entery=ttk.Entry(search_frame2,width=18,font=("times new roman",9,"bold"))
        entry1_entery.grid(row=0,column=3,padx=6,pady=5,sticky=W)

        # button add

        search_btn=Button(search_frame2,width=21,text="Search ",font=("times new roman",10,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=4)

        show_btn=Button(search_frame2,width=20,text="Show all ",font=("times new roman",10,"bold"),bg="blue",fg="white")
        show_btn.grid(row=0,column=5)

        table_frame2=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame2.place(x=5,y=180,width=630,height=295)

        scroll_x=ttk.Scrollbar(table_frame2,orient=HORIZONTAL )
        scroll_y=ttk.Scrollbar(table_frame2,orient=VERTICAL )

        self.student_table=ttk.Treeview(table_frame2,column=("dep","course","year","sem","id","name","div","roll","dob","email","gender","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="Student ID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll No.")
        self.student_table.heading("dob",text="Date Of Birth")
        self.student_table.heading("email",text="Email ID")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("phone",text="Phone No.")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="Photo sample status")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=100)
        


        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()  
#   =========fuction decleration============
  
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_dep.get()==""or self.var_std_id.get()=="":
                messagebox.showerror("Error","All Field Are Required",parent=self.root)
        else:
                try:
                        conn=mysql.connector.connect(host="localhost",username="root",password="Abhi@9889",database="face_recognizer" )
                        my_cursor=conn.cursor()
                        my_cursor.execute("insert into student1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                
                                                                                                                        self.var_dep.get(),
                                                                                                                        self.var_course.get(),
                                                                                                                        self.var_year.get(),
                                                                                                                        self.var_semester.get(),
                                                                                                                        self.var_std_id.get(),
                                                                                                                        self.var_std_name.get(),
                                                                                                                        self.var_div.get(),
                                                                                                                        self.var_roll.get(),
                                                                                                                        self.var_gender.get(),
                                                                                                                        self.var_dob.get(),
                                                                                                                        self.var_email.get(),
                                                                                                                        self.var_phone.get(),
                                                                                                                        self.var_address.get(),
                                                                                                                        self.var_teacher.get(),
                                                                                                                        self.var_radio1.get()

                                                                                                                ))
                        conn.commit()
                        self.fetch_data()
                        conn.close()
                        messagebox.showinfo("successfully","student details successfully added",parent=self.root)
                except Exception as es:
                        messagebox.showinfo("Error",f"due to:{str(es)}",parent=self.root)


                        # ===fetch data====

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Abhi@9889",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student1")
        data=my_cursor.fetchall()

        if len(data)!= 0:
                self.student_table.delete(*self.student_table.get_children())
                for i in data :
                        self.student_table.insert("",END,values=i)
                conn.commit()
        conn.close()

        #   get cursor===================

    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])


        # =====Update function====

#     def update_data(self):
#         if self.var_dep.get()=="Select Department" or self.var_dep.get()==""or self.var_std_id.get()=="":
#                 messagebox.showerror("Error","All Field Are Required",parent=self.root)
#         else:
#                 try:
#                         Update=messagebox.askyesno("update","Do you want to update this student details?",parent=self.root)
#                         if Update:
#                                 conn=mysql.connector.connect(host="localhost",username="root",password="Abhi@9889",database="face_recognizer" )
#                                 my_cursor=conn.cursor()
#                                 my_cursor.execute( "UPDATE student1 SET Dep=%s,course=%s,Year=%s,Semester=%s,Student id=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,Photo_Sample=%s where Student_id=%s",(
#                                                                                                                                                                                                                         self.var_std_id.get(), 
#                                                                                                                                                                                                                         self.var_course.get(),
#                                                                                                                                                                                                                         self.var_year.get(),
#                                                                                                                                                                                                                         self.var_semester.get(),
#                                                                                                                                                                                                                         self.var_std_name.get(),
#                                                                                                                                                                                                                         self.var_div.get(),
#                                                                                                                                                                                                                         self.var_roll.get(),
#                                                                                                                                                                                                                         self.var_gender.get(),
#                                                                                                                                                                                                                         self.var_dob.get(),
#                                                                                                                                                                                                                         self.var_email.get(),
#                                                                                                                                                                                                                         self.var_phone.get(),
#                                                                                                                                                                                                                         self.var_address.get(),
#                                                                                                                                                                                                                         self.var_teacher.get(),
#                                                                                                                                                                                                                         self.var_radio1.get(),   
                                                                                                                                                                                                                                                                                                                                                                                                          
#                                                                                                                                                                                                                 ))
#                         conn.commit()
#                         self.fetch_data()
#                         conn.close()
#                         messagebox.showinfo("success","Student details successfully updated",parent=self.root)
#                 except Exception as es:
#                         messagebox.showinfo("error",f"Due to:{str(es)}",parent=self.root)


    def update_data(self):
        if ( self.var_dep.get() == "Select Department"or self.var_dep.get() == ""  or self.var_std_id.get() == "" ):
                          messagebox.showerror("Error", "All Fields Are Required", parent=self.root)
        else:
                try:
                        Update = messagebox.askyesno("Update", "Do you want to update this student's details?", parent=self.root)
                        if Update:
                                conn = mysql.connector.connect(
                                host="localhost",
                                username="root",
                                password="Abhi@9889",
                                database="face_recognizer",)
                                my_cursor = conn.cursor()

                        # Correct the column names and placeholders
                                sql = ("UPDATE student1 SET Dep=%s, course=%s, Year=%s, Semester=%s, Name=%s, Division=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, Photo_Sample=%s  WHERE Student_id=%s" )

                        # Make sure the parameters match the placeholders in the same order
                                values = (
                                
                                self.var_dep.get(),
                                self.var_course.get(),
                                self.var_year.get(),
                                self.var_semester.get(),
                                self.var_std_name.get(),
                                self.var_div.get(),
                                self.var_roll.get(),
                                self.var_gender.get(),
                                self.var_dob.get(),
                                self.var_email.get(),
                                self.var_phone.get(),
                                self.var_address.get(),
                                self.var_teacher.get(),
                                self.var_radio1.get(),
                                self.var_std_id.get()
                                )

                                my_cursor.execute(sql, values)
                                conn.commit()
                                conn.close()
                                self.fetch_data()
                                messagebox.showinfo("Success", "Student details successfully updated",parent=self.root)
                        else:
                                if not Update:
                                        return
                except Exception as es:
                        messagebox.showinfo("Error", f"Due to: {str(es)}", parent=self.root)



#     ====delete function====
    def delete_data(self):
        if self.var_std_id.get()=="":
                messagebox.showerror("Error","Student_id must be required",parent=self.root)
        else:
                try:
                        delete=messagebox.askyesno("Student delete page","do you want delete this student",parent=self.root)
                        if delete>0:
                                conn=mysql.connector.connect(host="localhost",username="root",password="Abhi@9889",database="face_recognizer" )
                                my_cursor=conn.cursor()
                                sql="DELETE FROM student1 WHERE Student_id=%s"
                                val=(self.var_std_id.get(),)
                                my_cursor.execute(sql,val)
                        else:
                                if not delete:
                                        return
                        conn.commit()
                        self.fetch_data()
                        conn.close()
                        messagebox.showinfo("Delete","Student deleted successfully",parent=self.root)  
                        

                except Exception as es:
                        messagebox.showinfo("error",f"Due to:{str(es)}",parent=self.root)


#   reset=====

    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")


#==============Generate data set or take photo sample============

    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_dep.get()==""or self.var_std_id.get()=="":
                messagebox.showerror("Error","All Field Are Required",parent=self.root)
        else:
                try:
                        conn=mysql.connector.connect(host="localhost",username="root",password="Abhi@9889",database="face_recognizer" )
                        my_cursor=conn.cursor()
                        my_cursor.execute("select * from student1")
                        my_result=my_cursor.fetchall()
                        id=0
                        for x in my_result :
                                id=id+1
                        sql = ("UPDATE student1 SET Dep=%s, course=%s, Year=%s, Semester=%s, Name=%s, Division=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, Photo_Sample=%s  WHERE Student_id=%s" )

                        values = (
                                
                                self.var_dep.get(),
                                self.var_course.get(),
                                self.var_year.get(),
                                self.var_semester.get(),
                                self.var_std_name.get(),
                                self.var_div.get(),
                                self.var_roll.get(),
                                self.var_gender.get(),
                                self.var_dob.get(),
                                self.var_email.get(),
                                self.var_phone.get(),
                                self.var_address.get(),
                                self.var_teacher.get(),
                                self.var_radio1.get(),
                                self.var_std_id.get()==id+1
                                )     
                                                                                                                                                                                                                        
                        my_cursor.execute(sql, values)
                        conn.commit()
                        self.fetch_data()
                        self.reset_data()
                        conn.close()
                        # ==========Load predefined data on face

                        face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                        def face_cropped(img):
                                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                                faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                        # scaling factor = 1.3 minimum neighbor = 5

                                for (x, y, w, h) in faces:
                                        face_cropped = img[y:y+h, x:x+w]
                                        return face_cropped

                        cap = cv2.VideoCapture(0)
                        img_id = 0

                        while True:
                                ret, my_Frame = cap.read()
                                cropped_face = face_cropped(my_Frame)  # Call the function only once

                                if cropped_face is not None:
                                        img_id += 1
                                        face = cv2.resize(cropped_face, (450, 450))
                                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                                        file_name_path = "data/user." + str(img_id) + ".jpg"
                                        cv2.imwrite(file_name_path, face)
                                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                                        cv2.imshow("cropped face", face)

                                        if cv2.waitKey(1) == 13 or int(img_id) == 100:
                                                break

                        cap.release()
                        cv2.destroyAllWindows()
                        messagebox.showinfo("result", "Generating data sets completed!!!")

                #         face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                #         def face_cropped(img):
                #                 gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                #                 faces=face_classifier.detectMultiScale(gray,1.3,5)
                #                 #  scaling factor =1.3 minimum neibhor=5

                #                 for (x,y,w,h) in faces:
                #                         face_cropped=img[y:y+h,x:x+w]
                #                         return face_cropped
                #         cap=cv2.VideoCapture(0)
                #         img_id=0
                #         while True:
                #                 ret,my_Frame=cap.read()
                #                 if face_cropped(my_Frame)is not None:
                #                         img_id+=1
                #                         face=cv2.resize(face_cropped(my_Frame),(450,450))
                #                         face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                #                         file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                #                         cv2.imwrite(file_name_path,face)
                #                         cv2.putText(face,str(img_id),(50,50), cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                #                         cv2.imshow("cropped face",face)

                #                 if cv2.waitKey(1)==13 or int(img_id)==100:
                #                         break
                #         cap.release()
                #         cv2.destroyAllWindows()
                #         messagebox.showinfo("result","Generating data sets compeleted!!!")

                except Exception as es:
                        messagebox.showinfo("error",f"Due to:{str(es)}",parent=self.root)       
                        



          



if __name__ == "__main__":

        root=Tk()

        obj=Student(root)

        root.mainloop()
