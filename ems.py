from customtkinter import*
from PIL import Image 
from tkinter import ttk,messagebox
import database

#function for the data table
def treeview_data():
   employee= database.fetch_employee()
   tree.delete(*tree.get_children())
   for employee in employee:
    tree.insert('',END,values=employee)


#add function
def add_employee():
    if idEntry.get()=='' or phoneEntry.get()=='' or nameEntry.get()=='' or salaryEntry.get()=='':
       messagebox.showerror('Error','All fields are required')
    elif database.id_exists(idEntry.get()):
        messagebox.showerror('Error','Id already exists')
    else:
        database.insert(idEntry.get(),nameEntry.get(),phoneEntry.get(),roleBox.get(),genderBox.get(),salaryEntry.get())
        treeview_data()
        messagebox.showinfo('Success','Data is added')
    

#GUI part
window=CTk()#same as root
window.geometry('930x580+100+100')
window.resizable(0,0)#it disabled the maximize button. At (0,0) you can also write (false,false)
window.title('Employee Management System')
window.configure(fg_color='#1E1E1E')#background Color

logo = CTkImage(Image.open('bg.jpg'), size=(930, 158))
logoLabel = CTkLabel(window, image=logo, text='')
logoLabel.grid(row=0, column=0,columnspan=2)#grid for divided into rows and columns

#for left Frame
leftFrame=CTkFrame(window,fg_color='#252526')#frame are the container
leftFrame.grid(row=1,column=0)#as column =0 so we have to start there after as col = 1

#for id
idLabel=CTkLabel(leftFrame,text='Id',font=('arial',18,'bold'),text_color='White')
idLabel.grid(row=0,column=0,padx=20,pady=15,sticky='w')
idEntry=CTkEntry(leftFrame,font=('arial',15,'bold'),width=180)
idEntry.grid(row=0,column=1)

#for name
nameLabel=CTkLabel(leftFrame,text='Name',font=('arial',18,'bold'),text_color='White')
nameLabel.grid(row=1,column=0,padx=20,pady=15,sticky='w')
nameEntry=CTkEntry(leftFrame,font=('arial',15,'bold'),width=180)
nameEntry.grid(row=1,column=1)

#for phone
phoneLabel=CTkLabel(leftFrame,text='Phone',font=('arial',18,'bold'),text_color='White')
phoneLabel.grid(row=2,column=0,padx=20,pady=15,sticky='w')
phoneEntry=CTkEntry(leftFrame,font=('arial',15,'bold'),width=180)
phoneEntry.grid(row=2,column=1)

#for role drop down
roleLabel=CTkLabel(leftFrame,text='Role',font=('arial',18,'bold'),text_color='White')
roleLabel.grid(row=3,column=0,padx=20,pady=15,sticky='w')
#role combobox
role_options=['Web Developer','Cloud Architect','Database Adminstartor',
'Flutter Developer','Java Developer','IT Consultatnt' ]
roleBox=CTkComboBox(leftFrame,values=role_options,width=180,font=('arial',15,'bold'),state='readonly')
roleBox.grid(row=3,column=1)
roleBox.set('Web Developer')

#for gender 
genderLabel=CTkLabel(leftFrame,text='Gender',font=('arial',18,'bold'),text_color='White')
genderLabel.grid(row=4,column=0,padx=20,pady=15,sticky='w')
gender_options=['Male','Female']
genderBox=CTkComboBox(leftFrame,values=gender_options,width=180,font=('arial',15,'bold'),state='readonly')
genderBox.grid(row=4,column=1)
genderBox.set('Male')

#for salary
salaryLabel=CTkLabel(leftFrame,text='Salary',font=('arial',18,'bold'),text_color='White')
salaryLabel.grid(row=5,column=0,padx=20,pady=15,sticky='w')
salaryEntry=CTkEntry(leftFrame,font=('arial',15,'bold'),width=180)
salaryEntry.grid(row=5,column=1)



#for Right Frame
rightFrame=CTkFrame(window)#frame are the container
rightFrame.grid(row=1,column=1)

search_options=['Id','Name','Phone','Role','Gender','Salary']
searchBox=CTkComboBox(rightFrame,values=search_options,state='readonly')
searchBox.grid(row=0,column=0)
searchBox.set('Search By')

searchEntry=CTkEntry(rightFrame)
searchEntry.grid(row=0,column=1)

SearchButton = CTkButton(rightFrame,text='Search',width=100)
SearchButton.grid(row=0,column=2)

ShowButton = CTkButton(rightFrame,text='Show All',width=100)
ShowButton.grid(row=0,column=3,pady=5)

tree=ttk.Treeview(rightFrame,height=13)#below the heading label
tree.grid(row=1,column=0,columnspan=4)

tree['columns']=('Id','Name','Phone','Role','Gender','Salary')
tree.heading('Id',text='Id')
tree.heading('Name',text='Name')
tree.heading('Phone',text='Phone')
tree.heading('Role',text='Role')
tree.heading('Gender',text='Gender')
tree.heading('Salary',text='Salary')

tree.config(show='headings')
tree.column('Id',width=100)
tree.column('Name',width=100)
tree.column('Phone',width=100)
tree.column('Role',width=100)
tree.column('Gender',width=100)
tree.column('Salary',width=100)

style=ttk.Style()
style.configure('Treeview.Heading',font=('arial',18,'bold'))
style.configure('Treeview',font=('arial',10,'bold'),rowheight=30,background='#161C30',foreground='white')

# scrollbar
scrollbar = ttk.Scrollbar(rightFrame, orient=VERTICAL)
scrollbar.grid(row=1, column=4, sticky='ns')



buttonFrame = CTkFrame(window,fg_color='#161C30')# button frame colour
buttonFrame.grid(row=2,column=0,columnspan=2)

newButton=CTkButton(buttonFrame,text='New Employee',font=('arial',15,'bold'),width=160,corner_radius=15)
newButton.grid(row=0,column=0,pady=5)

addButton=CTkButton(buttonFrame,text='Add Employee',font=('arial',15,'bold'),width=160,corner_radius=15,command=add_employee)
addButton.grid(row=0,column=1,pady=5,padx=5)

updateButton=CTkButton(buttonFrame,text='Update Employee',font=('arial',15,'bold'),width=160,corner_radius=15)
updateButton.grid(row=0,column=2,pady=5,padx=5)

deleteButton=CTkButton(buttonFrame,text='Delete Employee',font=('arial',15,'bold'),width=160,corner_radius=15)
deleteButton.grid(row=0,column=3,pady=5,padx=5)

deleteallButton=CTkButton(buttonFrame,text='Delete All Employee',font=('arial',15,'bold'),width=160,corner_radius=15)
deleteallButton.grid(row=0,column=4,pady=5,padx=5)


window.mainloop()