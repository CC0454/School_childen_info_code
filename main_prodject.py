import sqlite3
#This line imports the sqlite database.
import time
#This line imports time, meaning I can pause the program for a second.

conn = sqlite3.connect('highschool_prodject.db')
#This line connects to the database.

cursor = conn.cursor()
#This makes the little flashing writey thing in the veiw, I dont know much about the top three lines.

cursor.execute('SELECT * FROM teacher_table')
teacher_table = cursor.fetchall()
#These two lines of code type into the little flashy thing, with the thing being typed the statement in the cursor.execute
#The line underneath takes the table outputted and assighns the data to the varible teacher_table.

print('''
████████╗███████╗░█████╗░░█████╗░██╗░░██╗███████╗██████╗░░██████╗██╗
╚══██╔══╝██╔════╝██╔══██╗██╔══██╗██║░░██║██╔════╝██╔══██╗██╔════╝╚═╝
░░░██║░░░█████╗░░███████║██║░░╚═╝███████║█████╗░░██████╔╝╚█████╗░░░░
░░░██║░░░██╔══╝░░██╔══██║██║░░██╗██╔══██║██╔══╝░░██╔══██╗░╚═══██╗░░░
░░░██║░░░███████╗██║░░██║╚█████╔╝██║░░██║███████╗██║░░██║██████╔╝██╗
░░░╚═╝░░░╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚═════╝░╚═╝''')
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

cursor.execute('SELECT * FROM student_table')
student_table = cursor.fetchall()
#This is the exactly same two lines from before except it gets all the data from the students table instead of the teachers.

print('''\n
░██████╗████████╗██╗░░░██╗██████╗░███████╗███╗░░██╗████████╗░██████╗██╗
██╔════╝╚══██╔══╝██║░░░██║██╔══██╗██╔════╝████╗░██║╚══██╔══╝██╔════╝╚═╝
╚█████╗░░░░██║░░░██║░░░██║██║░░██║█████╗░░██╔██╗██║░░░██║░░░╚█████╗░░░░
░╚═══██╗░░░██║░░░██║░░░██║██║░░██║██╔══╝░░██║╚████║░░░██║░░░░╚═══██╗░░░
██████╔╝░░░██║░░░╚██████╔╝██████╔╝███████╗██║░╚███║░░░██║░░░██████╔╝██╗
╚═════╝░░░░╚═╝░░░░╚═════╝░╚═════╝░╚══════╝╚═╝░░╚══╝░░░╚═╝░░░╚═════╝░╚═╝\n''')
#Same thing as the teachers except theres a \n for formatting. 

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




