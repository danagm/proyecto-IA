from tkinter import *
from tkinter import ttk
from tkinter import filedialog

def explore():
    root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select fil",filetypes = (("txt files","*.txt"),("all files","*.*")))
    parts = root.filename.split('.')
    print(parts)
    #print (root.filename)


root = Tk()
root.geometry('300x300')
root.title('IA')
root.configure(bg = 'light green')

button_explore = ttk.Button(root, text='explorar', command=lambda: explore())
button_explore.place(x=120, y=170)

button_exit = ttk.Button(root, text='salir', command=root.destroy)
button_exit.place(x=120, y=230)

root.mainloop()