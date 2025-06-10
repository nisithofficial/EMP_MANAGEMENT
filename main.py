from customtkinter import *
from PIL import Image  # for image use in our project
from tkinter import ttk,
import database

def login():
    if UsernameEntry.get()=='' or PasswordEntry.get()=='':
        messagebox.showerror('Error', 'All fields are required')
    elif UsernameEntry.get()=='Nisith' and PasswordEntry.get()=='1234':
        messagebox.showinfo('Success','Login is successful')
        root.destroy()
        import ems #for close after click on ok(login page)
    else:
        messagebox.showerror('Error','Wrong credentials')

    

root = CTk()
root.geometry('930x478')  # for the well-mannered size purpose
root.resizable(0, 0)  # maximize option is disabled
root.title("Login Page")

# Load image correctly
image = CTkImage(Image.open('cover.png'), size=(930, 478))
imageLabel = CTkLabel(root, image=image, text='')
imageLabel.place(x=0, y=0)  # to make the cover.png constant at position

# Correct label name and placement
headingLabel = CTkLabel(root, text='Employee Management System',bg_color ='#FAFAFA',font=('Goudy Old Style',20,'bold'),text_color='dark blue')
headingLabel.place(x=20, y=100)  # Corrected placement
UsernameEntry = CTkEntry(root,placeholder_text='Entry your Username',width=180)#entry for the user - root - root window for the display
UsernameEntry.place(x=50, y=150)

PasswordEntry = CTkEntry(root,placeholder_text='Enter your Password',width=180,show='*')#Entry for the password - * for the pass you enter is not seen by other
PasswordEntry.place(x=50, y=200)

#adding button and add its functionality
loginButton = CTkButton(root,text='Log in',width=90,cursor ='hand2',command =login)# hand2 for the cursor to hand - login is a function - add at the begginning 
loginButton.place(x=90, y=250)
root.mainloop()
