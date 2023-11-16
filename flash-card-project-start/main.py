from tkinter import *
import pandas
import random

try:
    data = pandas.read_csv("data/words_to_learn.csv")
    row = None
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")

# ---------------------------- Change ------------------------------ #

def right():
    global data
    data = data.drop(row.name)
    random_generator()



def wrong():
    try:
        to_learn = pandas.read_csv("words_to_learn.csv")
    except FileNotFoundError:
        to_learn = pandas.DataFrame(row).T
    else:
        to_learn = to_learn.append(row)
    finally:
        to_learn.to_csv("./data/words_to_learn.csv", columns=["French", "English"])

    random_generator()



# ---------------------------- Change ------------------------------ #
def change(row):
    back_card = PhotoImage(file="./images/card_back.png")
    canvas.itemconfig(img, image=back_card)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=row["English"], fill="white")


# ---------------------------- Random generator------------------------------ #

def random_generator():
    global row
    row = data.loc[random.randint(0, len(data) - 1)]
    canvas.itemconfig(img, image=card)
    canvas.itemconfig(title, text='French', fill="black")
    canvas.itemconfig(word, text=row["French"], fill="black")
    print(row)
    canvas.after(3000, change, row)


# ---------------------------- UI SETUP ------------------------------- #

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card = PhotoImage(file="./images/card_front.png")
img = canvas.create_image(400, 263, image=card)
title = canvas.create_text(400, 150, text="French", font=('Ariel 40 italic'))
word = canvas.create_text(400, 263, text="Word", font=('Ariel 60 bold'))

canvas.grid(row=0, column=0, columnspan=2)

correct_img = PhotoImage(file="./images/right.png")
correctt_btn = Button(image=correct_img, highlightthickness=0, borderwidth=0, command=right)
correctt_btn.grid(row=1, column=0)

wrong_img = PhotoImage(file="./images/wrong.png")
wrong_btn = Button(image=wrong_img, highlightthickness=0, borderwidth=0, command=wrong)
wrong_btn.grid(row=1, column=1)

random_generator()

window.mainloop()
