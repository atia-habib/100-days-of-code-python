from tkinter import *

# Initialize window
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=150)
window.config(padx=5, pady=5)

# Input field
input = Entry(width=10)
input.grid(column=1, row=0)


# Labels
label_miles = Label(text="Miles")
label_miles.grid(column=2, row=0)

label_equal = Label(text="is equal to")
label_equal.grid(column=0, row=1)

label_km = Label(text="0")
label_km.grid(column=1, row=1)

label_km_unit = Label(text="Km")
label_km_unit.grid(column=2, row=1)


# Button click event
def miles_to_km():
    # Get value from input and convert to float
    miles = float(input.get())
    # Convert miles to kilometers
    kilometers = miles * 1.60934
    # Update the label to display the result
    label_km.config(text=f"{kilometers:.2f}")


# Button
button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)

# Run the GUI loop
window.mainloop()
