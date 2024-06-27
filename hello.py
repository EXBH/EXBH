from tkinter import *

root = Tk()
root.title("app")
root.geometry("700x500")
root.configure(bg='#000000')
frame = Frame(root,bg='#000000')
frame.pack(anchor='center')

def calculate():
    val1 = ent1.get()
    valC1 = ent2.get()
    val2 = ent1.get()

    if valC1 == "+" :
        txt['text'] = int(val1) + int(val2)
    elif valC1 == "-" :
        txt['text'] = int(val1) - int(val2)
    elif valC1 == "/" :
        txt['text'] = int(val1) / int(val2)
    elif valC1 == "*" :
        txt['text'] = int(val1) * int(val2)
    




lab1 = Label(frame,text='число',font=('Comic Sans MS', 18, 'bold'),bg="#000000",fg="#ffffff")
lab2 = Label(frame, text='операция',font=('Comic Sans MS', 18, 'bold'),bg="#000000",fg="#ffffff")
lab3 = Label(frame,text='число',font=('Comic Sans MS', 18, 'bold'),bg="#000000",fg="#ffffff")

ent1 = Entry(frame,font=('Comic Sans MS',18, "bold"))
ent2 = Entry(frame,font=('Comic Sans MS',18, "bold"))
ent3 = Entry(frame,font=('Comic Sans MS',18, "bold"))

btn = Button(frame, text="вычеслить", font=('Comic Sans MS', 18, "bold" ), bg="#000000",fg='#ffffff', command=calculate)
txt = Label(frame,text="",font=('Comic Sans MS', 18, "bold" ), bg='#000000',fg="#ffffff")

lab1.grid(row=0, column=0, padx=10, pady=10)
lab2.grid(row=0, column=1, padx=10, pady=10)
lab3.grid(row=0, column=2, padx=10, pady=10)
ent1.grid(row=1, column=0, padx=10, pady=10)
ent2.grid(row=1, column=1, padx=10, pady=10)
ent3.grid(row=1, column=2, padx=10, pady=10)
btn.grid(row=2, column=0, columnspan=3,sticky='we', padx=10, pady=10)
txt.grid(row=3, column=0, columnspan=3,sticky='we', padx=10, pady=10)

root.mainloop()




