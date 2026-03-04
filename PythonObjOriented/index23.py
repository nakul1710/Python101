#python writing files (.txt , .json , .csv)
# employees = ["Eugene", "squidward", "spoongbob", "patrick"]
# txt_data = "I like pizza!"

import csv

employee = [["Name", "Age", "job"],
            ["Spongbob", 30, "Cook"],
            ["Patrik", 37, "Unemployed"],
            ["Sandy" , 27, "Scientist"]]

file_path = "/Users/nakulyadav/Desktop/test.csv"


try:
    with open(file_path, "w") as file:
           # for employee in employees:
            #file.write(employee + "\n")
            #file.write(txt_data)
            # json.dump(employee, file, indent = 4)
            # print(f"txt file '{file_path}' was created")
        writer = csv.writer(file)
        writer.writerows(employee)
        print(f"csv file '{file_path}' was created")
except Exception as e:
    print(f"An error occurred: {e}")