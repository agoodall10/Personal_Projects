import tkinter
from tkinter import Entry, messagebox

base=tkinter.Tk()
base.title("To-Do List")


def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(tkinter.END, task )
        entry.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title= "Error!",              #error message pop-up            
        message="Please enter task.")

def delete_task():
    task_index = listbox.curselection()[0]                          #deletes a task entered
    listbox.delete(task_index)

#GUI
frame= tkinter.Frame(base)                                          #creates frame for scrollbar
frame.pack()

scrollbar = tkinter.Scrollbar(frame)                                #creates a scrollbar and aligns it in position
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
scrollbar.pack()


listbox= tkinter.Listbox(frame,height=3, width=50)                  #size of listbox
listbox.pack(side=tkinter.LEFT)                 


listbox.config(yscrollcommand = scrollbar.set)
scrollbar.config(command=listbox.yview)


entry = tkinter.Entry(base, width=50)                               #user input for tasks
entry.pack()


button_task_add = tkinter.Button(base, text="Add Task",width=48, command=add_task)              
button_task_add.pack()                                              #creating a button where a user can enter tasks

button_task_delete = tkinter.Button(base, text="Delete Task", width=48, command=delete_task)
button_task_delete.pack()                                           #creating a button where a user can delete tasks


base.mainloop()