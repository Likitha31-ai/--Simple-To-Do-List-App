import tkinter as tk
import sqlite3 as sql

def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)

def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except IndexError:
        pass

def mark_as_completed():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.itemconfig(task_index, {'bg': 'light green', 'fg': 'black'})
    except IndexError:
        pass

def clear_list():  
    listbox_tasks.delete(0, 'end')
  
def close():  
    print(tasks)  
    gui.destroy()  
  
def retrieve_database():  
    while(len(tasks) != 0):  
        tasks.pop()  
    for row in the_cursor.execute('select title from tasks'):  
        tasks.append(row[0])  

gui = tk.Tk()
gui.title("To-Do-List")
gui.geometry("500x450+750+250")
gui.resizable(0, 0)
gui.configure(bg = "#f4cec4")
the_connection = sql.connect('listOfTasks.db')  
the_cursor = the_connection.cursor()  
the_cursor.execute('create table if not exists tasks (title text)') 

entry_task = tk.Entry(gui, width=40)
entry_task.pack(pady=5)

listbox_tasks = tk.Listbox(gui, height=10, width=50, bg='white', fg='black')
listbox_tasks.pack(pady=5)

button_add_task = tk.Button(gui, text="Add Task", width=30, command=add_task)
button_add_task.pack(pady=5)

button_delete_task = tk.Button(gui, text="Delete Task", width=30, command=delete_task)
button_delete_task.pack(pady=5)

button_mark_as_completed = tk.Button(gui, text="Mark as Completed", width=30, command=mark_as_completed)
button_mark_as_completed.pack(pady=5)

gui.mainloop()