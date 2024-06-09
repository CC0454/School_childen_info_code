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
            \nYears of experience {information[6]}\n")
        #using an f string, the code prints out all of the information in a formatted veiw.
        
        time.sleep(0.1)
        #Using time.sleep, the program will pause for the time in the brackets, in this case a tenth of a second, between teachers pronted out.
        #This helps the formatting of the whole program

def all_students():
    #I have tabbed all of the data and put it in a define statment so I can use it in a menu
    cursor.execute('SELECT * FROM student_table')
    student_table = cursor.fetchall()
    #This is the exactly same two lines from before except it gets all the data from the students table instead of the teachers.

    print('''\n███████ ████████ ██    ██ ██████  ███████ ███    ██ ████████ ███████ 
    ██         ██    ██    ██ ██   ██ ██      ████   ██    ██    ██      
    ███████    ██    ██    ██ ██   ██ █████   ██ ██  ██    ██    ███████ 
        ██    ██    ██    ██ ██   ██ ██      ██  ██ ██    ██         ██ 
    ███████    ██     ██████  ██████  ███████ ██   ████    ██    ████████
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
        print("""
███████ ████████ ██    ██ ██████  ███████ ███    ██ ████████     ███    ███ ███████ ███    ██ ██    ██ 
██         ██    ██    ██ ██   ██ ██      ████   ██    ██        ████  ████ ██      ████   ██ ██    ██ 
███████    ██    ██    ██ ██   ██ █████   ██ ██  ██    ██        ██ ████ ██ █████   ██ ██  ██ ██    ██ 
     ██    ██    ██    ██ ██   ██ ██      ██  ██ ██    ██        ██  ██  ██ ██      ██  ██ ██ ██    ██ 
███████    ██     ██████  ██████  ███████ ██   ████    ██        ██      ██ ███████ ██   ████  ██████  """)
        
        user_input = input("Please enter the number corrosponding to the year level you are searching for. EG (year 9, search 9)\n:")
        
        try:
            user_input = int(user_input)
        except ValueError:
            input("\nPlease ensure you are entering a year level on the range of 9 to 13\n(press enter to continue)")
            os.system('cls')
            continue
        if user_input in range(9,14):
            os.system('cls')
            cursor.execute('SELECT * FROM student_table WHERE Year_level = ?;', (user_input, ))
            student_table = cursor.fetchall()
            year_number = student_print(user_input)
            print(year_number)
            for information in student_table:
                if information[4] == 0:
                    gender = "Male"
                elif information[4] == 1:
                    gender = "Female"
                else:
                    gender = "Non-binary"
                print(f"ID: {information[0]}\nName: {information[1]} {information[2]}\nGender: {gender}\
                      \nAge: {information[3]}\nYear level: {information[5]}\nYear credits: {information[6]}\n")
            input("(Press enter to continue)")
            os.system('cls')
            break
            

        else:
            print("poo")

def student_print(user_input):
    if user_input == 9:
        year_level = """██    ██ ███████  █████  ██████       █████      ███████ ████████ ██    ██ ██████  ███████ ███    ██ ████████ ███████ 
 ██  ██  ██      ██   ██ ██   ██     ██   ██     ██         ██    ██    ██ ██   ██ ██      ████   ██    ██    ██      
  ████   █████   ███████ ██████       ██████     ███████    ██    ██    ██ ██   ██ █████   ██ ██  ██    ██    ███████ 
   ██    ██      ██   ██ ██   ██          ██          ██    ██    ██    ██ ██   ██ ██      ██  ██ ██    ██         ██ 
   ██    ███████ ██   ██ ██   ██      █████      ███████    ██     ██████  ██████  ███████ ██   ████    ██    ███████ """
        return year_level
    elif user_input == 10:
        year_level = """██    ██ ███████  █████  ██████       ██  ██████      ███████ ████████ ██    ██ ██████  ███████ ███    ██ ████████ ███████ 
 ██  ██  ██      ██   ██ ██   ██     ███ ██  ████     ██         ██    ██    ██ ██   ██ ██      ████   ██    ██    ██      
  ████   █████   ███████ ██████       ██ ██ ██ ██     ███████    ██    ██    ██ ██   ██ █████   ██ ██  ██    ██    ███████ 
   ██    ██      ██   ██ ██   ██      ██ ████  ██          ██    ██    ██    ██ ██   ██ ██      ██  ██ ██    ██         ██ 
   ██    ███████ ██   ██ ██   ██      ██  ██████      ███████    ██     ██████  ██████  ███████ ██   ████    ██    ███████"""
        return year_level
    elif user_input == 11:
        year_level = """██    ██ ███████  █████  ██████       ██  ██     ███████ ████████ ██    ██ ██████  ███████ ███    ██ ████████ ███████ 
 ██  ██  ██      ██   ██ ██   ██     ███ ███     ██         ██    ██    ██ ██   ██ ██      ████   ██    ██    ██      
  ████   █████   ███████ ██████       ██  ██     ███████    ██    ██    ██ ██   ██ █████   ██ ██  ██    ██    ███████ 
   ██    ██      ██   ██ ██   ██      ██  ██          ██    ██    ██    ██ ██   ██ ██      ██  ██ ██    ██         ██ 
   ██    ███████ ██   ██ ██   ██      ██  ██     ███████    ██     ██████  ██████  ███████ ██   ████    ██    ███████"""
        return year_level
    elif user_input == 12:
        year_level = """██    ██ ███████  █████  ██████       ██ ██████      ███████ ████████ ██    ██ ██████  ███████ ███    ██ ████████ ███████ 
 ██  ██  ██      ██   ██ ██   ██     ███      ██     ██         ██    ██    ██ ██   ██ ██      ████   ██    ██    ██      
  ████   █████   ███████ ██████       ██  █████      ███████    ██    ██    ██ ██   ██ █████   ██ ██  ██    ██    ███████ 
   ██    ██      ██   ██ ██   ██      ██ ██               ██    ██    ██    ██ ██   ██ ██      ██  ██ ██    ██         ██ 
   ██    ███████ ██   ██ ██   ██      ██ ███████     ███████    ██     ██████  ██████  ███████ ██   ████    ██    ███████"""
        return year_level
    else:
        year_level = """██    ██ ███████  █████  ██████       ██ ██████      ███████ ████████ ██    ██ ██████  ███████ ███    ██ ████████ ███████ 
 ██  ██  ██      ██   ██ ██   ██     ███      ██     ██         ██    ██    ██ ██   ██ ██      ████   ██    ██    ██      
  ████   █████   ███████ ██████       ██  █████      ███████    ██    ██    ██ ██   ██ █████   ██ ██  ██    ██    ███████ 
   ██    ██      ██   ██ ██   ██      ██      ██          ██    ██    ██    ██ ██   ██ ██      ██  ██ ██    ██         ██ 
   ██    ███████ ██   ██ ██   ██      ██ ██████      ███████    ██     ██████  ██████  ███████ ██   ████    ██    ███████"""
        return year_level
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
    elif user_input == 2:
        pass
    elif user_input == 3:
        pass
    elif user_input == 4:
        pass
    elif user_input == 5:
        print("\n Thanks for using the program!")
        time.sleep(1)
        os.system('cls')
        break
    else:
        input("\nPlease ensure you are entering a number on the range of 1 to 5.\n(press enter to continue)")
        os.system('cls')
        continue
    #these lines check if the number is on the range of 1 - 5 and uses a definition accordingly. if the number enterd isn't on one to five, the code tells the user and resets the menu. 