from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    with open(r"Day 29 - Building a Password Manager GUI App with Tkinter\passwords.txt","a+") as pwd:
        pwd.write(f"{website_entry.get()} | {username_entry.get()} | {password_entry.get()}\n")
        website_entry.delete(0,END)
        password_entry.delete(0,END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)

canvas = Canvas(width=200,height=200)
logo_img = PhotoImage(file=r"Day 29 - Building a Password Manager GUI App with Tkinter\logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(column=1,row=0)
# ---------------------------- LABELS ------------------------------- #
website_lb = Label(text="Website:")
website_lb.grid(column=0,row=1)

username_lb = Label(text="Email/Username:")
username_lb.grid(column=0,row=2)

password_lb = Label(text="Password")
password_lb.grid(column=0,row=3)
# ---------------------------- ENTRIES ------------------------------- #
website_entry = Entry(width=36)
website_entry.grid(column=1,row=1,columnspan=2,sticky="EW")
website_entry.focus()

username_entry = Entry(width=36)
username_entry.grid(column=1,row=2,columnspan=2,sticky="EW")
username_entry.insert(0,"deepfreezer92@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(column=1,row=3,sticky="EW")
# ---------------------------- BUTTONS ------------------------------- #
generate_button = Button(text="Generate Password")
generate_button.grid(column=2,row=3)

add_button = Button(text="Add",width=36,command=save_password)
add_button.grid(column=1,row=4,columnspan=2,sticky="EW")


window.mainloop()