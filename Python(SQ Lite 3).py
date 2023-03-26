1
import sqlite3 as sq

connection = sq.connect("database.db")
cursor = connection.cursor()

if cursor.execute("""SELECT name FROM sqlite_master WHERE type='table' AND name='Student';""").fetchall() == []:
    command = '''CREATE TABLE Student (Name char(50), Registor_number integer NOT NULL UNIQUE, Gender char(1), Age integer, Year integer, CGPA dec(5, 2), Marks integer)'''
    cursor.execute(command)
    print("Creating table.")  


def get_input(num, cursor):
    for i in range(num):
        name = input("\nEnter the name: ").capitalize()
        reg = int(input("Enter the register number: "))
        gender = input("Enter gender (M/F): ").capitalize()
        age = int(input("Enter the age: "))
        year = int(input("Enter the year: "))
        cgpa = float(input("Enter the CGPA: "))
        marks= sum(map(int, input("Enter the marks seperated by space: ").split()))

        command = f'''INSERT INTO Student (Name, Registor_number, Gender, Age, Year, CGPA, Marks) VALUES("{name}", "{reg}", "{gender}", "{age}", "{year}", "{cgpa}", "{marks}")'''
        cursor.execute(command)
    connection.commit()


def get_output(cursor, sort_by):
    cmd  = f'''SELECT * FROM Student ORDER BY {sort_by}'''
    data = cursor.execute(cmd).fetchall()
    return data


while True:
    print("\nChoose any option...\n1.Enter Student Data.\n2.Retrive Student Data.\n4.Quit")
    choice = int(input("=> "))

    if choice == 1:
        num = int(input("\nEnter the number of records: "))
        get_input(num, cursor)

    elif choice == 2:
        print("Enter your choice to sort by...\n1.Registor number.\n2.Name\n3.CGPA")
        req = int(input("=> "))
        if req == 1:
            data = get_output(cursor, "Registor_number")
        elif req == 2:
            data = get_output(cursor, "Name")
        elif req == 3:
            data = get_output(cursor, "CGPA")

        print("Name".ljust(17) + "Reg_no".ljust(6) + " G " + "Age" + " Year " + "CGPA " + " Marks")
        print("----------------------------------------------")
        for i in data:
            print(f"{i[0]:15}  {i[1]:#6} {i[2]:1} {i[3]:3} {i[4]: 4} {i[5]: 4} {i[6]: 3}")
    else:
        break

connection.close()
