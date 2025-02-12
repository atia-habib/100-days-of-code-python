from tkinter import *
from tkinter import messagebox
import pandas
import random
import time

current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:  
    original_data = pandas.read_csv("french_words.csv") 
    to_learn = original_data.to_dict(orient = "records") 
else:    
    to_learn = data.to_dict(orient="records")


BACKGROUND_COLOR = "#B1DDC6"


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=front_image)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=back_image)


def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


flip_timer = window.after(3000, func=flip_card)


canvas = Canvas(width=800, height=526)
front_image = PhotoImage(file="card_front.png")
back_image = PhotoImage(file="card_back.png")
card_background = canvas.create_image(400, 263, image=front_image)
card_title = canvas.create_text(400, 150, text="Title", font=["Ariel", 40, "italic"])
card_word = canvas.create_text(400, 263, text="Word", font=["Ariel", 60, "bold"])
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

cross_image = PhotoImage(file="wrong.png")
unknown_button = Button(image=cross_image, command=next_card)
unknown_button.grid(column=0, row=1)
unknown_button.config(bg=BACKGROUND_COLOR, highlightthickness=0)

check_image = PhotoImage(file="right.png")
known_button = Button(image=check_image, command=is_known)
known_button.grid(column=1, row=1)
unknown_button.config(bg=BACKGROUND_COLOR, highlightthickness=0)

next_card()

window.mainloop()
