fname = input("Enter file name: ")
fh = open(fname)
lst = list()
x = list()
for line in fh:
    line.rstrip()
    if not len:
        lst = line.split()

    else:
        x = line.split()
        for word in x:
            if word in lst:
                continue
            else:
                lst.append(word)
print(sorted(lst))