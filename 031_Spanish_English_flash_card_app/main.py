from tkinter  import *
BACKGROUND_COLOR = "#B1DDC6"
import pandas
import random
data_list = {}
dictionary_data = {}
#Creating a dictionary out of a csv file
try:
    data_frame = pandas.read_csv("./data/known_data.csv")
except FileNotFoundError:
    data_frame2 = pandas.read_csv("./data/Spanish_English.csv")
    data_frame2.to_csv("./data/known_data.csv", index= False)
    dictionary_data = data_frame2.to_dict(orient="records")
else:
    dictionary_data = data_frame.to_dict(orient= "records")
# print(dictionary_data)

#creating a button function
def click():
    global flip_timer,data_list,dictionary_data
    window.after_cancel(flip_timer)
    data_list = random.choice(dictionary_data)
    canvas_img.itemconfig(back_ground_image, image = photo_front)
    canvas_img.itemconfig(text_up, text = "Spanish")
    canvas_img.itemconfig(text_down, text = f"{data_list["Spanish"]}")
    #flip_timer = window.after(3000,change_cards)
    flip_timer = window.after(3500,change_cards)


#creating the function to change to the English card
def change_cards():
    global data_list
    canvas_img.itemconfig(back_ground_image, image = photo_back)
    canvas_img.itemconfig(text_up, text = "English")
    canvas_img.itemconfig(text_down, text = f"{data_list["English"]}")

#creating function to save the words not to be learned in a different csv file
def known_data():
    global data_list
    dictionary_data.remove(data_list)
    data = pandas.DataFrame(dictionary_data)
    data.to_csv("./data/known_data.csv", index = False)
    click()


#Creating a UI
window = Tk()
window.title("Card_flip")
window.config(bg=BACKGROUND_COLOR,padx=50, pady= 50)
flip_timer = window.after(3000,change_cards)

canvas_img = Canvas(height=526, width=800 )
photo_front = PhotoImage(file="./images/card_front.png")
photo_back = PhotoImage(file="./images/card_back.png")
back_ground_image = canvas_img.create_image(400,263,image = photo_front)
canvas_img.config(bg =BACKGROUND_COLOR, highlightthickness = 0)
text_up = canvas_img.create_text(400,120,text="",font=("Arial", 40, "italic"), fill="black")
text_down = canvas_img.create_text(400,290,text="",font=("Arial", 60, "bold"), fill="black")
canvas_img.grid(row = 0, column =0, columnspan = 2 )

photo_tick = PhotoImage(file="./images/right.png")
button_tick = Button(height= 50, width=50, image= photo_tick, bg= BACKGROUND_COLOR, highlightthickness= 10, command= known_data)
button_tick.grid(row=1 , column =0)

photo_wrong = PhotoImage(file="./images/wrong.png")
button_wrong = Button(height= 50, width=50,image= photo_wrong, bg= BACKGROUND_COLOR, highlightthickness= 10, command = click)
button_wrong.grid(row=1 , column =1)

click()
known_data()

window.mainloop()


