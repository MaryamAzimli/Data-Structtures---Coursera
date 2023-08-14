"""10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below."""

""" name = input("Enter file:")s
if len(name) < 1:
    name = "mbox-short.txt" """

handle = open(r"C:\\mbox-short.txt")
dics=dict()
for lines in handle:
    if lines.startswith('From '):
        words=lines.split()
        d=words[5].split(':')
        dics[d[0]]=dics.get(d[0],0)+1

lst=list()
for k,v in dics.items():
    new=(k,v)
    lst.append(new)
tmp=sorted(lst)
for k,v in tmp:
    print(k,v)
