from tkinter import *

window = Tk()
window.title("Mile to Kilometer Converter")
window.config(padx=20, pady=20)


# TODO: calculate the conversion
def converter():
    km = round(float(measure.get()) * 1.609)
    results_text.config(text=km)


# TODO: Entry field for miles input
measure = Entry(width=7)
measure.insert(END, string='0')
measure.grid(column=1, row=0)

# TODO: Miles text
miles_text = Label(text="Miles")
miles_text.grid(column=2, row=0)

# TODO: is equal to text
equal_text = Label(text="is equal to")
equal_text.grid(column=0, row=1)

# TODO: result
results_text = Label(text=0)
results_text.grid(column=1, row=1)

# TODO: km text
miles_text = Label(text="Km")
miles_text.grid(column=2, row=1)

# TODO: calculate button - middle quadrant
button = Button(text="Calculate", command=converter)
button.grid(column=1, row=2)

window.mainloop()
