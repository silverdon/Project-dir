import os
import shutil
import tkinter



window = tkinter.Tk()
window.title("Project Folder Creation")
window.minsize(width=400, height=300)

label = tkinter.Label(text="Enter the name of the new directory", font=("Arial", 14))
label.pack()
input = tkinter.Entry(width=20)
input.pack()



def create_dir(): 
    ifExists = True
#    print(os.listdir('./ΩBlank/'))
    ifExists = os.path.exists(input.get())
    if ifExists == False:
        shutil.copytree('./ΩBlank', input.get())
        print("dir created")   
    os.chdir(input.get())
    for file_name in os.listdir():
        if "Ω" in file_name:
            new_name = input.get() + file_name[6:]
            os.rename(file_name, new_name) 

button = tkinter.Button(text="Create Directory", command=create_dir)
button.pack()