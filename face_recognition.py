from logging import disable
from random import setstate
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
from cv2 import data
from student import Student
import cv2
import os
import sys
import numpy as np
import mysql.connector
from time import strftime
from datetime import date, datetime




class Face_Recognition:
    def __init__(self,root):
            self.root=root
            self.root.geometry("800x800+0+0")
            self.root.title("Face recoginition")
            self.var_subject=StringVar()
            self.var_password=StringVar()

         #title label
            title_lbl=Label(self.root,text="Face Recoginition",font=("times new  roman",30,"bold"),bg= "white", fg="green")
            title_lbl.place(x=0,y=0, width=800,height=60) 
             # left image
            img=Image.open(r"C:\Users\Manoj\OneDrive\Desktop\python\College_Image\new.jpg")
            img= img.resize((400,700),Image.ANTIALIAS)
            self.photoimg=ImageTk.PhotoImage(img)
            f_lbl=Label(self.root,image=self.photoimg)
            f_lbl.place(x=0,y=60,width=400,height=720)
            #right side image 
            img2=Image.open(r"C:\Users\Manoj\OneDrive\Desktop\python\College_Image\new.jpg")
            img2= img2.resize((400,700),Image.ANTIALIAS)
            self.photoimg2=ImageTk.PhotoImage(img2)
            f_lbl=Label(self.root,image=self.photoimg2)
            f_lbl.place(x=400,y=60,width=400,height=720)
            #button
            btn_1=Button(f_lbl,command=self.recogintion_face,text="Face Recoginition",width=19,font=("times new roman",15,"bold"),bg="darkgreen",fg="white",cursor="hand2")
            btn_1.place(x=100,y=620,width=200,height=45)
            

            #title_lbl1=Label(self.root,text="Subject",font=("times new  roman",10,"bold"),bg= "yellow", fg="green")
            #title_lbl1.place(x=320,y=400, width=200,height=20) 

            #entryk=ttk.Entry(self.root,textvariable=self.var_subject,width=14,font=("times new roman",16,"bold"))
            #entryk.place(x=550,y=400, width=200,height=20) 

            #title_lbl2=Label(self.root,text="Password",font=("times new  roman",10,"bold"),bg= "yellow", fg="green")
            #title_lbl2.place(x=320,y=450, width=200,height=20) 
            #entryk1=ttk.Entry(self.root,show='*',textvariable=self.var_password,width=14,font=("times new roman",16,"bold"))
            #entryk1.place(x=550,y=450, width=200,height=20) 


            
            #btn_x=Button(self.root,text="starting",width=19,font=("times new roman",15,"bold"),bg="darkgreen",fg="white",cursor="hand2")
            #btn_x.place(x=450,y=500,width=200,height=25)
            ##btn_1["state"]="disabled"

            #if(self.var_password.__getattribute__=='manoj'):
                    #self.btn1["state"]="active"
    ##def enableface(self) :       
            

               

             
            

    
        



            #========== attendance==============
    def mark_attendace(self,i,r,n,d):
        
        
        with open("manoj.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list) ):
               now=datetime.now()
               d1=now.strftime("%d/%m/%Y")
               dtString= now.strftime("%H:%M:%S")
               f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},preset")
        
        with open("manoj.csv","r") as f1:
            myDataList1=f1.readlines()
            f1.close()
        ln=datetime.now().strftime("%Y%m%d-%H")    
        with open(("Attendance"+ln+".csv"),"w+") as f2:
            f2.writelines(myDataList1)

        with open("manoj.csv","r+") as f3:
            # f3.truncate()
            f3.close()       


   
      #=========== face recogination========
    def recogintion_face(self):

       
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
          gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
          features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)
          coord=[]

          for(x,y,w,h) in features:
              cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
              id,predict=clf.predict(gray_image[y:y+h,x:x+w])
              confidence=int((100*(1-predict/300)))
              try:
                    conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognizer")
                    mycursor=conn.cursor()

                    mycursor.execute("select Student_id from  student where Student_id="+str(id))
                    i=mycursor.fetchone()
                    #i='+'.join(i)
                    i=str(i)



                    mycursor.execute("select Name from student where Student_id="+str(id))
                    n=mycursor.fetchone()
                    n='+'.join(n)
                    # n=str (n)

                    mycursor.execute("select Roll from student where Student_id="+str(id))
                    r=mycursor.fetchone()
                    r='+'.join(r)
                    # r=str(r)

                    mycursor.execute("select Dep from student where Student_id="+str(id))
                    d=mycursor.fetchone()
                    d='+'.join(d)
              except Exception as es: 
                    messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)


              if confidence>77:
                  cv2.putText(img,f"ID:{i}",(x,y-90),cv2.FONT_HERSHEY_COMPLEX,0.8,(250,0,0),3)
                  cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(250,0,0),3)
                  cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(250,0,0),3)
                  cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(250,0,0),3)
                  self.mark_attendace(i,r,n,d)
              else:
                   cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                   cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
              coord=[x,y,w,y]
    
              
          return coord


        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img



        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        video_cap=cv2.VideoCapture(0)


        while True:
            
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To face Recognition",img)


            if cv2.waitKey(1)==13:
                break

        video_cap.release()
        cv2.destroyAllWindows()



if __name__ == "__main__":
        root=Tk()
        obj=Face_Recognition(root)
        root.mainloop()
    
