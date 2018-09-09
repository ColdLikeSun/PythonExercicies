name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
fh = open(name)
counts = dict()
words = list()
y = list()
for line in fh:
    if line.startswith('From '):
        y = line.split()[5].split(':')
        words.append(y[0])
    else:
        continue
for word in words:
    counts[word] = counts.get(word, 0) + 1
for k,v in sorted(counts.items()):
    print (k,v)