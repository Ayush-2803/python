#making a grade calculator
# Add student names and grades.
# Calculate the average grade of all students.
# Display the highest and lowest grades.
# List all students and their grades.
# Exit the program.

#function for adding students
def add_stu(students):
    name = input("Enter student name : ")
    try :
        grade = float(input("Enter grade (numeric value) : "))
    except ValueError:
        print("Enter correct numeric value")
    students[name] = grade
    print(f"Student {name} with grade {grade} added successfully")

def calc_average(students):
    if not students:
        print("No Student found")
    else :
        average = sum(students.values())/len(students)
        print(f"The average grade is {average: .2f}")
    
def min_max_grades(students):
    if not students:
        print("No Data Found")
    else :
        highest = max(students.values())
        lowest = min(students.values())
        print("Student with HIGHEST GRADE : ")
        for name , grade in students.items():
            if grade == highest:
                print(name)
        print("Student with LOWEST GRADE : ")
        for name , grade in students.items():
            if grade == lowest:
                print(name)

def list_stu(students):
    if not students:
        print("NO DATA FOUND !!!")
    else :
        for name , grade in students.items():
            print(f"{name} : {grade}")

def display_menu():
    """Displays the menu of operations."""
    print("\nStudent Grade Manager")
    print("1. Add Student")
    print("2. Calculate Average Grade")
    print("3. Display Highest and Lowest Grades")
    print("4. List All Students")
    print("5. Exit")

def grade_manager():
    students = {}
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")
        
        if choice == '5':
            print("Exiting the Grade Manager. Goodbye!")
            break
        elif choice == '1':
            add_stu(students)
        elif choice == '2':
            calc_average(students)
        elif choice == '3':
            min_max_grades(students)
        elif choice == '4':
            list_stu(students)
        else:
            print("Invalid choice! Please select a valid option.")

grade_manager()
