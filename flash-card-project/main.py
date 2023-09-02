import random
from tkinter import *

import pandas
from pandas import *

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = read_csv("data/word_to_learn.csv")

except FileNotFoundError:
    Original_data = read_csv("data/french_words.csv")
    to_learn = Original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(image, image=card_front_img)
    canvas.itemconfig(canvas_title, text="French", fill="black")
    canvas.itemconfig(canvas_word, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(image, image=card_back_image)
    canvas.itemconfig(canvas_title, text="English", fill="white")
    canvas.itemconfig(canvas_word, text=current_card["English"], fill="white")


def is_known():
    to_learn.remove(current_card)
    data = DataFrame(to_learn)
    data.to_csv("data/word_to_learn.csv", index=False)
    next_word()


window = Tk()
window.title("Flashy")
window.config(padx=20, pady=20, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
image = canvas.create_image(400, 263, image=card_front_img)
canvas_title = canvas.create_text(400, 150, text="", font=("Ariel,", 40, "italic"))
canvas_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_word)
unknown_button.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
known_button = Button(image=right_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

next_word()
window.mainloop()
