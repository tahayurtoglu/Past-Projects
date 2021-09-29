fname = input("Enter file name: ")
fh = open(fname)
all_num = 0
c = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    ind = -1
    for index in line:
        ind = ind + 1
        if index == ":":
            c = c+1
            ar_ind=ind
            #print()
            num = float(line[ar_ind+1:])
            all_num = all_num + num

print("Average spam confidence:",all_num/c)