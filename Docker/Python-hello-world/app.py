print("Hello world DEVOPS PYTHON")

with open('a.txt') as f:
    names = f.read()

    names = names.split()


    for i,name in enumerate(names):
        print(f"{i+1}.{name}")
