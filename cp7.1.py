# Use words.txt as the file name
"""fname = input("Enter file name: ")"""

fh = open(r"C:\\Users\\Maryam Azimli\Desktop\\Coursera\\Python\\Data Structures\\cp7 assignments\\words.txt")

for line in fh:
    line=line.rstrip()
    print(line.upper())