print("Hi, Enter your age:")

age = int(input("Hi, Enter your age:\n"))

if int(age) < 18:
    print("You are a minor.")
else:
    print("You are an adult.")  

print(type(age))