#Python file detection

import os
file_path = "/Users/nakulyadav/Desktop/test.txt"

if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")
    if os.path.isfile(file_path): 
        print("This is a file")
    else:
        print("This is a directory")
else:
    print("That location doesn't exist")  