import tkinter as tk

def open_second_window():
    main_window.withdraw()
    second_window.deiconify()

def back_to_main_window():
    second_window.withdraw()
    main_window.deiconify()

main_window = tk.Tk()
main_window.title("main window")
main_window.geometry("500x500")
main_window.configure(bg="#4c2457")

txt = tk.Label(main_window, text='main window',font=('times new roman', 20, 'bold'),bg="#162f8a",fg="#ffdd00")
txt.pack()

open_button = tk.Button(main_window, text="open second window",command=open)
open_button.pack(pady=20)

second_window = tk.Toplevel(main_window)
second_window.title("second window")
second_window.geometry("500x500")
second_window.configure(bg="#3a5c23")
second_window.withdraw()

txt1 = tk.Label(second_window,text="second window", font=('times new roman', 20 , 'bold'),bg="#162f8a")
txt1.pack()

back_button = tk.Button(main_window, text="back to main Window",command=back_to_main_window)
back_button.pack(pady=20)

main_window.mainloop()



















