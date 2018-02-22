from tkinter import *
from tkinter.filedialog import *
import pert

root=Tk();
root.title('PERT')

def on_import():
    
    global lbl
    
    Tk().withdraw()
    filename = askopenfilename()
    
    status = pert.main(filename)
    if status == -1:
        print('ERROR')
        lbl['text'] = 'ERROR'
        lbl.config(foreground = 'red')
    else:
        lbl['text'] = 'succesful :)'
        lbl.config(foreground = 'green')

def on_close():
    global root
    root.destroy()

frame = Frame(root, height=200, width=250)
frame.pack()

btn = Button(frame, text="Import Data", command = on_import)
btn.place(relx=0.5, rely=0.4, anchor = CENTER)

lbl = Label(frame, text=' ')
lbl.place(relx=0.5, rely=0.6, anchor = CENTER)

root.protocol('WM_DELETE_WINDOW', on_close)
root.mainloop()