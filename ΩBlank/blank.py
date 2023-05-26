import os
import time
import re

os_path = os.getcwd()
path_list = (os_path.split("\\"))
cur_dir = path_list[-1]


for file_name in os.listdir():
    if "Ω" in file_name:
        print(file_name)
        new_name = cur_dir + file_name[6:]
        print(new_name)
        os.rename(file_name, new_name)
time.sleep(1)
