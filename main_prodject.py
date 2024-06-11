import sqlite3
#This line imports the sqlite database.
import time
#This line imports time, meaning I can pause the program for a second.
import os
#I will be using this line to clear the terminal, 

conn = sqlite3.connect('highschool_prodject.db')
#This line connects to the database.

cursor = conn.cursor()
#This makes the little flashing writey thing in the veiw, I dont know much about the top three lines.

def all_teachers():
    cursor.execute('SELECT * FROM teacher_table')
    teacher_table = cursor.fetchall()
    #These two lines of code type into the little flashy thing, with the thing being typed the statement in the cursor.execute
    #The line underneath takes the table outputted and assighns the data to the varible teacher_table.

    print('''████████ ███████  █████   ██████ ██   ██ ███████ ██████  ███████ 
    ██    ██      ██   ██ ██      ██   ██ ██      ██   ██ ██      
    ██    █████   ███████ ██      ███████ █████   ██████  ███████ 
    ██    ██      ██   ██ ██      ██   ██ ██      ██   ██      ██ 
    ██    ███████ ██   ██  ██████ ██   ██ ███████ ██   ██ ███████\n''')
    #This line prints teachers: as an intro to the data that is about to be displayed

    for information in teacher_table:
        if information[4] == 0:
            gender = "Male"
        else:
            gender = "Female"
        #In these five lines, the code makes a loop that will cycle through the list teacher_table, taking out each part of the 2d list and assigning it to a vatible.
        #The four next four lines checks if the gender is a 1 or a 0, 0 being male and 1 being female. It then assigns the gender to a varible called varible
        print(f"ID: {information[0]}: {information[1]} {information[2]}\nAge: {information[3]}\nGender: {gender}\nSubject: {information[5]}\
            \nYears of experience: {information[6]}\n")
        #using an f string, the code prints out all of the information in a formatted veiw.
        
        time.sleep(0.1)
        #Using time.sleep, the program will pause for the time in the brackets, in this case a tenth of a second, between teachers pronted out.
        #This helps the formatting of the whole program

def all_students():
    #I have tabbed all of the data and put it in a define statment so I can use it in a menu
    cursor.execute('SELECT * FROM student_table')
    student_table = cursor.fetchall()
    #This is the exactly same two lines from before except it gets all the data from the students table instead of the teachers.

    print('''\n
    ███████ ████████ ██    ██ ██████  ███████ ███    ██ ████████ ███████ 
    ██         ██    ██    ██ ██   ██ ██      ████   ██    ██    ██      
    ███████    ██    ██    ██ ██   ██ █████   ██ ██  ██    ██    ███████ 
         ██    ██    ██    ██ ██   ██ ██      ██  ██ ██    ██         ██ 
    ███████    ██     ██████  ██████  ███████ ██   ████    ██    ███████
                                                                        \n''')
    #Same thing as the teachers except theres a \n infront as well for formatting. 

    for information in student_table:
        if information[4] == 0:
            gender = "Male"
        elif information[4] == 1:
            gender = "Female"
        else:
            gender = "Non-binary"
        #This is the exactly same as before, and uses the same varibles as theyre disposable varibles and are reusable. The only real diffenect
        #Is how there is an elif statement in the code because of the third gender; non-binary.

        print(f"ID: {information[0]}\nName: {information[1]} {information[2]}\nGender: \
    {gender}\nAge: {information[3]}\nYear level: {information[5]}\nYear credits: {information[6]}\n")
        #much alike the other line used for the teachers, this line prints out the information in a formatted form.

        time.sleep(0.05)
        #same as the first time.sleep, this one causes a pause inbetween users for 0.05 seconds for formatting reasons.
        #The shorter time is there so the user isn't left waiting for too long.   

def student_menu():
    while True:
        os.system('cls')
        #like the first menu, this one uses while true and os.system('cls') to repeat cleanly unti the user is finished with the program

        print("""
███████ ████████ ██    ██ ██████  ███████ ███    ██ ████████     ███    ███ ███████ ███    ██ ██    ██ 
██         ██    ██    ██ ██   ██ ██      ████   ██    ██        ████  ████ ██      ████   ██ ██    ██ 
███████    ██    ██    ██ ██   ██ █████   ██ ██  ██    ██        ██ ████ ██ █████   ██ ██  ██ ██    ██ 
     ██    ██    ██    ██ ██   ██ ██      ██  ██ ██    ██        ██  ██  ██ ██      ██  ██ ██ ██    ██ 
███████    ██     ██████  ██████  ███████ ██   ████    ██        ██      ██ ███████ ██   ████  ██████  """)
        #another menu, this one used to represent the student menu

        user_input = input("\nPlease enter the number corrosponding to the year level you are searching for. EG (year 9, search 9)\n:")
        #this line takes the users inut and assigns it to the varible user_input.

        try:
            user_input = int(user_input)
        except ValueError:
            input("\nPlease ensure you are entering a year level on the range of 9 to 13\n(press enter to continue)")
            os.system('cls')
            continue
        #These lines try to convert the users input into an integer, and if it cant, it tells the user to try again and resets the program.
        #In short, it checks if the varible a number and restarts to the top of the menu if not.
        
        if user_input in range(9,14):
            #the if statment here checks if the number inside the user_input varible is in the range of 9 to 13, 14 is used as it dosent count the last number.
            #If the number is not in the range of 9 to 13, it gets skipped over to the else statment.

            cursor.execute('SELECT * FROM student_table WHERE Year_level = ?;', (user_input, ))
            student_table = cursor.fetchall()
            #These two lines get the data from the table and assigns it to the varible student table. 

            os.system('cls')
            #another clearing statment in prepearation for a new menu decal thingy.

            year_number = student_print(user_input)
            print(year_number)
            #this line takes the returned data from the define statment and assighns it to the varible year_number before printing it

            for information in student_table:
                if information[4] == 0:
                    gender = "Male"
                elif information[4] == 1:
                    gender = "Female"
                else:
                    gender = "Non-binary"
                print(f"ID: {information[0]}\nName: {information[1]} {information[2]}\nGender: {gender}\
                      \nAge: {information[3]}\nYear level: {information[5]}\nYear credits: {information[6]}\n")
                time.sleep(0.01)
            #these lines loop through each line, printing it in a formatted way.
            
            input("(Press enter to continue)")
            #This line stops the data put on screen from being immediately wiped from existance.
            os.system('cls')
            break
            #these two lines wipe the termilnal from existance and breaks, going back to the main menu
        else:
            input("\nPlease ensure you are entering a year level on the range of 9 to 13\n(press enter to continue)")
            os.system('cls')
            #these two lines tell the user they've done somthing wrong, wait for them to tell the program to proceed then clear the terminal, printing the student menu again

def student_print(user_input):

    if user_input == 9:
        year_level = """██    ██ ███████  █████  ██████       █████      ███████ ████████ ██    ██ ██████  ███████ ███    ██ ████████ ███████ 
 ██  ██  ██      ██   ██ ██   ██     ██   ██     ██         ██    ██    ██ ██   ██ ██      ████   ██    ██    ██      
  ████   █████   ███████ ██████       ██████     ███████    ██    ██    ██ ██   ██ █████   ██ ██  ██    ██    ███████ 
   ██    ██      ██   ██ ██   ██          ██          ██    ██    ██    ██ ██   ██ ██      ██  ██ ██    ██         ██ 
   ██    ███████ ██   ██ ██   ██      █████      ███████    ██     ██████  ██████  ███████ ██   ████    ██    ███████
    """
        return year_level
    elif user_input == 10:
        year_level = """██    ██ ███████  █████  ██████       ██  ██████      ███████ ████████ ██    ██ ██████  ███████ ███    ██ ████████ ███████ 
 ██  ██  ██      ██   ██ ██   ██     ███ ██  ████     ██         ██    ██    ██ ██   ██ ██      ████   ██    ██    ██      
  ████   █████   ███████ ██████       ██ ██ ██ ██     ███████    ██    ██    ██ ██   ██ █████   ██ ██  ██    ██    ███████ 
   ██    ██      ██   ██ ██   ██      ██ ████  ██          ██    ██    ██    ██ ██   ██ ██      ██  ██ ██    ██         ██ 
   ██    ███████ ██   ██ ██   ██      ██  ██████      ███████    ██     ██████  ██████  ███████ ██   ████    ██    ███████
   """
        return year_level
    elif user_input == 11:
        year_level = """██    ██ ███████  █████  ██████       ██  ██     ███████ ████████ ██    ██ ██████  ███████ ███    ██ ████████ ███████ 
 ██  ██  ██      ██   ██ ██   ██     ███ ███     ██         ██    ██    ██ ██   ██ ██      ████   ██    ██    ██      
  ████   █████   ███████ ██████       ██  ██     ███████    ██    ██    ██ ██   ██ █████   ██ ██  ██    ██    ███████ 
   ██    ██      ██   ██ ██   ██      ██  ██          ██    ██    ██    ██ ██   ██ ██      ██  ██ ██    ██         ██ 
   ██    ███████ ██   ██ ██   ██      ██  ██     ███████    ██     ██████  ██████  ███████ ██   ████    ██    ███████
   """
        return year_level
    elif user_input == 12:
        year_level = """██    ██ ███████  █████  ██████       ██ ██████      ███████ ████████ ██    ██ ██████  ███████ ███    ██ ████████ ███████ 
 ██  ██  ██      ██   ██ ██   ██     ███      ██     ██         ██    ██    ██ ██   ██ ██      ████   ██    ██    ██      
  ████   █████   ███████ ██████       ██  █████      ███████    ██    ██    ██ ██   ██ █████   ██ ██  ██    ██    ███████ 
   ██    ██      ██   ██ ██   ██      ██ ██               ██    ██    ██    ██ ██   ██ ██      ██  ██ ██    ██         ██ 
   ██    ███████ ██   ██ ██   ██      ██ ███████     ███████    ██     ██████  ██████  ███████ ██   ████    ██    ███████
   """
        return year_level
    else:
        year_level = """██    ██ ███████  █████  ██████       ██ ██████      ███████ ████████ ██    ██ ██████  ███████ ███    ██ ████████ ███████ 
 ██  ██  ██      ██   ██ ██   ██     ███      ██     ██         ██    ██    ██ ██   ██ ██      ████   ██    ██    ██      
  ████   █████   ███████ ██████       ██  █████      ███████    ██    ██    ██ ██   ██ █████   ██ ██  ██    ██    ███████ 
   ██    ██      ██   ██ ██   ██      ██      ██          ██    ██    ██    ██ ██   ██ ██      ██  ██ ██    ██         ██ 
   ██    ███████ ██   ██ ██   ██      ██ ██████      ███████    ██     ██████  ██████  ███████ ██   ████    ██    ███████
   """
        return year_level
    #what this whole thing does is take one argument which is set as user_input on the other end and checks which number it is on the scale from 9 - 13
    #It then takes that number and assigns another varible a menu decal accordingly using the return function.

def search():
    while True:
        print('''
███████ ███████  █████  ██████   ██████ ██   ██ 
██      ██      ██   ██ ██   ██ ██      ██   ██ 
███████ █████   ███████ ██████  ██      ███████ 
     ██ ██      ██   ██ ██   ██ ██      ██   ██ 
███████ ███████ ██   ██ ██   ██  ██████ ██   ██\n''')
        user_input = input("Please enter one option:\n1) Search students\n2) Search teachers\n3) Exit search\n:")
        try:
            user_input = int(user_input)
        except ValueError:
            input("\nPlease ensure you are entering a number on the range of 1 to 2.\n(press enter to continue)")
            os.system('cls')
            continue
        if user_input == 1:
            student_search()
        elif user_input == 2:
            teacher_search()
        elif user_input == 3:
            os.system('cls')
            break
        else:
            input("\nPlease ensure you are entering a number on the range of 1 to 3.\n(press enter to continue)")
            os.system('cls')

def student_search():

    user_choice = input("\nPlease enter one option:\n1) Search by ID\n2) Search by first name\n3) Search by last name\n:")
    try:
        user_choice = int(user_choice)
    except ValueError:
        input("Please ensure you are entering a number on a range of 1 to 3\n(Press enter to continue)")
        os.system('cls')
        return
    if user_choice == 1:
        query = "SELECT * FROM student_table WHERE ID = ?"
        user_search = input("\nEnter the ID you are searching for\n:")
        error = "There is no student ID in the database that matches "
    elif user_choice == 2:
        query = "SELECT * FROM student_table WHERE First_name = ?"
        user_search = input("\nPlease enter the first name you are searching for\n:")
        error = "There is no student first name in the database that matches "
    elif user_choice == 3:
        query = "SELECT * FROM student_table WHERE Last_name = ?"
        user_search = input("\nPlease enter the last name that you are searching for\n:")
        error = "There is no student last name in the database that matches "
    else:
        input("Please ensure you are entering a number on a range of 1 to 3\n(Press enter to continue)")
        os.system('cls')
        return
    user_search_cap = user_search.capitalize()
    cursor.execute(query, (user_search_cap, ))
    student_information = cursor.fetchall()
    if student_information == []:
       input(error + str(user_search) + "\n(Press enter to continue)")
       os.system('cls')
       return
    
    for information in student_information:
        if information[4] == 0:
            gender = "Male"
        elif information[4] == 1:
            gender = "Female"
        else:
            gender = "Non-binary"
        
        if information[6] <= 50:
            condition = "They have " +  str(information[6]) + " credits and isn't on track to pass the year."
        elif information[6] > 50 and information[6] < 80:
            condition = "They have " + str(information[6]) + " credits and are on track to pass this year."
        else:
            condition = "They have " + str(information[6]) + " credits and have passed the year."
        
        print(f"\nID: {information[0]}\n{information[1]} {information[2]} is {information[3]} years old in year {information[5]}.\nTheir gender is {gender}")
        print(condition)

        input("(press enter to continue)")
        os.system('cls')
        return

def teacher_search():
    user_choice = input("\nPlease enter one option:\n1) Search by ID\n2) Search by first name\n3) Search by last name\n:")
    try:
        user_choice = int(user_choice)
    except ValueError:
        input("Please ensure you are entering a number on a range of 1 to 3\n(Press enter to continue)")
        os.system('cls')
        return
    if user_choice == 1:
        query = "SELECT * FROM teacher_table WHERE ID = ?"
        user_search = input("\nEnter the ID you are searching for\n:")
        error = "There is no teacher ID in the database that matches "
        try:
            user_search = int(user_search)
        except ValueError:
            input("Please ensure you are entering an number ID\n(Press enter to continue)")
            os.system('cls')
            return
    elif user_choice == 2:
        query = "SELECT * FROM teacher_table WHERE First_name = ?"
        user_search = input("\nPlease enter the first name you are searching for\n:")
        error = "There is no teacher first name in the database that matches "
        user_search = user_search.capitalize()
    elif user_choice == 3:
        query = "SELECT * FROM teacher_table WHERE Last_name = ?"
        user_search = input("\nPlease enter the last name that you are searching for\n:")
        error = "There is no teacher last name in the database that matches "
        user_search = user_search.capitalize()
    else:
        input("Please ensure you are entering a number on a range of 1 to 3\n(Press enter to continue)")
        os.system('cls')
        return
    
    cursor.execute(query, (user_search, ))
    teacher_information = cursor.fetchall()
    print(teacher_information)

    if teacher_information == []:
       input(error + str(user_search) + "\n(Press enter to continue)")
       os.system('cls')
       return
    
    for information in teacher_information:
        if information[4] == 0:
            gender = "Male"
        else:
            gender = "Female"
        
        print(f"\nID: {information[0]}\n{information[1]} {information[2]} is {information[3]} years old and has worked {information[6]} years at this school.\nThey teach {information[5]} and their gender is {gender}")
        input("(press enter to continue)")
        os.system('cls')
        return


while True:
    print(''''
███    ███ ███████ ███    ██ ██    ██ 
████  ████ ██      ████   ██ ██    ██ 
██ ████ ██ █████   ██ ██  ██ ██    ██ 
██  ██  ██ ██      ██  ██ ██ ██    ██ 
██      ██ ███████ ██   ████  ██████\n''')
    #this is a menu print statment, it prints a menu sign.
    user_input = input("Please enter one option:\n1) Student menu\n2) Teacher menu\n3) Search\n4) Dump database (give all data)\n5) Quit program\n:")
    #this line takes the user input and assighns it to the varible user_input
    
    try:
        user_input = int(user_input)
    except ValueError:
        input("\nPlease ensure you are entering a number on the range of 1 to 5.\n(press enter to continue)")
        os.system('cls')
        continue
    #these few lines use try and except to check if the input is a number, it tries to convert the varible to a ineger and if it can't it tells the user and resets the menu.
    if user_input == 1:
        student_menu()
    #this line calls on the function stundent_menu
    elif user_input == 2:
        os.system('cls')
        all_teachers()
        #this line calles on the function all_teachers
        input("\n(Press enter to continue)")
        os.system('cls')
        #These two lines prepear to return the user to the menu, request for them to press enter when finished and then clears the terminal
    elif user_input == 3:
        os.system('cls')
        search()
    elif user_input == 4:
        os.system('cls')
        all_teachers()
        all_students()
        #this line clears the terminal of the menu then prints all the teachers, followed by all the students.
        input("\n(Press enter to continue)")
        os.system('cls') 
        #These two lines prepear to return the user to the menu, request for them to press enter when finished and then clears the terminal
    elif user_input == 5:
        print("\n Thanks for using the program!")
        time.sleep(1)
        os.system('cls')
        break
    #these lines check if the number is 5, then thank the user for using the program for a second before clearing the menu and breaking out of the while True loop
    else:
        input("\nPlease ensure you are entering a number on the range of 1 to 5.\n(press enter to continue)")
        os.system('cls')
        continue
    #these lines check if the number is on the range of 1 - 5 and uses a definition accordingly. if the number enterd isn't on one to five, the code tells the user and resets the menu. 