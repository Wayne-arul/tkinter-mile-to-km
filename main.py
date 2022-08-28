from tkinter import *

def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    kilometer_result_label.config(text=f"{km}")

window = Tk()
window.minsize(width=250, height=120)
window.title("Mile to Km Converter")
window.config(padx=40, pady=30)

miles_input = Entry(width=5)
miles_input.grid(row=0, column=1)

miles_label = Label(text='Miles')
miles_label.grid(row=0, column=2)

is_equal_label = Label(text='is equal to')
is_equal_label.grid(row=1, column=0)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(row=1, column=1)

kilometer_label = Label(text='Km')
kilometer_label.grid(row=1, column=2)

calculate_button = Button(text='Calculate', command=miles_to_km)
calculate_button.grid(row=2, column=1)




window.mainloop()

