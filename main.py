from tkinter import *

window = Tk()

miles_input = Entry()
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

km_num_label = Label(text="0")
km_num_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate")
calculate_button.grid(column=1, row=2)


window.mainloop()
