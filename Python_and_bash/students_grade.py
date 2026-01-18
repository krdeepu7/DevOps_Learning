students={}

while True:
    print("\nStudent Grade Management System"
          "\n1. Add Student"
          "\n2. Update Student Grade"
          "\n3. View Students"
          "\n4. Exit")
    choice = input("Choose an option (1-4): ")

    if choice == '1':
        name = input("Enter student name: ")
        grade = input("Enter student grade: ")
        students[name] = grade
        print(f"Student {name} added with grade {grade}.")  
    
    elif choice == '2':
        name = input("Enter student name to update: ")
        if name in students:
            grade = input("Enter new grade: ")
            students[name] = grade
            print(f"Student {name}'s grade updated to {grade}.")
        else:
            print(f"Student {name} not found.")
    
    elif choice == '3':
        if students:
            print("\nStudent Grades:")
            for name, grade in students.items():
                print(f"{name}: {grade}")
        else:
            print("No students found.")
    
    elif choice == '4':
        print("Exiting the program.")
        break   
    