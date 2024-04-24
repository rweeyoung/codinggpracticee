#this scripthas some error handling issues

import csv


first_input = None
second_input = None






class Trackertwo:
    def __init__(self, name):
        self.name =name
    def add_inflow(self, statement, how_much):
        with open(self.name, "a", newline ="") as file:
            filee = csv.DictWriter(file, fieldnames = ["statement", "how_much"])
            filee.writerow({"statement": statement, "how_much": how_much})
    def add_outflow(self, statement, how_much):
        with open(self.name, "a", newline ="") as file:
            filee = csv.DictWriter(file, fieldnames = ["statement", "how_much"])
            filee.writerow({"statement": statement, "how_much": -how_much})
    def display(self):
        with open(self.name, "r", newline ="") as file:
            temp_list = []
            filee = csv.DictReader(file)
            for i in filee:
                print(i)
    def total_balance(self):
        with open(self.name, "r", newline ="") as file:
            temp = 0
            filee = csv.DictReader(file)
            for i in filee:
                temp += float(i["how_much"])
            print(temp)
    def pathtwo(self):
        while True:
            second_input = input("press 1 to add inflow, press 2 to add outflow, press 3 to display, press 4 for total balance")
            try:
                second_input = int(second_input)
                if 1 > second_input or second_input > 4:
                    print("input number within range")
                    print("\n" * 3)
                    continue
            except ValueError:
                print("input a number")
                print("\n" * 3)
                continue
            else:
                if second_input == 1:
                    statement, how_much = input("what is the statement, how much(seperate with commas)").split(",")
                    how_much = float(how_much)
                    self.add_inflow(statement, how_much)
                    third_input = input("press 1 to exit, else will return")
                    third_input = int(third_input) # no error handling for now
                    if third_input == 1:
                        break 
                elif second_input == 2:
                    statement, how_much = input("what is the statement, how much(seperate with commas)").split(",")
                    how_much = float(how_much)
                    self.add_outflow(statement, how_much)
                    third_input = input("press 1 to exit, else will return")
                    third_input = int(third_input) # no error handling for now
                    if third_input == 1:
                        break 
                elif second_input == 3:
                    self.display()
                    third_input = input("press 1 to exit, else will return")
                    third_input = int(third_input) # no error handling for now
                    if third_input == 1:
                        break 
                elif second_input == 4:
                    self.total_balance()
                    third_input = input("press 1 to exit, else will return")
                    third_input = int(third_input) # no error handling for now
                    if third_input == 1:
                        break 
        return 0
        

class Tracker:
    def __init__(self, name):
        self.name =name
        intermm = str(self.name)
        with open(intermm , "w") as file:
            fileobject = csv.DictWriter(file, fieldnames = ["statement", "how_much"])
            fileobject.writeheader() 
    def add_inflow(self, statement, how_much):
        with open(self.name, "a", newline ="") as file:
            filee = csv.DictWriter(file, fieldnames = ["statement", "how_much"])
            filee.writerow({"statement": statement, "how_much": how_much})
    def add_outflow(self, statement, how_much):
        with open(self.name, "a", newline ="") as file:
            filee = csv.DictWriter(file, fieldnames = ["statement", "how_much"])
            filee.writerow({"statement": statement, "how_much": -how_much})
    def display(self):
        with open(self.name, "r", newline ="") as file:
            temp_list = []
            filee = csv.DictReader(file)
            for i in filee:
                print(i)
    def total_balance(self):
        with open(self.name, "r", newline ="") as file:
            temp = 0
            filee = csv.DictReader(file)
            for i in filee:
                temp += float(i["how_much"])
            print(temp)
    def pathtwo(self):
        while True:
            second_input = input("press 1 to add inflow, press 2 to add outflow, press 3 to display, press 4 for total balance")
            try:
                second_input = int(second_input)
                if 1 > second_input or second_input > 4:
                    print("input number within range")
                    print("\n" * 3)
                    continue
            except ValueError:
                print("input a number")
                print("\n" * 3)
                continue
            else:
                if second_input == 1:
                    statement, how_much = input("what is the statement, how much(seperate with commas)").split(",")
                    how_much = float(how_much)
                    self.add_inflow(statement, how_much)
                    third_input = input("press 1 to exit, else will return")
                    third_input = int(third_input) # no error handling for now
                    if third_input == 1:
                        break 
                elif second_input == 2:
                    statement, how_much = input("what is the statement, how much(seperate with commas)").split(",")
                    how_much = float(how_much)
                    self.add_outflow(statement, how_much)
                    third_input = input("press 1 to exit, else will return")
                    third_input = int(third_input) # no error handling for now
                    if third_input == 1:
                        break 
                elif second_input == 3:
                    self.display()
                    third_input = input("press 1 to exit, else will return")
                    third_input = int(third_input) # no error handling for now
                    if third_input == 1:
                        break 
                elif second_input == 4:
                    self.total_balance()
                    third_input = input("press 1 to exit, else will return")
                    third_input = int(third_input) # no error handling for now
                    if third_input == 1:
                        break 
        return 0
        










while True:
    first_input = input("press 1 to make new tracker, press 2 to access existing tracker, press 3 to exit")
    try:
        first_input = int(first_input)
        if 1 > first_input or first_input > 3:
            print("input number within range")
            print("\n" * 3)
            continue
    except ValueError:
        print("input a number")
        print("\n" * 3)
        continue
    else:
        break


if first_input == 1:
    print("making new tracker for you now")
    x = input("what is the new name of your file: ").lower().strip()
    new_tracker = Tracker(x)
    new_tracker.pathtwo()


if first_input == 2:
    y = input("what is the existing name of your file").lower().strip()
    ytracked = Trackertwo(y)
    ytracked.pathtwo()



print("program finished running ")


