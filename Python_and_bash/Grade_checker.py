marks = input("Enter your marks: ")

if int(marks) >= 90:
    print("Grade: A")
elif int(marks) >= 80:
    print("Grade: B")
elif int(marks) >= 70:
    print("Grade: C")
elif int(marks) >= 60:
    print("Grade: D")
else:
    print("Grade: F")