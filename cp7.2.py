""" 7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce 
an output as shown below. Do not use the sum() function or a variable named sum in your solution.
You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.
 """
""" fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print('File cannot be open: ', fname) """
fh= open(r"C:\\Users\\Maryam Azimli\Desktop\\Coursera\\Python\\Data Structures\\cp7 assignments\\mbox-short.txt")
count=0
toplama=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count+=1
    c=line.find(':')
    d=line[c+1:].strip()
    e=float(d)
    toplama+=e
    
aver=float(toplama/count)
print("Average spam confidence:", aver)
