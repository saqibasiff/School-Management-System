students = []

def entry():
    name = str(input("\nEnter Student's Name = "))
    students.append(name)
    print("\nThe Student's Name is Added In The List!")

def display():
    if students:    
        print(f"The List Of Students Is :\n{students}")
    else:
        print("Thanks For Coming!")

def delete():
    if students:
            students.clear()
            print("Your Student's List Has Been Deleted!")
    else:
            print("No Students To Delete!")

def search():
        print("Do You Want To Search For Students")
        print("1. Search")
        print("2. No ")
        choice4 = int(input("Enter Your Choice = "))
        student_name = str(input("Enter Student's Name To Search = "))

        if student_name in students:
            print(f"This Student's Name {student_name} Is Present In Student's List!")


def update():
        print('''
        Do You Want To Update Student's List ?
         1. Yes
         2. No
''')
        choice5 = int(input("Enter Your Choice = "))

        if choice5 == 1 :
            add = str(input("Enter The Name You Want To Add = "))
        else:
             print("Student cannot be added.")
        
        students.append(add)

print('''
            Welcome To School Management!
                What Do You Want To Select :
            1. Student Entry
            2. Display Students
            3. Delete List
            4. Search List
            5. Update List 
        ''')
                             
select_choice = int(input("Enter Choice = "))

if select_choice == 1:
     entry()

elif select_choice == 2:
     display()

elif select_choice == 3:
     delete()

elif select_choice == 4:
     search()

elif select_choice == 5:
     update()

print(students)

