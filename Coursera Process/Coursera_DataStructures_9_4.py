handle = open("mbox-short.txt")
counter = {}
for line in handle:
    if line.startswith('From '):
        words = line.split()
        word = words[1]
        counter[word] = counter.get(word, 0) + 1
    else: continue
user = None
times = None
for k,v in counter.items():
    if user == None or v > times:
        user = k
        times = v
print(user,times)





