import tkinter

window = tkinter.Tk()
window.title("First GUI")


user_entry = tkinter.Entry(width=10)
user_entry.grid(column=1,row=0,padx=5,pady=5)


miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=2,row=0,padx=5,pady=5)

isequal_label = tkinter.Label(text="Is equal to:")
isequal_label.grid(column=0,row=1,padx=5,pady=5)

result_label = tkinter.Label(text="0")
result_label.grid(column=1,row=1,padx=5,pady=5)

km_label = tkinter.Label(text="Km")
km_label.grid(column=2,row=1,padx=5,pady=5)

def calculate():
    result_label.config(text=f"{round(float(user_entry.get())*1.609344)}")
    

calculate_button = tkinter.Button(text="Calculate",command=calculate)
calculate_button.grid(column=1,row=2)





window.mainloop()