from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

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

def save_colors(color_entrys, terrain_entrys): #guarda el texto de las entrys de la función siguiente
    colors = []
    terrains = []
    for c in color_entrys:
        colors.append(c.get())
    
    for t in terrain_entrys:
        terrains.append(t.get())
    
    for c in colors:
        print(c)
    
    for t in terrains:
        print(t)


def colors(matrix):
    numbers = [] #números diferentes que existen en la matriz
    for i in matrix:
        for j in i:
            if(not numbers.__contains__(j)):
                numbers.append(j)
    
    if(len(numbers) > 10):
        messagebox.showinfo(message='Hay demasiados terrenos', title="Error en archivo")
    else:
        color_entrys = [] #lista de entrys de los colores
        terrain_entrys = [] #lista de entrys de los nombres de los terrenos
        ask_colors_window = Tk()
        ask_colors_window.geometry('500x400')
        ask_colors_window.title("Terrenos")
        ask_colors_window.configure(bg = 'light pink')
        ttk.Label(ask_colors_window, text="01 - Café\n02 - Naranja\n03 - Negro\n04 - Gris\n05 - Verde fuerte").place(x=0, y=0)
        ttk.Label(ask_colors_window, text="06 - Verde claro  \n07 - Azul fuerte\n08 - Azul claro\n09 - Blanco\n10 - Rojo").place(x=0, y=76)
        ttk.Label(ask_colors_window, text="                  Terreno                   Color    ").place(x=175, y=20)

        i_place = 50
        for i in range(len(numbers)):
            c_e = StringVar()
            t_e = StringVar()
            ttk.Label(ask_colors_window, text=numbers[i]).place(x=180, y=i_place)
            Entry(ask_colors_window, textvariable=c_e, width=3).place(x=330, y=i_place)
            color_entrys.append(c_e)
            Entry(ask_colors_window, textvariable=t_e).place(x=200, y=i_place)
            terrain_entrys.append(t_e)
            i_place += 30

        button_save = ttk.Button(ask_colors_window, text="guardar", command=lambda: save_colors(color_entrys, terrain_entrys))
        button_save.place(x=180, y=350)

        ask_colors_window.mainloop()

    return numbers

def create_map(matrix, x, y):
    numbers = colors(matrix)
    print(numbers)
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

    R = 1
    for r in range(y):
        C = 1
        for c in range(len(x)):
            cell = Entry(map_window, width=5)
            cell.grid(padx=3, pady=3, row=R, column=C)
            cell.insert(0, matrix[r][c])
            C += 1
        R += 1

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