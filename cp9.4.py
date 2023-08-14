"""9.4 Write a program to read through the mbox-short.txt and figure out who has 
sent the greatest number of mail messages. The program looks for 'From ' lines and takes the 
second word of those lines as the person who sent the mail. The program creates a Python dictionary 
that maps the sender's mail address to a count of the number of times they appear in the file. After the 
dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer."""
""" name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
 """

handle= open(r"C:\\Users\\Maryam Azimli\Desktop\\Coursera\\Python\\Data Structures\\cp7 assignments\\mbox-short.txt")
dict=dict()

for lines in handle:
    if lines.startswith('From:'):
        words=lines.split()
        dict[words[1]]=dict.get(words[1],0)+1

largest=None
larword=None

for word,count in dict.items():
    if largest is None or count>largest:
        largest=count
        larword=word
print(larword,largest)