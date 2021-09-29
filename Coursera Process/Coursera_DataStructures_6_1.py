y=0
while  True:
    y= y+1
    str = input("Enter a number:")
    if str == "done":
        break
    try:
        flo = int(str)
    except:
        print("Invalid input")
        continue
    if y==1:
        larv = flo
        smav = flo
    if flo > larv:
        larv=flo
    if flo < smav:
        smav=flo
print("Maximum is",larv)
print("Minimum is",smav)