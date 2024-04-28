from tkinter import *
def display_msg():
    name=e1.get()
    hello_lable.config(text=f"Hello, {name}")

root=Tk()
root.title("Nisha's App")
l1=Label(root,text="User name")
l1.grid(row=0,column=0,padx=10,pady=10)
e1=Entry(root)  # entery used for text box display
e1.grid(row=0,column=1,padx=10,pady=10)
hello_lable=Label(root,text="")


hello_lable.grid(row=2,column=0,padx=10,pady=10)
b1=Button(root,text="Submit",command=display_msg)
b1.grid(row=1, column=0,padx=10,pady=10)
root.mainloop()
