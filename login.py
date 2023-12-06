from tkinter import*
from tkinter  import ttk
from PIL import Image,ImageTk
import PIL
import os
import tkinter
from time import strftime
from datetime import datetime
from tkinter import messagebox 

# def main():
#     win=Tk()
#     app=Login_Window(win)
#     win.mainloop()

class Login_Window:
    def __init__(self,root):
        self.root=root 
        self.root.geometry("1350x780+0+0")
        self.root.title("Developer Details")

        title_labl=Label(self.root,text="Welcome Students !",font=("times new roman",25,"bold"),bg="white",fg="red")
        title_labl.place(x=0,y=0,width=1430,height=35)


        img_top=Image.open(rb"college_images\un.jpg")
        img_top=img_top.resize((1320,620))
        self.photo_img_top = ImageTk.PhotoImage(img_top)
        labell_top=Label(self.root, image=self.photo_img_top)
        labell_top.place(x=8,y=50,width=1320,height=620)

        developer_frame=LabelFrame(self.root,bd=2,bg="black" )
        developer_frame.place(x=530,y=160,width=340,height=430)


        img_left=Image.open(rb"C:\Users\Dell\Desktop\image\college_images\Login.png")
        # self.photoimg1=ImageTk.PhotoImage(img1)
        img_left=img_left.resize((80,80))
        self.img_left1 = ImageTk.PhotoImage(img_left)

        labell_left=Label(developer_frame, image=self.img_left1,bg="black",borderwidth=0)
        labell_left.place(x=125,y=6,width=80,height=80)

      

        get_str=Label(developer_frame,text='Get Started',font=("time new romen",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)

        # label entery box

        login_label=Label(developer_frame,text="Username",font=("times new roman",12,"bold"),fg="white",bg="black")
        login_label.place(x=80,y=165)
        self.user_entery=ttk.Entry(developer_frame,width=28,font=("times new roman",12,"bold"))
        self.user_entery.place(x=50,y=185)

        login_label1=Label(developer_frame,text="Password",font=("times new roman",12,"bold"),fg="white",bg="black")
        login_label1.place(x=80,y=220)
        self.login_entery1=ttk.Entry(developer_frame,width=28,font=("times new roman",12,"bold"))
        self.login_entery1.place(x=50,y=240)
    


    # image icon

        
        img_icon=Image.open(rb"C:\Users\Dell\Desktop\image\college_images\Login.png")
        img_icon=img_left.resize((20,20))
        self.img_icon1 = ImageTk.PhotoImage(img_icon)
        labell_icon=Label(developer_frame, image=self.img_icon1,bg="black",borderwidth=0)
        labell_icon.place(x=60,y=165,width=20,height=20)

        img_icon2=Image.open(rb"C:\Users\Dell\Desktop\image\college_images\lock.png")
        img_icon2=img_left.resize((20,20))
        self.img_icon12 = ImageTk.PhotoImage(img_icon2)
        labell_icon2=Label(developer_frame, image=self.img_icon12,bg="black",borderwidth=0)
        labell_icon2.place(x=60,y=220,width=20,height=20)

        #  login button

        b_1=Button(developer_frame,command=self.login, text="Login",cursor="hand2",font=("times new roman",10,"bold"),relief=RIDGE,bg="red",fg="white",activeforeground="white",activebackground="red")
        b_1.place(x=120,y=290,width=80,height=30)

        b_2=Button(developer_frame, text="New User Ragister",cursor="hand2",font=("times new roman",8,"bold"),relief=RIDGE,bg="red",fg="white",activeforeground="white",activebackground="red")
        b_2.place(x=10,y=340,width=120,height=25)

        b_3=Button(developer_frame, text="Forget password",cursor="hand2",font=("times new roman",8,"bold"),relief=RIDGE,bg="red",fg="white",activeforeground="white",activebackground="red")
        b_3.place(x=10,y=375,width=120,height=25)

    # def login(self):
    #     if self.user_entery.get()==""or self.login_entery1.get()=="":
    #         messagebox.showerror("Error","all field required")
    #     elif self.user_entery.get()=="Abhi" and self.login_entery1.get()=="abhi123":
    #         messagebox.showinfo("success","welcome to user")
    #     else:
    #         messagebox.showerror("invalid","invalid username and password   ")

    def login(self):
        if (self.txtuser.get()=="" or self.txtpwd.get()==""):
            messagebox.showerror("Error","All Field Required!")
        elif(self.txtuser.get()=="admin" and self.txtpwd.get()=="admin"):
            messagebox.showinfo("Sussessfully","Welcome to Attendance Managment System Using Facial Recognition")
        else:
            # messagebox.showerror("Error","Please Check Username or Password !")
            conn = mysql.connector.connect(username='root', password='root',host='localhost',database='face_recognition',port=3307)
            mycursor = conn.cursor()
            mycursor.execute("select * from regteach where email=%s and pwd=%s",(
                self.txtuser.get(),
                self.txtpwd.get()
            ))
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username and Password!")
            else:
                open_min=messagebox.askyesno("YesNo","Access only Admin")
                if open_min>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)
                else:
                    if not open_min:
                        return
            conn.commit()
            conn.close()
#=======================Reset Passowrd Function=============================
    def reset_pass(self):
        if self.var_ssq.get()=="Select":
            messagebox.showerror("Error","Select the Security Question!",parent=self.root2)
        elif(self.var_sa.get()==""):
            messagebox.showerror("Error","Please Enter the Answer!",parent=self.root2)
        elif(self.var_pwd.get()==""):
            messagebox.showerror("Error","Please Enter the New Password!",parent=self.root2)
        else:
            conn = mysql.connector.connect(username='root', password='root',host='localhost',database='face_recognition',port=3307)
            mycursor = conn.cursor()
            query=("select * from regteach where email=%s and ss_que=%s and s_ans=%s")
            value=(self.txtuser.get(),self.var_ssq.get(),self.var_sa.get())
            mycursor.execute(query,value)
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please Enter the Correct Answer!",parent=self.root2)
            else:
                query=("update regteach set pwd=%s where email=%s")
                value=(self.var_pwd.get(),self.txtuser.get())
                mycursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Successfully Your password has been rest, Please login with new Password!",parent=self.root2)
                



# =====================Forget window=========================================
    def forget_pwd(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please Enter the Email ID to reset Password!")
        else:
            conn = mysql.connector.connect(username='root', password='root',host='localhost',database='face_recognition',port=3307)
            mycursor = conn.cursor()
            query=("select * from regteach where email=%s")
            value=(self.txtuser.get(),)
            mycursor.execute(query,value)
            row=mycursor.fetchone()
            # print(row)

            if row==None:
                messagebox.showerror("Error","Please Enter the Valid Email ID!")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("400x400+610+170")
                l=Label(self.root2,text="Forget Password",font=("times new roman",30,"bold"),fg="#002B53",bg="#fff")
                l.place(x=0,y=10,relwidth=1)
                # -------------------fields-------------------
                #label1 
                ssq =lb1= Label(self.root2,text="Select Security Question:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
                ssq.place(x=70,y=80)

                #Combo Box1
                self.combo_security = ttk.Combobox(self.root2,textvariable=self.var_ssq,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security["values"]=("Select","Your Date of Birth","Your Nick Name","Your Favorite Book")
                self.combo_security.current(0)
                self.combo_security.place(x=70,y=110,width=270)


                #label2 
                sa =lb1= Label(self.root2,text="Security Answer:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
                sa.place(x=70,y=150)

                #entry2 
                self.txtpwd=ttk.Entry(self.root2,textvariable=self.var_sa,font=("times new roman",15,"bold"))
                self.txtpwd.place(x=70,y=180,width=270)

                #label2 
                new_pwd =lb1= Label(self.root2,text="New Password:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
                new_pwd.place(x=70,y=220)

                #entry2 
                self.new_pwd=ttk.Entry(self.root2,textvariable=self.var_pwd,font=("times new roman",15,"bold"))
                self.new_pwd.place(x=70,y=250,width=270)

                # Creating Button New Password
                loginbtn=Button(self.root2,command=self.reset_pass,text="Reset Password",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="#002B53",activeforeground="white",activebackground="#007ACC")
                loginbtn.place(x=70,y=300,width=270,height=35)






    


if __name__ == "__main__":

        root=Tk()

        obj=Login_Window(root)

        root.mainloop()



         