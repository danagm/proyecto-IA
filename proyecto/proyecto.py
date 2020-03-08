from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import numpy as np

matrix = []
matrix.append([])

def explore():
    root.filename = ''
    root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("txt files","*.txt"),("all files","*.*")))
    parts = root.filename.split('.')
    if(parts[len(parts)-1] != 'txt'):
        messagebox.showinfo(message='Favor de seleccionar un archivo de texto, "txt file"', title="Error en archivo")
    else:
        my_file = open(root.filename, 'r')
        str_matrix = my_file.read()
        my_file.close()
        check(str_matrix)


def check(str_matrix):
    only_numeric = True
    i = 0
    for x in str_matrix:
        if(x == ','):
            pass
        elif(x.isdigit()):
            matrix[i].append(x)
        elif(x=='\0' or x=='\n'):
            matrix.append([])
            i = i+1
        else:
            messagebox.showinfo(message='La matriz contiene valores no numéricos', title="Error en archivo")
            only_numeric = False
            break

    if(only_numeric == True):
        print(matrix)
        



root = Tk()
root.geometry('300x300')
root.title('IA')
root.configure(bg = 'light green')

button_explore = ttk.Button(root, text='explorar', command=lambda: explore())
button_explore.place(x=120, y=170)

button_exit = ttk.Button(root, text='salir', command=root.destroy)
button_exit.place(x=120, y=230)

root.mainloop()