print("Hello World")

with open("to_read.txt", "a+") as to_read:
    to_read.seek(0)
    for line in to_read.readlines():
        print(line)
    to_read.write("\nI am Sharvari")