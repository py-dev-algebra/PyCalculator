import tkinter as tk


# TODO sto ako kliknemo vise operacija? - uzimamo zadnju operaciju koja je kliknuta
# TODO kombiniranje vise operacija - 2 + 3 / 4 - 9


def insert_one():
    pass
def insert_two():
    pass
def insert_three():
    pass
def insert_add():
    pass
def insert_four():
    pass
def insert_five():
    pass
def insert_six():
    pass
def insert_substract():
    pass
def insert_seven():
    pass
def insert_eight():
    pass
def insert_nine():
    pass
def insert_multiply():
    pass
def cancel():
    pass
def insert_zero():
    pass
def calculate():
    pass
def insert_division():
    pass



main_window = tk.Tk()
main_window.title('Python Calculator')
#main_window.geometry('600x400')

main_window.columnconfigure((0, 1, 2, 3), minsize=75)
main_window.rowconfigure(0, minsize=100)
main_window.rowconfigure((1, 2, 3, 4), minsize=75)

# PROSTOR ZA WIDGETS
lbl_display = tk.Label(main_window,
                       text='Prikaz rezultata',
                       font=('Segoe UI', 20)).grid(row=0, column=0, columnspan=4)

btn_one = tk.Button(main_window,
                    text='1',
                    font=('Segoe UI', 12),
                    command=insert_one).grid(column=0, row=1, sticky='NESW')
btn_two = tk.Button(main_window,
                    text='2',
                    font=('Segoe UI', 12),
                    command=insert_two).grid(column=1, row=1, sticky='NESW')
btn_three = tk.Button(main_window,
                    text='3',
                    font=('Segoe UI', 12),
                    command=insert_three).grid(column=2, row=1, sticky='NESW')
btn_add = tk.Button(main_window,
                    text='+',
                    font=('Segoe UI', 12),
                    command=insert_add).grid(column=3, row=1, sticky='NESW')
btn_four = tk.Button(main_window,
                    text='4',
                    font=('Segoe UI', 12),
                    command=insert_four).grid(column=0, row=2, sticky='NESW')
btn_five = tk.Button(main_window,
                    text='5',
                    font=('Segoe UI', 12),
                    command=insert_five).grid(column=1, row=2, sticky='NESW')
btn_six = tk.Button(main_window,
                    text='6',
                    font=('Segoe UI', 12),
                    command=insert_six).grid(column=2, row=2, sticky='NESW')
btn_substract = tk.Button(main_window,
                    text='-',
                    font=('Segoe UI', 12),
                    command=insert_substract).grid(column=3, row=2, sticky='NESW')
btn_seven = tk.Button(main_window,
                    text='7',
                    font=('Segoe UI', 12),
                    command=insert_seven).grid(column=0, row=3, sticky='NESW')
btn_eight = tk.Button(main_window,
                    text='8',
                    font=('Segoe UI', 12),
                    command=insert_eight).grid(column=1, row=3, sticky='NESW')
btn_nine = tk.Button(main_window,
                    text='9',
                    font=('Segoe UI', 12),
                    command=insert_nine).grid(column=2, row=3, sticky='NESW')
btn_multiply = tk.Button(main_window,
                    text='*',
                    font=('Segoe UI', 12),
                    command=insert_multiply).grid(column=3, row=3, sticky='NESW')
btn_cancel = tk.Button(main_window,
                    text='C',
                    font=('Segoe UI', 12),
                    command=cancel).grid(column=0, row=4, sticky='NESW')
btn_zero = tk.Button(main_window,
                    text='0',
                    font=('Segoe UI', 12),
                    command=insert_zero).grid(column=1, row=4, sticky='NESW')
btn_calculate = tk.Button(main_window,
                    text='=',
                    font=('Segoe UI', 12),
                    command=calculate).grid(column=2, row=4, sticky='NESW')
btn_division = tk.Button(main_window,
                    text='/',
                    font=('Segoe UI', 12),
                    command=insert_division).grid(column=3, row=4, sticky='NESW')




main_window.mainloop()
