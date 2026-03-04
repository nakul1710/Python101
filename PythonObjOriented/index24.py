#Python reading files (.txt, .json, .csv)
import csv



file_path = "/Users/nakulyadav/Desktop/test.csv"
try:
    with open(file_path, "r") as file:
        #content = file.read(file)
        #content = json.load(file)
        content = csv.reader(file)
        for line in content:
            print(line)
        print(content)
except FileNotFoundError:
    print("That file not found")
except PermissionError:
    print("You don't have permission to read the file")

