import tkinter

window = tkinter.Tk()
window.title("Mile to km convertor")
window.config(padx=20,pady=20)

title = tkinter.Label(text="is equal to")
title.grid(row=0,column=0,rowspan=3)

milles = tkinter.Entry(width=15)
milles.grid(row=0,column=1)
miiles_label = tkinter.Label(text="Miles")
miiles_label.grid(row=0,column=2)

result = tkinter.Label(text="0")
result.grid(row=1,column=1)
km_label = tkinter.Label(text="Miles")
km_label.grid(row=1,column=2)

def convert():
    result.config(text=round(int(milles.get())*1.609344))

button = tkinter.Button(text="calculate" ,command=convert)
button.grid(row =2 , column=1)


# my_label = tkinter.Label(text="I am Label", font=("Arial", 24, "bold"))
# my_label.grid(row=0,column= 0)
#
# my_label.config(text="neww")
#
#
# def on_change():
#     my_label.config(text=input.get())
#
#
# button = tkinter.Button(text="click me", command=on_change)
# button.grid(row=1,column=1)
#
# input = tkinter.Entry(width=10)
# input.grid(row=2,column=2)
#
# new_button = tkinter.Button(text="click me also")
# new_button.grid(row=0,column=2)
#
#
window.mainloop()
