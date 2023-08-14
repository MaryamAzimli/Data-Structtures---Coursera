# Use words.txt as the file name
"""fname = input("Enter file name: ")"""

fh = open(r"C:\\words.txt")

for line in fh:
    line=line.rstrip()
    print(line.upper())
