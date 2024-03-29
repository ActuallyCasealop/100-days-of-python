from tkinter import *
from tkinter import messagebox
import random
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_entry.delete(0,END)

    pw_gen_letters = [random.choice(letters) for letter in range(random.randint(8,10))]
    pw_gen_numbers = [random.choice(numbers) for number in range(random.randint(2,4))]
    pw_gen_symbols = [random.choice(symbols) for symbol in range (random.randint(2,4))]

    password_list = pw_gen_letters + pw_gen_numbers + pw_gen_symbols
    random.shuffle(password_list)
    password = "".join(password_list)
    
    password_entry.insert(0,password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get().lower()
    username = username_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
            "username":username,
            "password":password,
        }
    }

    if len(website) < 1 or len(password) < 1 or len(username) < 1:
        messagebox.showerror(title="Error",message="The following field might be empty:\nWebsite\nUsername\nPassword")
    else:    
        popup_resonse = messagebox.askokcancel(title=website,message=f"Are the following information correct?\nUsername: {username}\nPassword: {password}")
        if popup_resonse:
                try:
                    with open(r"Day 29 - Building a Password Manager GUI App with Tkinter\passwords.json","r") as pwd:
                        data = json.load(pwd)
                
                except FileNotFoundError:
                    with open(r"Day 29 - Building a Password Manager GUI App with Tkinter\passwords.json","w") as pwd:
                        json.dump(new_data, pwd, indent=4)
                
                else:
                    if website_entry.get().lower() in data:
                         warning_response = messagebox.askokcancel(title="Warning",message="Entry already exist; said entry will instead be replaced with the new one. continue?")
                         if warning_response:
                            data.update(new_data)
                            with open(r"Day 29 - Building a Password Manager GUI App with Tkinter\passwords.json","w") as pwd:
                                json.dump(data, pwd, indent=4)
                finally:
                    website_entry.delete(0,END)
                    password_entry.delete(0,END)

def find_website():
    try:
        with open (file=r"Day 29 - Building a Password Manager GUI App with Tkinter\passwords.json") as data:
            data_base = json.load(data)
    except FileNotFoundError:
            messagebox.showerror(title="ERROR",message="Repository is empty. Please add NTLOGIN to the repository.")
    else:
        website = website_entry.get().lower()
        if website in data_base:
             data_result = data_base[website]
             messagebox.showinfo(title=website.title(),message=f"Username: {data_result['username']}\nPassword: {data_result['password']}")
        else:
             messagebox.showerror(title="ERROR",message="Entry does not exist in the repository, consider saving one first.")

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
website_lb.grid(column=0,row=1,sticky="EW")

username_lb = Label(text="Email/Username:")
username_lb.grid(column=0,row=2,sticky="EW")

password_lb = Label(text="Password")
password_lb.grid(column=0,row=3,sticky="EW")
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
find_button = Button(text="Find Website", command=find_website)
find_button.grid(column=2,row=1,sticky="EW")

generate_button = Button(text="Generate Password",command=password_generator)
generate_button.grid(column=2,row=3,sticky="EW")

add_button = Button(text="Add",width=36,command=save_password)
add_button.grid(column=1,row=4,columnspan=2,sticky="EW")


window.mainloop()