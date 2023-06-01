import os
import shutil
import tkinter

window = tkinter.Tk()
window.title("New Project Dir")
window.minsize(width=400, height=300)

my_label = tkinter.Label(text="i am a label")
my_label.pack(side="left")



# ifExists = True

# print(os.listdir('./ΩBlank/'))

# while ifExists == True:
#     dir_name = input("What is the new project name: ")
#     ifExists = os.path.exists(dir_name)
#     if ifExists == False:
#         shutil.copytree('./ΩBlank', dir_name)
#         print("dir created")
#     else:
#         print("Dir name exists")

# os.chdir(dir_name)

# for file_name in os.listdir():
#     if "Ω" in file_name:
#         new_name = dir_name + file_name[6:]
#         os.rename(file_name, new_name)    

# devices = True

# while devices == True:
#     dev_name = input("Enter a device name or exit when done: ")
#     if dev_name == "exit" or dev_name == e:
#         break
#     os.mkdir(dev_name)
#     os.chdir(dev_name)
#     with open(dev_name + '-MOP.txt', 'w') as fp:
#         pass
#     with open(dev_name + '-Original.txt', 'w') as fp:
#         pass
#     with open(dev_name + '-Rollback.txt', 'w') as fp:
#         pass
#     os.chdir("../")



window.mainloop()    
