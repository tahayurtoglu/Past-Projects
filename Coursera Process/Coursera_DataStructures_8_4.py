fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    striped_l = line.rstrip()
    li_striped_l = striped_l.split()
    for word in li_striped_l:
        print(word)
        if word not in lst:
            lst.append(word)
        else:
            continue
lst.sort()
print(lst)
