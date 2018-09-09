name = input("Enter file:")
if len(name) < 1: name = "mbox-short.txt"
fh = open(name)
counts = dict()
words = list()
y = list()
for line in fh:
    if line.startswith('From '):
        y = line.split()
        words.append(y[1])
    else:
        continue
for word in words:
    counts[word] = counts.get(word, 0) + 1
email = None
times = None

for word, count in counts.items():
    if times is None or count > times:
        email = word
        times = count
print(email, times)
