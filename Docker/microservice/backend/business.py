def get_data():
    with open('a.txt') as f:
        names = f.read()

        names =names.split()
        
        return names

