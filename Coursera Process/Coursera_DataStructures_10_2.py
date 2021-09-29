handle = open("mbox-short.txt")
dic = {}
for line in handle:
    if "From " in line:
        whtspcslc = line.split()
        clnslc = whtspcslc[5].split(":")
        dic[clnslc[0]] = dic.get(clnslc[0],0)+1
    else: continue

lst = sorted(dic.items())
for x,y in lst:
    print(x,y)
