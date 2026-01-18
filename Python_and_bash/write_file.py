import os

if not os.path.exists("sample_output.txt"):
    open("sample_output.txt", "w").close()

data = open("sample_output.txt", "r+")
data.write("This is first line\n")
data.write("This is second line\n")
data.write("This is third line\n")
data.close()    



