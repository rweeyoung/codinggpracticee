class Draft:
    def __init__(self, user_second_input_name, user_second_input_description)
        self.user_second_input_name = user_second_input_name
        self.user_second_input_description = user_second_input_description
        with open(user_second_input_name, "w") as file:
             file.write("this is" + str"self.user_second_input_name)
        print("done created a new draft")
    def __repr__(self)
        return "{} is about {}".format(self.user_second_input_name, self.user_second_input_description)
    def error(self, user_second_input):
         try:
            user_second_input = int(user_second_input)
        except ValueError:
            return 5
        else:
            if 1 > user_second_input or user_second_input > 3:
                pass 
            return 5



         


    def append(self, amended_statement):
        listlol = []
        dictlol ={}
        x = str(self.user_second_input_name)
        with open(x, "r") as file:
            for i in file.readlines():
                listlol.append(i)
            for index, value in enumerate(listlol, start = 1):
                dictlol[index] = value
            print(str(amended_statement) + " will be slot in at index " + str(max(dictlol.keys(), default = 0) + 1))
        with open(x, "a") as file:
            file.write(f"\n{amended_statement}")

            

                
            

             
    def amend(self,variable_name, amended_statmentnumbers, amended_statment):
         listlol = []
        dictlol ={}
        listsecond = []
        x = str(self.user_second_input_name)
        with open(x, "r") as file:
            for i in file.readlines():
                listlol.append(i)
            for index, value in enumerate(listlol, start = 1):
                dictlol[index] = value
        for i in amended_statmentnumbers:
            if i in dictlol.keys():
            listsecond.append(i)
         with open(x, "w") as file:
            
         






    def delete(self,variable_name, amended_statmentnumbers)
  






user_first_input = None 

while True:
    user_first_input = input("press 1 to create new draft, \npress 2 to access existing draft\n press 3 to exit:")
    try:
        user_first_input = int(user_first_input)
    except ValueError:
        print("input numbers only")
        print("\n" * 3)
    else:
        if 1 > user_first_input or user_first_input > 3:
            print("between 1-3 only, inclusive")
            print("\n" * 3)
            continue
        else:
            break




if user_first_input == 1:
    user_second_input_name, user_second_input_description = = input("what is the name and description?(enter while serpated by comma)").split(",")
    user_second_input_name = user_second_input_name.strip()
    user_second_input_description = user_second_input_description.strip()
    user_draft = Draft(user_second_input_name, user_second_input_description)
        while user_second_input != 1
            user_second_input = input("to exit, press 1, else 2 for append newly created, else 3 for amend newly created, else 4 for to delete newly created")
            error =Draft.error(user_second_input)
            elif error == 2:
                Draft.append
            elif error == 3:
                Draft.amend
            elif error == 4:
                Draft.delete
    



elif user_first_input == 2:
            #insert
            while user_second_input != 1
                user_second_input = input("to exit, press 1, else 2 for append newly created, else 3 for amend newly created, else 4 for to delete newly created")
                error =Draft.error(user_second_input)
                elif error == 2:
                    #insert
                elif error == 3:
                    #insert
                elif error == 4:



print("exited, programe end")
                
            
            



else:
     return 0