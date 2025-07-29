#------------Printing Menu---------------
def show_menu():
    print("\n--- Student Progress Tracker ---")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Delete a Student")
    print("4. Exit")

# Add student and save to file function
def add_student():
    name = input("Enter student's name: ")

    # Ensuring the user enters a valid grade
    while True:
        try:
            grade = float(input("Enter student's grade: "))
            if grade < 0 or grade > 100:
                print("Please enter a grade between 0 and 100.")
            else:
                break
        except ValueError:
            print("Invalid input! Please enter a valid number for the grade.")
    
    # Save student info to a file
    with open('students.txt', 'a') as file:
        file.write(f"{name}, {grade}\n")
    print(f"Student {name} added successfully!")

# -----------------View students information--------------------
def view_students():
    try:
        with open('students.txt', 'r') as file:
            students = file.readlines()

        if not students:
            print("No students found.")
            return

        total_grade = 0
        highest_grade = float('-inf')
        lowest_grade = float('inf')
        count = len(students)

        print("\n--- Student List ---")
        for student in students:
            name, grade = student.strip().split(', ')
            grade = float(grade)
            total_grade += grade
            highest_grade = max(highest_grade, grade)
            lowest_grade = min(lowest_grade, grade)
            print(f"Name: {name}, Grade: {grade}")

        # Calculate average grade
        average_grade = total_grade / count
        print("\n--- Statistics ---")
        print(f"Average Grade: {average_grade:.2f}")
        print(f"Highest Grade: {highest_grade}")
        print(f"Lowest Grade: {lowest_grade}")
    
    except FileNotFoundError:
        print("No student records found. Please add some students first.")

#----------------Delete Student information----------------------
def delete_student():
    name_to_delete = input("Enter the name of the student to delete: ")
    
    try:
        # Read all lines from the file
        with open('students.txt', 'r') as file:
            students = file.readlines()

        # Check if the student exists
        student_found = False
        with open('students.txt', 'w') as file:
            for student in students:
                name, grade = student.strip().split(', ')
                if name.lower() != name_to_delete:
                    file.write(student)  # Write back all students except the one to delete
                else:
                    student_found = True

        if student_found:
            print(f"Student {name_to_delete} deleted successfully.")
        else:
            print(f"No student found with the name {name_to_delete}.")
    
    except FileNotFoundError:
        print("No student records found. Please add some students first.")

#-----------------main Funciton-----------------------
def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            delete_student()
        elif choice == '4':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")



main()
