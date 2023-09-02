from tkinter import *

# Create New Window
window = Tk()
window.title('My First GUI')
window.minsize(width=500, height=450)

# Create Label
my_label = Label(text="I am label", font=("Arial", 24, "bold"))
my_label.grid()


# my_label["text"] = "New Text"
# my_label.config(text='New Text')


def clickbutton():
    new_input = input.get()
    my_label.config(text=new_input)


# Create Button
button = Button(text='Click on', command=clickbutton)
button.grid()
# Entry
input = Entry(width=10)
input.grid()
print(input.get())

# Entries
entry = Entry(width=30)
# Add some text to being with
entry.insert(END, string="some text being with ")
print(entry.get())
entry.grid()

# Text

text = Text(height=5, width=30)
# Puts cursotr in textbox
text.focus()
# Adds some text to being with.
text.insert(END, "Example of multi-line text entry.")
# Get`s current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.grid()


# Spinbox
def spinbox_used():
    # gets the current value in spinbox.
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.grid()


# Scale
# Called with current scale value.

def scale_used(value):
    print(value)


scale = Scale(from_=0, to=100, command=scale_used)
scale.grid()


# CheckButton
def checkbutton_used():
    # Prints 1 if On button checked, otherwise 0.
    print(check_state.get())


# Variable to hold on to checked state, 0 is off, 1 is on .
check_state = IntVar()
checkbox = Checkbutton(text="Is On?", variable=check_state, command=checkbutton_used)
check_state.get()
checkbox.grid()


# Radiobutton
def radio_used():
    print(radio_state.get())


# Variable to hold on to which radio button value is checked
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.grid()
radiobutton2.grid()


# Listbox
def listbox_used(event):
    # Get current selection from listbox
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
fruit = ["Apple", "Pear", "Orange", "Banana"]
for item in fruit:
    listbox.insert(fruit.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.grid()

# button2 = Button(text="click on me")
# button2.grid(column=3,row=0)

window.mainloop()
