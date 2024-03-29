from tkinter import *
from tkinter import ttk
from backend import *

# shut the window
def close_window(tool):
    tool.destroy()  # destroy the window

# add student
def add_student():
    
    def add_rec():
        from tkinter import messagebox

        #Getting the values from the fields...

        student_id = int(student_id_entry.get())
        student_name = student_name_entry.get()
        student_age = int(student_age_entry.get())
        student_roll = student_roll_entry.get()
        student_branch = student_branch_entry.get()
        
        #Calling the backend....

        result=add_new_record(student_id, student_name, student_age, student_roll, student_branch)
        if result['success']:
            messagebox.showinfo("Success", result['message'])
        else:
            messagebox.showinfo("Error", result['message'])

        #Closing the window....
        addrecordwindow.destroy()


    addrecordwindow= Toplevel()
    addrecordwindow.title("Add Record")
    addrecordwindow.geometry("1600x1600")
    addrecordwindow.configure(background='#00BFFF')

    add_record_label=Label(addrecordwindow,text="Add Record",font=("arial",20,"bold"))
    add_record_label.grid(row=0,column=0,padx=20,pady=20)

    #add student id
    student_id_label = Label(addrecordwindow, text="Student ID", font=("Times New Roman", 20))
    student_id_label.grid(row=1, column=0, padx=10, pady=40)

    student_id_entry = Entry(addrecordwindow, font=("Times New Roman", 20))
    student_id_entry.grid(row=1, column=1, padx=10, pady=40)

    #add student name
    student_name_label = Label(addrecordwindow, text="Student Name", font=("Times New Roman", 20))
    student_name_label.grid(row=2, column=0, padx=10, pady=40)
    
    student_name_entry = Entry(addrecordwindow, font=("Times New Roman", 20))
    student_name_entry.grid(row=2, column=1, padx=10, pady=40)

    #add student age
    student_age_label = Label(addrecordwindow, text="Student Age", font=("Times New Roman", 20))
    student_age_label.grid(row=3, column=0, padx=10, pady=40)

    student_age_entry = Entry(addrecordwindow, font=("Times New Roman", 20))
    student_age_entry.grid(row=3, column=1, padx=10, pady=40)

    #add student roll
    student_roll_label = Label(addrecordwindow, text="Student Roll", font=("Times New Roman", 20))
    student_roll_label.grid(row=4, column=0, padx=10, pady=40)

    student_roll_entry = Entry(addrecordwindow, font=("Times New Roman", 20))
    student_roll_entry.grid(row=4, column=1, padx=10, pady=40)

    #add student branch
    student_branch_label = Label(addrecordwindow, text="Student Branch", font=("Times New Roman", 20))
    student_branch_label.grid(row=5, column=0, padx=10, pady=40)

    student_branch_entry = Entry(addrecordwindow, font=("Times New Roman", 20))
    student_branch_entry.grid(row=5, column=1, padx=10, pady=40)

    #add student button
    add_student_button = Button(addrecordwindow, text="Add Student", font=("Times New Roman", 20), command=add_rec)
    add_student_button.grid(row=6, column=1, padx=10, pady=40)

    #close button
    close_button = Button(addrecordwindow, text="Back", font=("Times New Roman", 20), command=lambda: close_window(addrecordwindow))
    close_button.grid(row=6, column=0, padx=10, pady=40)

#search student
def search_student():
    from tkinter import messagebox
    def search_rec():
        
        #Getting the id....
        student_id = int(student_id_entry.get())

        #Fetching record from backend...
        result=search_record_by_id(student_id)
        if(result['success']):

            student_name=Label(searchrecordwindow,text="Name",font=("arial",20,"bold"))
            student_name.grid(row=2,column=0,padx=20,pady=20)

            student_name_value=Entry(searchrecordwindow,text="",font=("arial",20))
            student_name_value.grid(row=2,column=1,padx=20,pady=20)

            student_age=Label(searchrecordwindow,text="Age",font=("arial",20,"bold"))
            student_age.grid(row=3,column=0,padx=20,pady=20)

            student_age_value=Entry(searchrecordwindow,text="",font=("arial",20))
            student_age_value.grid(row=3,column=1,padx=20,pady=20)

            student_roll=Label(searchrecordwindow,text="Roll No",font=("arial",20,"bold"))
            student_roll.grid(row=4,column=0,padx=20,pady=20)

            student_roll_value=Entry(searchrecordwindow,text="",font=("arial",20))
            student_roll_value.grid(row=4,column=1,padx=20,pady=20)

            student_branch=Label(searchrecordwindow,text="Branch",font=("arial",20,"bold"))
            student_branch.grid(row=5,column=0,padx=20,pady=20)

            student_branch_value=Entry(searchrecordwindow,text="",font=("arial",20))
            student_branch_value.grid(row=5,column=1,padx=20,pady=20)

            for x in result['data']:
                student_name_value.insert(0,x[1])
                student_age_value.insert(0,x[2])
                student_roll_value.insert(0,x[3])
                student_branch_value.insert(0,x[4])

            back_button.grid(row=6, column=0, padx=10, pady=40)

            searchButton.grid(row=6, column=2, padx=10, pady=40)
        else:
            messagebox.showinfo("Error", result['message'])
            searchrecordwindow.destroy()

    searchrecordwindow= Toplevel()
    searchrecordwindow.title("Search Record")
    searchrecordwindow.geometry("1600x1600")
    searchrecordwindow.configure(background='#00BFFF')

    search_record_label=Label(searchrecordwindow,text="Search Record",font=("arial",20,"bold"))
    search_record_label.grid(row=0,column=0,padx=20,pady=20)

    #add student id
    student_id_label = Label(searchrecordwindow, text="Student ID", font=("Times New Roman", 20))
    student_id_label.grid(row=1, column=0, padx=10, pady=40)

    student_id_entry = Entry(searchrecordwindow, font=("Times New Roman", 20))
    student_id_entry.grid(row=1, column=1, padx=10, pady=40)

    back_button = Button(searchrecordwindow, text="Back", font=("Times New Roman", 20), command=lambda: close_window(searchrecordwindow))
    back_button.grid(row=2, column=0, padx=10, pady=40)
    
    searchButton = Button(searchrecordwindow, text="Search", font=("Times New Roman", 20), command=search_rec)
    searchButton.grid(row=2, column=1, padx=10, pady=40)

#modify student
def modify_student():
    from tkinter import messagebox
    
    def modify_rec_helper():
        
        def modify_rec():

            #Getting new values...
            student_id = int(student_id_entry.get())
            student_name = student_name_value.get()
            student_age = int(student_age_value.get())
            student_roll = student_roll_value.get()
            student_branch = student_branch_value.get()

            #Updating record using backend...
            result=modify_record(student_id, student_name, student_age, student_roll, student_branch)
            messagebox.showinfo("Success", result['message'])
            modifyrecordwindow.destroy()
        
        #Getting the id....
        student_id = int(student_id_entry.get())

        #Fetching record from backend...
        result=search_record_by_id(student_id)

        #check if the student exists in the database
        if(result['success']):
            student_name=Label(modifyrecordwindow,text="Name",font=("arial",20,"bold"))
            student_name.grid(row=2,column=0,padx=20,pady=20)

            student_name_value=Entry(modifyrecordwindow,text="",font=("arial",20))
            student_name_value.grid(row=2,column=1,padx=20,pady=20)

            student_age=Label(modifyrecordwindow,text="Age",font=("arial",20,"bold"))
            student_age.grid(row=3,column=0,padx=20,pady=20)

            student_age_value=Entry(modifyrecordwindow,text="",font=("arial",20))
            student_age_value.grid(row=3,column=1,padx=20,pady=20)

            student_roll=Label(modifyrecordwindow,text="Roll No",font=("arial",20,"bold"))
            student_roll.grid(row=4,column=0,padx=20,pady=20)

            student_roll_value=Entry(modifyrecordwindow,text="",font=("arial",20))
            student_roll_value.grid(row=4,column=1,padx=20,pady=20)

            student_branch=Label(modifyrecordwindow,text="Branch",font=("arial",20,"bold"))
            student_branch.grid(row=5,column=0,padx=20,pady=20)

            student_branch_value=Entry(modifyrecordwindow,text="",font=("arial",20))
            student_branch_value.grid(row=5,column=1,padx=20,pady=20)

            for x in result['data']:
                student_name_value.insert(0,x[1])
                student_age_value.insert(0,x[2])
                student_roll_value.insert(0,x[3])
                student_branch_value.insert(0,x[4])

            back_button.grid(row=6, column=0, padx=10, pady=40)

            modify_button["command"] = lambda: modify_rec()
            modify_button["text"] = "Modify"
            modify_button.grid(row=6, column=1, padx=10, pady=40)
        else:
            messagebox.showinfo("Error", result['message'])
            modifyrecordwindow.destroy()
    

    modifyrecordwindow= Toplevel()
    modifyrecordwindow.title("Modify Record")
    modifyrecordwindow.geometry("1600x1600")
    modifyrecordwindow.configure(background='#00BFFF')

    modify_record_label=Label(modifyrecordwindow,text="Modify Record",font=("arial",20,"bold"))
    modify_record_label.grid(row=0,column=0,padx=20,pady=20)

    student_id_label = Label(modifyrecordwindow, text="Student ID", font=("Times New Roman", 20))
    student_id_label.grid(row=1, column=0, padx=10, pady=40)

    student_id_entry = Entry(modifyrecordwindow, font=("Times New Roman", 20))
    student_id_entry.grid(row=1, column=1, padx=10, pady=40)

    back_button = Button(modifyrecordwindow, text="Back", font=("Times New Roman", 20), command=lambda: close_window(modifyrecordwindow))
    back_button.grid(row=2, column=0, padx=10, pady=40)

    modify_button = Button(modifyrecordwindow, text="Search And Modify", font=("Times New Roman", 20), command=modify_rec_helper)
    modify_button.grid(row=2, column=1, padx=10, pady=40)

#delete student
def delete_student():
    from tkinter import messagebox
    def delete_rec(student_id):
        result=delete_record(student_id)
        messagebox.showinfo("Success", result['message'])
        deleterecordwindow.destroy()

    def del_rec_helper():

        #define the variables
        student_id = int(student_id_entry.get())

        #check if the student exist in the database
        result=search_record_by_id(student_id)

        if result['success']:
            student_name=Label(deleterecordwindow,text="Name",font=("arial",20,"bold"))
            student_name.grid(row=2,column=0,padx=20,pady=20)

            student_name_value=Entry(deleterecordwindow,text="",font=("arial",20))
            student_name_value.grid(row=2,column=1,padx=20,pady=20)

            student_age=Label(deleterecordwindow,text="Age",font=("arial",20,"bold"))
            student_age.grid(row=3,column=0,padx=20,pady=20)

            student_age_value=Entry(deleterecordwindow,text="",font=("arial",20))
            student_age_value.grid(row=3,column=1,padx=20,pady=20)

            student_roll=Label(deleterecordwindow,text="Roll No",font=("arial",20,"bold"))
            student_roll.grid(row=4,column=0,padx=20,pady=20)

            student_roll_value=Entry(deleterecordwindow,text="",font=("arial",20))
            student_roll_value.grid(row=4,column=1,padx=20,pady=20)

            student_branch=Label(deleterecordwindow,text="Branch",font=("arial",20,"bold"))
            student_branch.grid(row=5,column=0,padx=20,pady=20)

            student_branch_value=Entry(deleterecordwindow,text="",font=("arial",20))
            student_branch_value.grid(row=5,column=1,padx=20,pady=20)

            for x in result['data']:
                student_name_value.insert(0,x[1])
                student_age_value.insert(0,x[2])
                student_roll_value.insert(0,x[3])
                student_branch_value.insert(0,x[4])
            
            #Realinging the buttons
            back_button.grid(row=6, column=0, padx=10, pady=40)
            delete_button["command"] = lambda: delete_rec(student_id)
            delete_button["text"] = "Delete"
            delete_button.grid(row=6, column=1, padx=10, pady=40)
        else:
            messagebox.showinfo("Error", result['message'])
            deleterecordwindow.destroy()
    

    deleterecordwindow= Toplevel()
    deleterecordwindow.title("Delete Record")
    deleterecordwindow.geometry("1600x1600")
    deleterecordwindow.configure(background='#00BFFF')

    delete_record_label=Label(deleterecordwindow,text="Delete Record",font=("arial",20,"bold"))
    delete_record_label.grid(row=0,column=0,padx=20,pady=20)

    #add student id
    student_id_label = Label(deleterecordwindow, text="Student ID", font=("Times New Roman", 20))
    student_id_label.grid(row=1, column=0, padx=10, pady=40)

    student_id_entry = Entry(deleterecordwindow, font=("Times New Roman", 20))
    student_id_entry.grid(row=1, column=1, padx=10, pady=40)
    
    back_button = Button(deleterecordwindow, text="Back", font=("Times New Roman", 20), command=lambda: close_window(deleterecordwindow))
    back_button.grid(row=2, column=0, padx=10, pady=40)
    
    delete_button = Button(deleterecordwindow, text="Search And Delete", font=("Times New Roman", 20), command=del_rec_helper)
    delete_button.grid(row=2, column=1, padx=10, pady=40)

#view all records
def view_all_records():

    view_all_records_window= Toplevel()
    view_all_records_window.title("View All Records")
    view_all_records_window.geometry("1600x1600")
    view_all_records_window.configure(background='#00BFFF')

    view_all_records_label=Label(view_all_records_window,text="View All Records",font=("arial",20,"bold"))
    view_all_records_label.grid(row=0,column=0,padx=20,pady=20)

    #running sql query
    result= fetch_all_records()
    lhead=["ID","Name","Age","Roll No","Branch"]
    
    #using treeview
    tree=ttk.Treeview(view_all_records_window,columns=lhead,show="headings")
    tree.grid(row=1,column=0,padx=10,pady=40)
    tree.heading("#1",text="ID")
    tree.heading("#2",text="Name")
    tree.heading("#3",text="Age")
    tree.heading("#4",text="Roll No")
    tree.heading("#5",text="Branch")

    for x in result['data']:
        tree.insert("",END,values=x)

    back_button = Button(view_all_records_window, text="Back", font=("Times New Roman", 20), command=lambda: close_window(view_all_records_window))
    back_button.grid(row=1, column=0, padx=10, pady=40)   


#main window
root = Tk()
root.title("Student Record Manager")
root.geometry("1000x1000")
root.configure(background='#00BFFF')
rootlabel= Label(root, text="STUDENT RECORD MANAGER", font=("Times New Roman", 20))
rootlabel.grid(row=1, column=1, padx=25,pady=40)

addRecord= Button(root, text="Add Record", font=("Times New Roman", 15),command=add_student)
addRecord.grid(row=2, column=1, padx=500,pady=10)

searchRecord = Button(root, text="Search Record", font=("Times New Roman", 15),command=search_student)
searchRecord.grid(row=3, column=1, padx=500,pady=10)

modifyRecord = Button(root, text="Modify Record", font=("Times New Roman", 15), command=modify_student)
modifyRecord.grid(row=4, column=1, padx=500,pady=10)

deleteRecord = Button(root, text="Delete Record", font=("Times New Roman", 15),command=delete_student)
deleteRecord.grid(row=5, column=1, padx=500,pady=10)

allRecord = Button(root, text="View All Records", font=("Times New Roman", 15),command=view_all_records)
allRecord.grid(row=6, column=1, padx=500,pady=10)

exitButton= Button(root, text="Exit", font=("Times New Roman", 15),command=lambda:close_window(root))
exitButton.grid(row=7, column=1, padx=500,pady=10)

root.mainloop()