#write data to a file
f = open("data.txt", "w")
f.write("Hello Python\n")
f.write("This is file handling")
f.close()
#read data from a file
f = open("data.txt", "r")
content = f.read()
print(content)
f.close()
#append data to a file
f = open("data.txt", "a")
f.write("\nAppending new line to the file.")
f.close()
#using 'with' statement for file handling
with open("data.txt", "r") as f:
    print(f.read())
    