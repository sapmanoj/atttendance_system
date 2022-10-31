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



class Student:
    
    # GuI Fynction
    def __init__(self,root):
        self.root=root
        self.root.geometry("1200x1200+0+0")
        self.root.title("Student Attendance System")
        #+++====++++=++++==========================
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_Std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.Dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        self.var_radio1=StringVar()
        self.var_radio2=StringVar()
        self.var_search_by=StringVar()
        self.var_search_value=StringVar()
        

        #background Image
        img4=Image.open(r"C:\Users\Manoj\OneDrive\Desktop\python\College_Image\bg.jpg")
        img4= img4.resize((1200,1200),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_lbl=Label(self.root,image=self.photoimg4)
        bg_lbl.place(x=0,y=45,width=1200,height=1200)


      #first top iamge
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
        # title label
        title_lbl=Label(bg_lbl,text="Student Management System",font=("times new  roman",30,"bold"),bg= "blue", fg="white")
        title_lbl.place(x=0,y=100, width=1200)
        # frame
        main_frame=Frame(bg_lbl,bd=2)
        main_frame.place(x=0,y=150,width=1200,height=585)

         # left label frame
        Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"),bg= "white", fg="black")
        Left_frame.place(x=10,y=0,width=580,height=580)

         

         # left frame  ist image top
        img4=Image.open(r"C:\Users\Manoj\OneDrive\Desktop\python\College_Image\01.jpg")
        img4= img.resize((580,200),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        f_lbl=Label(Left_frame,image=self.photoimg4)
        f_lbl.place(x=0,y=0,width=575,height=100)
         
         # frame  for Current Course Information
        Left_frame1=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"),bg= "white", fg="black")
        Left_frame1.place(x=2,y=100,width=575,height=125)
        
        #--department
        dep_label=Label(Left_frame1,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=2,pady=10,sticky=W)
        #dep_combo=ttk.Entry(Left_frame1,textvariable=self.var_dep,text="Department",font=("times new roman",12,"bold"),width=18)
        #dep_combo["values"]=("Select Department","computer","Civil","IT","Software")
        #dep_combo.current()
        depart_entry=ttk.Entry(Left_frame1,textvariable=self.var_dep,width=14,font=("times new roman",12,"bold"))
        depart_entry.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        #Course
        course_label=Label(Left_frame1,text="Course",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=2,pady=10,sticky=W)
        
        #course_combo=ttk.Combobox(Left_frame1,textvariable=self.var_course,text="Course",font=("times new roman",12,"bold"),width=18,state="readonly")
        #["values"]=("Select cource","math","Ct","oosm","pst")
        #course_combo.current()
        #course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)
        course_entry=ttk.Entry(Left_frame1,textvariable=self.var_course,width=14,font=("times new roman",12,"bold"))
        course_entry.grid(row=0,column=3,padx=2,pady=10,sticky=W)
        
        # year
        year_label=Label(Left_frame1,text="year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=2,pady=10,sticky=W)
        #year_combo=ttk.Combobox(Left_frame1,textvariable=self.var_year,text="year",font=("times new roman",12,"bold"),width=18,state="readonly")
       # year_combo["values"]=("Select year","2017-2022","2018-2023","2019-2024","2020-2024")
        #year_combo.current()
        
        year_entry=ttk.Entry(Left_frame1,textvariable=self.var_year,width=14,font=("times new roman",12,"bold"))
        year_entry.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        
        # Semester
        sem_label=Label(Left_frame1,text="Semester",font=("times new roman",12,"bold"),bg="white")
        sem_label.grid(row=1,column=2,padx=2,pady=10,sticky=W)
        #sem_combo=ttk.Combobox(Left_frame1,textvariable=self.var_semester,text="Semester`",font=("times new roman",12,"bold"),width=18,state="readonly")
        #sem_combo["values"]=("Select semester","1","2","3","4","5","6","7","8")
        #sem_combo.current()
        sem_entry=ttk.Entry(Left_frame1,textvariable=self.var_semester,width=14,font=("times new roman",12,"bold"))
       
        sem_entry.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #Class  student  Information
        Left_frame2=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"),bg= "white", fg="black")
        Left_frame2.place(x=2,y=225,width=575,height=350)


        # Student Id
        student_id=Label(Left_frame2,text="StudentID:",font=("times new roman",12,"bold"),bg="white")
        student_id.grid(row=0,column=0,padx=2,pady=10,sticky=W)
        student_entry1=ttk.Entry(Left_frame2,textvariable=self.var_std_id,width=14,font=("times new roman",12,"bold"))
        student_entry1.grid(row=0,column=1,padx=2,pady=10,sticky=W)


        # Student name
        student_name=Label(Left_frame2,text="Student Name:",font=("times new roman",12,"bold"),bg="white")
        student_name.grid(row=0,column=2,padx=2,pady=10,sticky=W)
        student_entry2=ttk.Entry(Left_frame2,textvariable=self.var_Std_name,width=14,font=("times new roman",12,"bold"))
        student_entry2.grid(row=0,column=3,padx=2,pady=10,sticky=W)
       
        # student division
        student_division=Label(Left_frame2,text="Class Division:",font=("times new roman",12,"bold"),bg="white")
        student_division.grid(row=1,column=0,padx=2,pady=10,sticky=W)
        
        #div_combo=ttk.Combobox(Left_frame2,textvariable=self.var_div,state="readonly",text="Div`",font=("times new roman",12,"bold"),width=18,)
        #div_combo["values"]=("A","B","C")
        #div_combo.current()
        div_entry=ttk.Entry(Left_frame2,textvariable=self.var_div,width=14,font=("times new roman",12,"bold"))
        
        div_entry.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        
        # student roll
        student_roll=Label(Left_frame2,text="Class Roll:",font=("times new roman",12,"bold"),bg="white")
        student_roll.grid(row=1,column=2,padx=2,pady=10,sticky=W)
        student_entry4=ttk.Entry(Left_frame2,textvariable=self.var_roll,width=14,font=("times new roman",12,"bold"))
        student_entry4.grid(row=1,column=3,padx=2,pady=10,sticky=W)
         

         #gender
        student_gender=Label(Left_frame2,text="Gender:",font=("times new roman",12,"bold"),bg="white")
        student_gender.grid(row=2,column=0,padx=2,pady=10,sticky=W)
        
        #gender_combo=ttk.Combobox(Left_frame2,textvariable=self.var_gender,text="Gender",font=("times new roman",12,"bold"),width=18,state="readonly")
        #gender_combo["values"]=("Male","Female","other")
        #gender_combo.current()
        #gender_combo.grid(row=2,column=1,padx=2,pady=10,sticky=W)
        gender_entry=ttk.Entry(Left_frame2,textvariable=self.var_gender,width=14,font=("times new roman",12,"bold"))
        gender_entry.grid(row=2,column=1,padx=2,pady=10,sticky=W)

        #DOb
        student_gender=Label(Left_frame2,text="DOB:",font=("times new roman",12,"bold"),bg="white")
        student_gender.grid(row=2,column=2,padx=2,pady=10,sticky=W)
        student_entry5=ttk.Entry(Left_frame2,textvariable=self.Dob,width=14,font=("times new roman",12,"bold"))
        student_entry5.grid(row=2,column=3,padx=2,pady=10,sticky=W)

        #Email
        student_Email=Label(Left_frame2,text="Email:",font=("times new roman",12,"bold"),bg="white")
        student_Email.grid(row=3,column=0,padx=2,pady=10,sticky=W)
        student_entry6=ttk.Entry(Left_frame2,textvariable=self.var_email,width=14,font=("times new roman",12,"bold"))
        student_entry6.grid(row=3,column=1,padx=2,pady=10,sticky=W)


        # Phone

        student_Phone=Label(Left_frame2,text="Phone:",font=("times new roman",12,"bold"),bg="white")
        student_Phone.grid(row=3,column=2,padx=2,pady=10,sticky=W)
        student_entry7=ttk.Entry(Left_frame2,textvariable=self.var_phone,width=14,font=("times new roman",12,"bold"))
        student_entry7.grid(row=3,column=3,padx=2,pady=10,sticky=W)
        
        # address
        student_address=Label(Left_frame2,text="Address:",font=("times new roman",12,"bold"),bg="white")
        student_address.grid(row=4,column=0,padx=2,pady=10,sticky=W)
        student_entry8=ttk.Entry(Left_frame2,textvariable=self.var_address,width=14,font=("times new roman",12,"bold"))
        student_entry8.grid(row=4,column=1,padx=2,pady=10,sticky=W)

        # Teacher name 
        Teacher_name=Label(Left_frame2,text="Teacher:",font=("times new roman",12,"bold"),bg="white")
        Teacher_name.grid(row=4,column=2,padx=2,pady=10,sticky=W)
        entry=ttk.Entry(Left_frame2,textvariable=self.var_teacher,width=14,font=("times new roman",12,"bold"))
        entry.grid(row=4,column=3,padx=2,pady=10,sticky=W) 


        #photo radio button

        Radiobutton1=ttk.Radiobutton(Left_frame2,variable=self.var_radio1,text="Take a photo Sample",value="yes")
        Radiobutton1.grid(row=5,column=0,padx=2,pady=10,sticky=W)
        Radiobutton2=ttk.Radiobutton(Left_frame2,variable=self.var_radio1,text="No Photo Sample",value="No")
        Radiobutton2.grid(row=5,column=1,padx=2,pady=10,sticky=W)

        #button frame
        btn_frame=Frame(Left_frame2,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=260,width=572,height=60)


        # save button
        save_btn=Button(btn_frame,command=self.Add_data,text="Save",width=19,font=("times new roman",10,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)
        # update
        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=19,font=("times new roman",10,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)
        #delete
        delete_btn=Button(btn_frame,command=self.delete_data,text="Delete",width=18,font=("times new roman",10,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)
        #Select
        reset_btn=Button(btn_frame,command=self.reset_data,text="Reset",width=19,font=("times new roman",10,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        #take  a Photo sample
        takephoto_btn=Button(btn_frame,command=self.generate_dataset,text="Take  photo sample",width=15,font=("times new roman",10,"bold"),bg="blue",fg="white")
        takephoto_btn.grid(row=1,column=1)
        #update photo sample
        updatephoto_btn=Button(btn_frame,text="Update photo sample",width=15,font=("times new roman",10,"bold"),bg="blue",fg="white")
        updatephoto_btn.grid(row=1,column=2)
        # Right label frame
        right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"),bg= "white", fg="black")
        right_frame.place(x=600,y=0,width=580,height=575)

         #Right image
        img5=Image.open(r"C:\Users\Manoj\OneDrive\Desktop\python\College_Image\01.jpg")
        img5= img.resize((580,200),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        f_lbl=Label(right_frame,image=self.photoimg4)
        f_lbl.place(x=0,y=0,width=575,height=100)

        # search system 
        search_frame2=LabelFrame(right_frame,bd=2,relief=RIDGE,text="Search System",font=("times new roman",12,"bold"),bg= "white", fg="black")
        search_frame2.place(x=2,y=100,width=575,height=70)
         #search by
        search_label=Label(search_frame2,text="Search by:",font=("times new roman",15,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=2,pady=10,sticky=W)
        search_combo=ttk.Combobox(search_frame2,text="Semester`",textvariable=self.var_search_by,font=("times new roman",12,"bold"),width=10,state="read only")
        search_combo["values"]=("Select","Roll","Phone")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        # entry field
        Search_entry=ttk.Entry(search_frame2,textvariable=self.var_search_value,width=24,font=("times new roman",12,"bold"))
        Search_entry.grid(row=0,column=2,padx=2,pady=10,sticky=W) 

        # search button
        Search_btn=Button(search_frame2,command=self.searchby,text="Search",width=10,font=("times new roman",10,"bold"),bg="blue",fg="white")
        Search_btn.grid(row=0,column=3)

        #show all
        ShowAll_btn=Button(search_frame2,text="Show all", width=10,font=("times new roman",10,"bold"),bg="blue",fg="white")
        ShowAll_btn.grid(row=0,column=4,padx=2,pady=10,sticky=W)
       
       # table frame

        Table_frame2=LabelFrame(right_frame,bd=2,relief=RIDGE)
        Table_frame2.place(x=2,y=170,width=575,height=380)

        #scroll bar
        scroll_x=ttk.Scrollbar(Table_frame2,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_frame2,orient=VERTICAL)  
        self.student_table=ttk.Treeview(Table_frame2,column=("department","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading("department",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="ClassRoll")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Adress")
        self.student_table.heading("teacher",text="teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table.heading("gender",text="Gender")
       
        self.student_table["show"]="headings"
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
    #========= function ============
    def Add_data(self):
           if self.var_dep.get()=="Select Department" or self.var_Std_name.get()=="" or self.var_std_id.get()=="":
                messagebox.showerror("Error","All Fields are Rquired",parent=self.root)   
           else:
              try:

                 conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognizer")
                 mycursor=conn.cursor()
                 mycursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                    self.var_dep.get(),
                                                                                                                    self.var_course.get(),
                                                                                                                    self.var_year.get(),
                                                                                                                    self.var_semester.get(),
                                                                                                                    self.var_std_id.get(),
                                                                                                                    self.var_Std_name.get(),
                                                                                                                    self.var_div.get(),
                                                                                                                    self.var_roll.get(),
                                                                                                                    self.var_gender.get(),
                                                                                                                    self.Dob.get(),
                                                                                                                    self.var_email.get(),
                                                                                                                    self.var_phone.get(),
                                                                                                                    self.var_address.get(),
                                                                                                                    self.var_teacher.get(),
                                                                                                                    self.var_radio1.get()
                                                                                                                  ))
                 conn.commit() 
                 self.fetch_data()  
                 conn.close()                                                                                               
                 messagebox.showinfo("sucess","Student details has been added sucessfully",parent=self.root)     
            
              except Exception as es:
                
                  messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
    
    def fetch_data(self):
          conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognizer")
          mycursor=conn.cursor()
          mycursor.execute("select * from student")
          data=mycursor.fetchall()

          if len(data)!=0:
                self.student_table.delete(*self.student_table.get_children())
                for i in data:
                      self.student_table.insert("",END,values=i)
                conn.commit()
          conn.close()
    def get_cursor(self,event=""):
          cursor_focus=self.student_table.focus()
          content=self.student_table.item(cursor_focus)
          data=content["values"]
          self.var_dep.set(data[0]),
          self.var_course.set(data[1]),
          self.var_year.set(data[2]),
          self.var_semester.set(data[3]),
          self.var_std_id.set(data[4]),
          self.var_Std_name.set(data[5]),
          self.var_div.set(data[6]),
          self.var_roll.set(data[7]),
          self.var_gender.set(data[8]),
          self.Dob.set(data[9]),
          self.var_email.set(data[10]),
          self.var_phone.set(data[11])
          self.var_address.set(data[12])
          self.var_teacher.set(data[13])
          self.var_radio1.set(data[14])
       #update function
    def update_data(self):
          if self.var_dep.get()=="Select Department" or self.var_Std_name.get()=="" or self.var_std_id.get()=="":
              messagebox.showerror("Error","All Fields are Rquired",parent=self.root)   
          
          else:
                try:
                      update=messagebox.askyesno("Upadte","Do you want to update this student details",parent=self.root)
                      if update>0:
                            conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognizer")
                            mycursor=conn.cursor()
                            mycursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s ",(
                                                                                                                    self.var_dep.get(),
                                                                                                                    self.var_course.get(),
                                                                                                                    self.var_year.get(),
                                                                                                                    self.var_semester.get(),
                                                                                                                   
                                                                                                                    self.var_Std_name.get(),
                                                                                                                    self.var_div.get(),
                                                                                                                    self.var_roll.get(),
                                                                                                                    self.var_gender.get(),
                                                                                                                    self.Dob.get(),
                                                                                                                    self.var_email.get(),
                                                                                                                    self.var_phone.get(),
                                                                                                                    self.var_address.get(),
                                                                                                                    self.var_teacher.get(),
                                                                                                                    self.var_radio1.get(),
                                                                                                                    self.var_std_id.get()
                                                                                                                                          ))
                      else: 
                            if not update:
                                  return
                      
                      messagebox.showinfo("Sucess","Student details Successfully upadte completed",parent=self.root)
                      conn.commit()
                      self.fetch_data()
                      conn.close()
                except Exception as es: 
                      messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    def delete_data(self):
          if self.var_std_id.get()=="":
                messagebox.showerror("Error","student id must be required",parent=self.root)
          else:
                try:
                      delete=messagebox.askyesno("student delete page","Do you  want to delete this student",parent=self.root)
                      if delete>0:
                            conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognizer")
                            mycursor=conn.cursor()
                            sql="delete from student where Student_id=%s"
                            val=(self.var_std_id.get(),)
                            mycursor.execute(sql,val)
                      else:   
                            if not delete:
                                  return
                      conn.commit()    
                      self.fetch_data() 
                      conn.close()  
                      messagebox.showinfo("delete","Successfully deleted student details",parent=self.root)  
                except Exception as es: 
                      messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    def reset_data(self):
          self.var_dep.set("")
          self.var_course.set("")
          self.var_year.set("")
          self.var_semester.set("")
          self.var_std_id.set("")
          self.var_Std_name.set("")
          self.var_div.set("A")
          self.var_roll.set("")
          self.var_gender.set("Male")
          self.Dob.set("")
          self.var_email.set("")
          self.var_phone.set("")
          self.var_address.set("")
          self.var_teacher.set("")
          self.var_radio1.set("")
   # ++============= d=generate data or take photo sample=======
    def generate_dataset(self):
           if self.var_dep.get()=="Select Department" or self.var_Std_name.get()=="" or self.var_std_id.get()=="":
                  messagebox.showerror("Error","All Fields are Rquired",parent=self.root)   
          
           else:
                 try:
               
                        conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognizer")
                        mycursor=conn.cursor()
                        mycursor.execute("select * from student")
                        myresult=mycursor.fetchall()
                        id=0
                        for x in myresult:
                              id+=1
                        mycursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s ",(
                                                                                                                        self.var_dep.get(),
                                                                                                                        self.var_course.get(),
                                                                                                                        self.var_year.get(),
                                                                                                                        self.var_semester.get(),
                                                                                                                        
                                                                                                                        self.var_Std_name.get(),
                                                                                                                        self.var_div.get(),
                                                                                                                        self.var_roll.get(),
                                                                                                                        self.var_gender.get(),
                                                                                                                        self.Dob.get(),
                                                                                                                        self.var_email.get(),
                                                                                                                        self.var_phone.get(),
                                                                                                                        self.var_address.get(),
                                                                                                                        self.var_teacher.get(),
                                                                                                                        self.var_radio1.get(),
                                                                                                                        self.var_std_id.get()==id+1
                                                                                                                                                ))
                        conn.commit()
                        self.fetch_data()
                        self.reset_data()
                        conn.close()
                        #+++========== load predifine data on face++
                        face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                        def face_cropped(img):
                              gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                              faces=face_classifier.detectMultiScale(gray,1.3,4)   
                        #++++++++=== scaling factor= 1.3, and  neighbor=5
                              for(x,y,w,h) in faces:
                                    face_cropped=img[y:y+h,x:x+w]
                                    return face_cropped
                        cap=cv2.VideoCapture(0)
                        img_id=0
                        while True:
                              ret,myframe=cap.read()
                              if face_cropped(myframe) is not None:
                                    img_id+=1
                                    face=cv2.resize(face_cropped(myframe),(450,450))
                                    face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                                    filenamepath="data/user."+str(id)+"."+str(img_id)+".jpg"
                                    cv2.imwrite(filenamepath,face)
                                    cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(255,0,0),2)
                                    cv2.imshow("croped face",face)
                              if cv2.waitKey(1)==13 or int(img_id)==100:
                                    break
                        cap.release()
                        cv2.destroyAllWindows()
                        messagebox.showinfo("Result","Generating data set completed!!!")
                 except Exception as es: 
                        messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    def searchby(self):

           conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognizer")
           mycursor=conn.cursor()
           mycursor.execute("select * from student where %s=%s",self.var_search_by,self.var_search_value)
           data=mycursor.fetchall()
           if len(data)!=0:
                self.student_table.delete(*self.student_table.get_children())
                for i in data:
                      self.student_table.insert("",END,values=i)
                conn.commit()
           conn.close()

              
       


                
               
                    


                                                                                    
if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
