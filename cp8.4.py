"""8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in python sort() order as shown in the desired output.
You can download the sample data at http://www.py4e.com/code3/romeo.txt"""

"""fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print('File cannot be open: ', fname)
    quit() """
fh =open(r"C:\\Users\\Maryam Azimli\Desktop\\Coursera\\Python\\Data Structures\\cp8 assignments\\romeo.txt")
lst = list()
for line in fh:
    v=line.split()
    for word in v:
        if word in lst:
            continue
        lst.append(word)
lst.sort()
print(lst)