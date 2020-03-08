from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import numpy as np

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
        check_numeric(str_matrix)


def check_numeric(str_matrix):
    matrix = []
    matrix.append([])
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
        check_form(matrix)

def check_form(matrix):
    good_form = True
    first_y = matrix[0] #numero de columnas en la primera fila (x)
    rows = 0 #numero de filas en la matriz (y)
    for y in matrix:
        rows = rows + 1
        if(len(y) != len(first_y)):
            messagebox.showinfo(message='La matriz no tiene una forma adecuada', title="Error en archivo")
            good_form = False
            break

    if(good_form == True):
        create_map(matrix, first_y, rows)

def create_map(matrix, x, y):
    map_window = Tk()
    map_window.title("mapa")
    letter = 65
    c = 1
    for i in x:
        lbl = Label(map_window, text = chr(letter))
        lbl.grid(column=c, row=0)
        letter += 1
        c += 1

    c = 1
    for j in range(y):
        lbl = Label(map_window, text = c)
        lbl.grid(column=0, row=c)
        letter += 1
        c += 1

    map_window.mainloop()

root = Tk()
root.geometry('300x300')
root.title('IA')
root.configure(bg = 'light green')

button_explore = ttk.Button(root, text='explorar', command=lambda: explore())
button_explore.place(x=120, y=170)

button_exit = ttk.Button(root, text='salir', command=root.destroy)
button_exit.place(x=120, y=230)

root.mainloop()