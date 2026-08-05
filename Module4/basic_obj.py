a = [1,2,3,4,5]
b = ["apple", 1, "cherry", 2.5, True]

print("This is list", a)
print(a)
print("This is mixed list", b)
print(b)


print (b[2])
result = b[1:4]
print("Sliced list:", result)
b.append("banana")
print("List after appending:", b)
