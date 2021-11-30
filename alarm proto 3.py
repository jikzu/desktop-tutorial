

from tkinter import *
import datetime    #A module to take the present time in use
import winsound
from playsound import playsound     #module to integrate a audio file in program
from tkinter import messagebox





def Alarm():
    global x,y
    if a1.get()=="AM":
        x=int(b1.get())
        y=int(b2.get())
        if x <= 12 and y <= 60:
              Time()
         else:            
               messagebox.showerror("error","please enter time in 12-hour format only")
                
    if a1.get()=="PM":
        x=int(b1.get())+12  #to convert 12-hour format to 24-hour for comparision with present system time(that is in 24 hour format)
        y=int(b2.get())
         if x <= 24 and y <= 60:
              Time()
         else:
               messagebox.showerror("error","please enter time in 12-hour format only")
                
  def Time():       
     messagebox.showinfo("notification", "alarm has been set")   #pops up a notification when time is set for alarm
     while True:
          if x == datetime.datetime.now().hour and  y == datetime.datetime.now().minute :   #compares present time with alarm time set
               print("subh ho gyi hae abhi khud jaagg jaooo, wrna mummie aenge aur chapal maar ke jaeynege")   #prints at alarm time     
               playsound("Creepy-background-music.mp3",winsound.SND_ASYNC)   #plays a audio at alarm time
               break
            
        
    

#setting-up the window for program
a=Tk()
a.title("Alarm clock by Jatin and Syed")
a.config(bg="grey")
a.geometry("600x300")


#adding buttons, labels and taking input from user.
label1=Label(a,text="Hours:")
label2=Label(a,text="Minute")
label1.place(x=70,y=30)
label2.place(x=310,y=30)
b1=Entry(a)
b2=Entry(a)
b1.place(x=120,y=30)
b2.place(x=360,y=30)
a1=Spinbox(a,value=(["AM","PM"]),width=10)
a1.place(x=280,y=90)
label3=Label(a,text="AM OR PM :")
label3.place(x=200,y=90)
c1=Button(a,text="Set Alarm",command=Alarm)
c1.place(x=250,y=150)
mainloop()






