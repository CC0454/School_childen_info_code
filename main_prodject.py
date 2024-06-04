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

print("Teachers:")
for information in teacher_table:
    if information[4] == 0:
        gender = "Male"
    else:
        gender = "Female"
    print(f"Number {information[0]}: {information[1]} {information[2]}\nAge: {information[3]}\nGender: {gender}\nSubject: {information[5]}\
          \nYears of experience {information[6]}\n")

