f = open("data.txt", "r+")

content = f.read()
print(content)

#Write to file
f.write("\nNew line added.")

f.close()

print(content)
