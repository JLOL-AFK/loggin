#Import libraries
from tkinter import*
import os 

#Delete function
def delete(x):
        x.destroy()

#Delete function for muliple commands at once
def delete2(*widgets):
        for widget in widgets:
            widget.destroy()

#Login success pop-up window message function
def login_success():
    global window3
    window3=Toplevel(window)
    window3.title("Login success")
    window3.geometry("150x100")
    Label(window3,text="Login success!").pack()
    Button(window3, text="OK",command=lambda:delete2(window3,window2,window)).pack()

#Password not recognised pop-up window message function
def password_not_recognised():
    global window4
    window4=Toplevel(window)
    window4.title("Password not recognised")
    window4.geometry("150x100")
    Label(window4,text="Password Incorrect!").pack()
    Button(window4, text="OK",command=lambda:delete(window4)).pack()

#Username not found pop-up window message function
def username_not_found():
    global window5
    window5=Toplevel(window)
    window5.title("User not found")
    window5.geometry("150x100")
    Label(window5,text="User not found!").pack()
    Button(window5, text="OK",command=lambda:delete(window5)).pack()

#staffID correct pop-up window message function
def staffID_correct():
    global window6
    window6=Toplevel(window)
    window6.title("StaffID found")
    window6.geometry("150x100")
    Label(window6,text="StaffID correct!").pack()
    Button(window6, text="OK",command=lambda:delete(window6)).pack()

#Staff ID incorrect pop-up window message function
def staffID_incorrect():
    global window7
    window7=Toplevel(window)
    window7.title("StaffID not found")
    window7.geometry("150x100")
    Label(window7,text="StaffID Incorrect!").pack()
    Button(window7, text="OK",command=lambda:delete(window7)).pack()



def login_verify():
    username1=username_verify.get()
    password1=password_verify.get()
    staffID1 =staffID_verify.get()
    username_entry2.delete(0,END)
    password_entry2.delete(0,END)
    staffID_entry2.delete(0,END)    
    
    #importing file with the username and passwords
    list_of_files=os.listdir()
    if username1 in list_of_files:
      file1=open(username1,"r")
      verify=file1.read().splitlines()
      if password1 in verify:
          login_success() 
      else:
          password_not_recognised()
    else:
        username_not_found()
    if staffID1 in verify:
       staffID_correct()
    else:
       staffID_incorrect() 
    

         
def register_user():
    global window1
    username_info=username.get()
    password_info=password.get()
    staffID_info=staffID.get()

#Will store and write the username, password and staffID in a docx.
    file=open(username_info,"w")
    file.write(username_info+"\n")
    file.write(password_info+"\n")
    file.write(staffID_info)
    file.close()
#Clears the enterd field once registered 
    username_entry.delete(0,END)
    password_entry.delete(0,END)
    staffID_entry.delete(0,END)

    Label(window1, text="Account created!",fg="red", font=("Arial",12)).pack()
    Label(window1,text="Press Main menu when done!", fg="red", font=("Arial",15)).pack()

def register():
    global window1
    window1=Toplevel(window)
    window1.title("Account Creation")
    window1.geometry("600x600")
    window1.configure(bg="blue")

#Global variable
    global username
    global password
    global staffID
    global username_entry
    global password_entry
    global staffID_entry
    
    #Storing variable
    username=StringVar()
    password=StringVar()
    staffID=StringVar()

    #creating heading and username Labels 
    Label(window1,text= "Welcome to the registration page,please enter your details below in order to create an account, Thank you!").pack()
    Label(window1,text= "").pack()
    Label(window1,text= "Username", font=("Arial",15)).pack()
   
    #Creating username box
    username_entry=Entry(window1,textvariable=username)
    username_entry.pack()
    
    #creating password Label
    Label(window1,text="").pack()
    Label(window1,text= "Password", font=("Arial",15)).pack()
   
    #password box
    password_entry=Entry(window1,textvariable=password)
    password_entry.pack()
    Label(window1,text="").pack()
    
    #staffID Label
    Label(window1,text="Staff ID", font=("Arial",15)).pack()
    #staffID box
    staffID_entry=Entry(window1,textvariable=staffID)
    staffID_entry.pack()
    
    #Creating register buttons
    Button(window1,text="Register",command=register_user, width=10, height=1).pack()
    Button(window1,text="Main Menu",command=lambda:delete(window1),width=10, height=1).pack()




def login():
    print("Welcome to Information Systems LTD")
    global window2
    global username_verify
    global password_verify
    global staffID_verify
    window2=Toplevel(window) 
    window2.title("Information Systems Login page")
    window2.geometry("600x600")

    username_verify=StringVar()
    password_verify=StringVar()
    staffID_verify=StringVar()
    
    global username_verify1
    global password_verify1
    global staffID_verify1
    
    global username_entry2
    global password_entry2
    global staffID_entry2

    #Creating labels for welcome message
    Label(window2,text= "Welcome to the login page,please enter your details below in order to continue, Thank you!").pack()
    Label(window2,text= "").pack()

   #Username label and entry
    Label(window2,text= "Username", font=("Arial",15)).pack()
    username_entry2=Entry(window2,textvariable=username_verify)
    username_entry2.pack()
    
   #Password label and entry
    Label(window2,text= "Password", font=("Arial",15)).pack()
    password_entry2=Entry(window2,textvariable=password_verify)
    password_entry2.pack()
   #StaffID label and entry
    Label(window2,text="Staff ID", font=("Arial",15)).pack()
    staffID_entry2=Entry(window2,textvariable=staffID_verify)
    staffID_entry2.pack()

    #Login button
    Button(window2,text="Login",width=10, height=1, font=("Arial",15), command=login_verify).pack()

def main_window():
    global window
    window=Tk()
    window.geometry("600x600") 
    window.title("Information Systems Login and Registration Page")
    window.configure(bg="blue")

#Creating the label widgets
   #Creating header label
    Label(text="Information Sytstems Login and Registration page", fg="black",bg="red" ,width="300", height="1", font=("Arial", 15,)).pack()
    Label(text= "",bg="blue").pack()
   
   #Creating login buttom
    Button(text="Login", fg="black", bg="red",height="2",width="30",command=login, font=("Arial",15)).pack()
    Label(text= "",bg="blue").pack()

   #Creating Register button
    Button(text="Create an account", fg="black", bg="red",height="2",width="30",command=register, font=("Arial",15)).pack()
    Label(text= "",bg="blue").pack()

    #introduction messsage
    Label(text= "If you do not have an account please create an account using your staff ID!",fg="black",bg="red" ,width="300", height="1", font=("Arial", 13,)).pack()
   
    

    window.mainloop()



main_window()