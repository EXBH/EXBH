from tkinter import *

root = Tk()
root.title("приложение")
root.geometry("700x500")
root.configure(bg="#162f8a")
root.



tx = Label(text='выбор карт',font=('time new roman', 18, 'bold'),bg="#162f8a",fg="#ffdd00")
tx.pack()
frame = Frame(root, bg="#162f8a")
frame.pack(anchor='center')

btn1 = Button(frame, text='скелет', font=('comic Sans MS', 20,'bold'),bg="#ffffff")
btn2 = Button(frame, text='гоблин', font=('comic Sans MS', 20,'bold'),bg="#aeff00")
btn3 = Button(frame, text='варвар', font=('comic Sans MS', 20,'bold'),bg="#ffe205")
btn4 = Button(frame, text='ведьма', font=('comic Sans MS', 20,'bold'),bg="#8105a1")

btn1.grid(row=0, column=0, padx=10, pady=30)
btn2.grid(row=0, column=1, padx=10, pady=30)
btn3.grid(row=0, column=2, padx=10, pady=30)
btn4.grid(row=0, column=3, padx=10, pady=30)

root.mainloop()
