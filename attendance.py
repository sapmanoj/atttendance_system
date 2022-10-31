from logging import exception
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
from typing import ValuesView
from PIL import Image,ImageTk
from tkinter import messagebox
import sys
import mysql.connector
from mysql.connector import cursor
import cv2
import os 
import csv
from tkinter import filedialog
import datetime


mydate=[]
class Attendance:
    
    # GuI Fynction
    def __init__(self,root):
        self.root=root
        self.root.geometry("1200x1200+0+0")
        self.root.title(" Attendance ")
        #========== variables ==========
        self.var_atten_id=StringVar()
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_department=StringVar()
        self.var_time=StringVar()
        self.var_date=StringVar()
        self.var_Att_Status=StringVar()
        
        
         #background Image
        img4=Image.open(r"C:\Users\Manoj\OneDrive\Desktop\python\College_Image\bg.jpg")
        img4= img4.resize((1200,1200),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_lbl=Label(self.root,image=self.photoimg4)
        bg_lbl.place(x=0,y=45,width=1200,height=1200)


      #first top image
        img=Image.open(r"C:\Users\Manoj\OneDrive\Desktop\python\College_Image\01.jpg")
        img= img.resize((400,200),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=400,height=150)

       # second top image
        img2=Image.open(r"C:\Users\Manoj\OneDrive\Desktop\python\College_Image\02.jpg")
        img2= img2.resize((400,200),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=400,y=0,width=400,height=150)

        #third top  image
        img3=Image.open(r"C:\Users\Manoj\OneDrive\Desktop\python\College_Image\03.jpg")
        img3= img3.resize((400,200),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=800,y=0,width=400,height=150)
        title_lbl=Label(bg_lbl,text="Attendance Management System",font=("times new  roman",30,"bold"),bg= "blue", fg="white")
        title_lbl.place(x=0,y=100, width=1200)
        main_frame=Frame(bg_lbl,bd=2)
        main_frame.place(x=0,y=150,width=1200,height=585)
        Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"),bg= "white", fg="black")
        Left_frame.place(x=10,y=0,width=580,height=580)
        Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"),bg= "white", fg="black")
        Right_frame.place(x=600,y=0,width=580,height=580)
        scroll_x=ttk.Scrollbar(Right_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Right_frame,orient=VERTICAL)  
        self.AttendanceReportTable=ttk.Treeview(Right_frame,column=("AttendanceId","Roll","Name","Deparment","Time","Date","Attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)
        self.AttendanceReportTable.heading("AttendanceId",text="AttendanceId")
        self.AttendanceReportTable.heading("Roll",text="Roll")
        self.AttendanceReportTable.heading("Name",text="Name")
        self.AttendanceReportTable.heading("Deparment",text="Department")
        self.AttendanceReportTable.heading("Time",text="Time")
        self.AttendanceReportTable.heading("Date",text="Date")
        self.AttendanceReportTable.heading("Attendance",text="Attendance")
        self.AttendanceReportTable["show"]="headings"
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
         # left frame  ist image top
        img4=Image.open(r"C:\Users\Manoj\OneDrive\Desktop\python\College_Image\01.jpg")
        img4= img.resize((580,250),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        f_lbl=Label(Left_frame,image=self.photoimg4)
        f_lbl.place(x=0,y=0,width=575,height=250)

        Left_frame2=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"),bg= "white", fg="black")
        Left_frame2.place(x=10,y=260,width=570,height=290)

        # student roll
        student_roll=Label(Left_frame2,text="AttendanceId:",font=("times new roman",12,"bold"),bg="white")
        student_roll.grid(row=0,column=0,padx=2,pady=10,sticky=W)
        student_entry4=ttk.Entry(Left_frame2,textvariable=self.var_atten_id,width=14,font=("times new roman",16,"bold"))
        student_entry4.grid(row=0,column=1,padx=2,pady=10,sticky=W)
         

         #gender
        student_gender=Label(Left_frame2,text="Roll:",font=("times new roman",12,"bold"),bg="white")
        student_gender.grid(row=0,column=2,padx=2,pady=10,sticky=W)
        
        #gender_combo=ttk.Combobox(Left_frame2 e=self.var_gender,text="Gender",font=("times new roman",12,"bold"),width=18,state="readonly")
        #gender_combo["values"]=("Male","Female","other")
        #gender_combo.current()
        #gender_combo.grid(row=2,column=1,padx=2,pady=10,sticky=W)
        gender_entry=ttk.Entry(Left_frame2,textvariable=self.var_roll,width=14,font=("times new roman",14,"bold"))
        gender_entry.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #DOb
        student_gender=Label(Left_frame2,text="Name:",font=("times new roman",12,"bold"),bg="white")
        student_gender.grid(row=1,column=0,padx=2,pady=10,sticky=W)
        student_entry5=ttk.Entry(Left_frame2,textvariable=self.var_name,width=14,font=("times new roman",16,"bold"))
        student_entry5.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #Email
        student_Email=Label(Left_frame2,text="Department:",font=("times new roman",12,"bold"),bg="white")
        student_Email.grid(row=1,column=2,padx=2,pady=10,sticky=W)
        student_entry6=ttk.Entry(Left_frame2,textvariable=self.var_department,width=14,font=("times new roman",14,"bold"))
        student_entry6.grid(row=1,column=3,padx=2,pady=10,sticky=W)


        # Phone

        student_Phone=Label(Left_frame2,text="Time",font=("times new roman",12,"bold"),bg="white")
        student_Phone.grid(row=2,column=0,padx=2,pady=10,sticky=W)
        student_entry7=ttk.Entry(Left_frame2,textvariable=self.var_time,width=14,font=("times new roman",16,"bold"))
        student_entry7.grid(row=2,column=1,padx=2,pady=10,sticky=W)
        
        # address
        student_address=Label(Left_frame2,text="Date:",font=("times new roman",12,"bold"),bg="white")
        student_address.grid(row=2,column=2,padx=2,pady=10,sticky=W)
        student_entry8=ttk.Entry(Left_frame2,textvariable=self.var_date,width=14,font=("times new roman",14,"bold"))
        student_entry8.grid(row=2,column=3,padx=2,pady=10,sticky=W)

        # Teacher name 
        Teacher_name=Label(Left_frame2,text="Attendance Status",font=("times new roman",12,"bold"),bg="white")
        Teacher_name.grid(row=3,column=0,padx=2,pady=10,sticky=W)
        entry=ttk.Entry(Left_frame2,textvariable=self.var_Att_Status,width=14,font=("times new roman",16,"bold"))
        entry.grid(row=3,column=1,padx=2,pady=10,sticky=W) 



        # import
        save_btn=Button(Left_frame2,command=self.importcsv,text="Import csv",width=17,font=("times new roman",10,"bold"),bg="blue",fg="white")
        save_btn.grid(row=4,column=0)
        # export
        update_btn=Button(Left_frame2,command=self.exportcsv,text="Export csv",width=17,font=("times new roman",10,"bold"),bg="blue",fg="white")
        update_btn.grid(row=4,column=1)
        #update
        delete_btn=Button(Left_frame2,text="Update",width=16,font=("times new roman",10,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=4,column=2)
        #Select
        reset_btn=Button(Left_frame2,command=self.resetdata,text="Reset",width=16,font=("times new roman",10,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=4,column=3)
 
 
 #===================fetchdata============
    def fetchdata(self,rows):
          self.AttendanceReportTable.delete(* self.AttendanceReportTable.get_children())
          for i in rows:
                self.AttendanceReportTable.insert("",END,values=i)
                #=====import csv=========
    def importcsv(self):
          global mydate

          mydate.clear()
          fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="open csv",filetypes=(("CSV File","*csv"),("All File","*.*")),parent=self.root)
          with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                  mydate.append(i)
            self.fetchdata(mydate)
    def exportcsv(self):
          try:
            if len(mydate)<1:
                  messagebox.showerror("No data","No Data found to export",parent=self.root)
                  return FALSE
            #fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="open csv",filetypes=(("CSV File","*csv"),("All File","*.*")),parent=self.root)
            timstr=datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

            fln="attendance"+timstr +".csv"
            with open(fln,mode="w+",newline="") as myfile:
              export_wrt=csv.writer(myfile,delimiter=",")
              for i in mydate:
                    export_wrt.writerow(i)
              messagebox.showinfo("Data EXport","your Exported to "+os.path.basename(fln)+"successfully")
          except Exception as es:
                
                  messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
    def get_cursor(self,event=""):
          cursor_row=self.AttendanceReportTable.focus()
          content=self.AttendanceReportTable.item(cursor_row)
          rows=content['values']
          self.var_atten_id.set(rows[0])
          self.var_roll.set(rows[1]) 
          self.var_name.set(rows[2])
          self.var_department.set(rows[3])
          self.var_time.set(rows[4])
          self.var_date.set(rows[5])
          self.var_Att_Status.set(rows[6])
    def resetdata(self):
        self.var_atten_id.set("")
        self.var_roll.set("") 
        self.var_name.set("")
        self.var_department.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_Att_Status.set("")
      

          

         


if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()
 