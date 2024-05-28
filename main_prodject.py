import sqlite3
#This line imports the sqlite database.
conn = sqlite3.connect('highschool_prodject.db')
#This line connects to the database.
cursor = conn.cursor()
#This makes the little flashing writey thing, I dont know much about the top three lines.
cursor.execute('SELECT * FROM student_table')
#This line uses a SQlite sequence and takes the data and puts it in a list.
main_list = cursor.fetchall()
#This line gets the list and assigns it to a varible.
print(main_list)
#This line prints the varible.

