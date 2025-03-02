from tkinter import *
from tkinter import messagebox

game = Tk()
game.geometry("400x400")
game.title("Currency Converter")
game.config(bg="green")

def convert():
    amount = entry_amount.get()
    from_val = from_var.get()
    to_val = to_var.get()

    if not amount.isdigit():
        messagebox.showerror("Invalid input","Please enter a valid number")
        return
    
    exchange_rate = {
        ("EUR","USD"):1.18, ("EUR","GBP"):0.88, ("EUR","INR"):88.0,
        ("USD", "EUR"): 0.85, ("USD", "GBP"): 0.75, ("USD", "INR"): 74.5,
        ("GBP", "USD"): 1.33, ("GBP", "EUR"): 1.14, ("GBP", "INR"): 100.5,
        ("INR", "USD"): 0.013, ("INR", "EUR"): 0.011, ("INR", "GBP"): 0.0099
    }

    if (from_val,to_val) in exchange_rate:
        rate = exchange_rate[(from_val,to_val)]
        converted_amount = float(amount)*rate
        result_label.config(text= f"{amount} {from_val} = {converted_amount:.2f} {to_val}")
    else:
        messagebox.showerror("Error","Conversion rate not available")

amount_label = Label(game,text="Enter an Amount:",bg="black",fg="white").pack()
entry_amount = Entry(game)
entry_amount.pack()

currencies = ["USD", "EUR", "GBP", "INR"]

from_label = Label(game,text="From:")

from_var = StringVar(game)
from_var.set("EUR")
from_menu = OptionMenu(game,from_var,*currencies)
from_menu.pack()

to_label = Label(game,text="To:",bg="purple",fg="white")

to_var = StringVar(game)
to_var.set("USD")
to_menu = OptionMenu(game,to_var,*currencies)
to_menu.pack()

convert_btn = Button(game,text="Convert", command= convert)
convert_btn.pack()

result_label = Label(game,text="",bg="green",fg="black")
result_label.pack()

game.mainloop()
