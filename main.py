from tkinter import*
from tkinter import ttk
import tkinter 
from PIL import Image,ImageTk
from cv2 import data
from student import Student
import os
from face_recognition import Face_Recognition
from train import Train
from attendance import Attendance

 
class Face_Recognition_System:
  #=================== function button===============
    def Student_details(self):
      self.new_window=Toplevel(self.root)
      self.app=Student(self.new_window)
      self.hide() 


    def iExit(self):
      self.iExit= tkinter.messagebox.askyesno("Face Recognition","Are you sure exit this project",parent=self.root)
      if self.iExit>0:
         self.root.destroy()
      else:
          return      

    def Attendance_details(self):
          self.new_window=Toplevel(self.root)
          self.app=Attendance(self.new_window)
          self.hide()  
          
    def open_img(self):
          os.startfile("data")
    def train_data(self):
          self.new_window=Toplevel(self.root)
          self.app=Train(self.new_window)
    def face_data(self):
          self.new_window=Toplevel(self.root)
          self.app=Face_Recognition(self.new_window)
          
    

 
    def __init__(self,root):
        self.root=root
        self.root.geometry("1000x1000+0+0")
        self.root.title("Student Attendance System")
     
     
        #background image 
        img2=Image.open(r"C:\Users\Manoj\OneDrive\Desktop\python\College_Image\bg.jpg")
        img2= img2.resize((1000,1000),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        bg_lbl=Label(self.root,image=self.photoimg2)
        bg_lbl.place(x=0,y=45,width=1000,height=1000)


      # first Image 
        img=Image.open(r"C:\Users\Manoj\OneDrive\Desktop\python\College_Image\new.jpg")
        img= img.resize((200,100),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=200,height=100)

      # Second Image
        img1=Image.open(r"C:\Users\Manoj\OneDrive\Desktop\python\College_Image\new.jpg")
        img1= img1.resize((200,100),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=200,y=0,width=200,height=100)

   #  third Iamge

        img3=Image.open(r"C:\Users\Manoj\OneDrive\Desktop\python\College_Image\new.jpg")
        img3= img1.resize((200,100),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=400,y=0,width=200,height=100)
        

        # fourth Image
        img4=Image.open(r"C:\Users\Manoj\OneDrive\Desktop\python\College_Image\new.jpg")
        img4= img4.resize((200,100),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        f_lbl=Label(self.root,image=self.photoimg4)
        f_lbl.place(x=600,y=0,width=200,height=100)
        

        # Fifth  Image
        img5=Image.open(r"C:\Users\Manoj\OneDrive\Desktop\python\College_Image\new.jpg")
        img5= img5.resize((200,100),Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        f_lbl=Label(self.root,image=self.photoimg5)
        f_lbl.place(x=800,y=0,width=200,height=100)
        
        # label for  Title 

        title_lbl=Label(bg_lbl,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new  roman",25,"bold"),bg= "White", fg="red")
        title_lbl.place(x=0,y=50, width=1000,height=100)
       
       
        # student Button
        img6=Image.open(r"C:\Users\Manoj\OneDrive\Desktop\python\College_Image\student.jpg")
        img6= img6.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        b1=Button(bg_lbl,command=self.Student_details,image=self.photoimg6,cursor="hand2")
        b1.place(x=100,y=200,width=220,height=220)
        b1_1=Button(bg_lbl,command=self.Student_details,text="Student Details",cursor="hand2",font=("times new  roman",15,"bold"),bg= "darkblue", fg="white")
        b1_1.place(x=100,y=400,width=220,height=40)
        # detect  face
        img7=Image.open(r"C:\Users\Manoj\OneDrive\Desktop\python\College_Image\student.jpg")
        img7= img7.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)
        b2=Button(bg_lbl,command=self.face_data,image=self.photoimg7,cursor="hand2")
        b2.place(x=370,y=200,width=220,height=220)
        b1_2=Button(bg_lbl,command=self.face_data,text="Face Detector",cursor="hand2",font=("times new  roman",15,"bold"),bg= "darkblue", fg="white")
        b1_2.place(x=370,y=400,width=220,height=40)
        
        # attendance
        img8=Image.open(r"C:\Users\Manoj\OneDrive\Desktop\python\College_Image\student.jpg")
        img8= img8.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)
        b3=Button(bg_lbl,command=self.Attendance_details,image=self.photoimg8,cursor="hand2")
        b3.place(x=640,y=200,width=220,height=220)
        b1_3=Button(bg_lbl,command=self.Attendance_details,text="Attendance",cursor="hand2",font=("times new  roman",15,"bold"),bg= "darkblue", fg="white")
        b1_3.place(x=640,y=400,width=220,height=40)
       #  Train face button
        img9=Image.open(r"C:\Users\Manoj\OneDrive\Desktop\python\College_Image\student.jpg")
        img9= img9.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)
        b4=Button(bg_lbl,command=self.train_data,image=self.photoimg9,cursor="hand2")
        b4.place(x=100,y=470,width=220,height=220)
        b1_4=Button(bg_lbl,command=self.train_data,text="Train Data",cursor="hand2",font=("times new  roman",15,"bold"),bg= "darkblue", fg="white")
        b1_4.place(x=100,y=670,width=220,height=40)
         
         #  Photo button
        img10=Image.open(r"C:\Users\Manoj\OneDrive\Desktop\python\College_Image\student.jpg")
        img10= img10.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)
        b5=Button(bg_lbl,command=self.open_img,image=self.photoimg10,cursor="hand2")
        b5.place(x=370,y=470,width=220,height=220)
        b1_5=Button(bg_lbl,command=self.open_img,text=" Show Photos",cursor="hand2",font=("times new  roman",15,"bold"),bg= "darkblue", fg="white")
        b1_5.place(x=370,y=670,width=220,height=40)
    
        #  Exit button
        img11=Image.open(r"C:\Users\Manoj\OneDrive\Desktop\python\College_Image\student.jpg")
        img11= img11.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img10)
        b6=Button(bg_lbl,image=self.photoimg10,cursor="hand2",command=self.iExit)
        b6.place(x=640,y=470,width=220,height=220)
        b1_6=Button(bg_lbl,text=" EXIT",cursor="hand2",command=self.iExit,font=("times new  roman",15,"bold"),bg= "darkblue", fg="white")
        b1_6.place(x=640,y=670,width=220,height=40)



if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
