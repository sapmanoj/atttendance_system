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


class Train:
    def __init__(self,root):
            self.root=root
            self.root.geometry("700x700+0+0")
            self.root.title("Face Recognition System")
            #title label
            title_lbl=Label(self.root,text="Train Data Set",font=("times new  roman",30,"bold"),bg= "white", fg="red")
            title_lbl.place(x=0,y=0, width=700) 
            # top image
            img=Image.open(r"C:\Users\Manoj\OneDrive\Desktop\python\College_Image\new.jpg")
            img= img.resize((700,300),Image.ANTIALIAS)
            self.photoimg=ImageTk.PhotoImage(img)
            f_lbl=Label(self.root,image=self.photoimg)
            f_lbl.place(x=0,y=50,width=700,height=300)
            #button
            save_btn=Button(self.root,command=self.train_classifier,text="Train Data",width=19,font=("times new roman",30,"bold"),bg="darkblue",fg="white")
            save_btn.place(x=0,y=350,width=700,height=60)
            #down image 
            img2=Image.open(r"C:\Users\Manoj\OneDrive\Desktop\python\College_Image\new.jpg")
            img2= img.resize((700,300),Image.ANTIALIAS)
            self.photoimg2=ImageTk.PhotoImage(img2)
            f_lbl=Label(self.root,image=self.photoimg2)
            f_lbl.place(x=0,y=400,width=700,height=300)
    def train_classifier(self):
        data_dir=("data")
        path=[ os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        faces=[]
        ids=[]
        for image in path:
            img=Image.open(image).convert('L')# gray scale image
            imagenp=np.array(img,'uint8') 
            id=int(os.path.split(image)[1].split('.')[1])


            faces.append(imagenp)
            ids.append(id)
            cv2.imshow("Training",imagenp)
            cv2.waitKey(1)==13
        ids=np.array(ids)
        #================= train the classifier and save =========
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Trainind data  set  completed!!!")


            
if __name__ == "__main__":
        root=Tk()
        obj=Train(root)
        root.mainloop()
    
