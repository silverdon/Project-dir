import os
import shutil
from tkinter import *

window = Tk()
window.title("Project Folder Creation")
window.minsize(width=400, height=300)

label = Label(text="Enter the name of the new directory", font=("Arial", 14))
label.pack()
input = Entry(width=20)
input.pack()

def create_dir(): 
    ifExists = True
    ifExists = os.path.exists(input.get())
    if ifExists == False:
        shutil.copytree('./ΩBlank', input.get())
        print("dir created")   
    os.chdir(input.get())
    for file_name in os.listdir():
        if "Ω" in file_name:
            new_name = input.get() + file_name[6:]
            os.rename(file_name, new_name) 
#    if checked_state.get() == 1:
#        for i

button = Button(text="Create Directory", command=create_dir)
button.pack()

#Checkbutton
def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())
#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Create Device config directories?", variable=checked_state, command=checkbutton_used)
checked_state.get()
if checked_state.get() == 1:
    print("We are going to create dirs")
checkbutton.pack()

#Text
text = Text(height=10, width=30)
#Puts cursor in textbox.
text.focus()
#Adds some text to begin with.
text.insert(END, "One device per line")
#Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()

window.mainloop()
