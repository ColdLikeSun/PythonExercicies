fname = input("Enter file name: ")
if len(fname) < 1: fname = "mbox-short.txt"
fh = open(fname)
count = 0
lst = list()
y = list()
for line in fh:
    if line.startswith('From '):
        y = line.split()
        lst.append(y[1])
        count = count + 1

    else:
        continue

for email in lst:
    print(email)
print("There were", count, "lines in the file with From as the first word")
