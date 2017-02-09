newfile=open("text1.txt",'r')
print(type(newfile))

contents=newfile.read()
print(contents)
print(type(contents))

print("to get the contents as a list")
contents1=newfile.readlines()
print(contents1)

print("it prints an empty list, as the cursor is at the end of all lines. pointer should be moved back")
newfile.seek(0)
contents1=newfile.readlines()
print(contents1)

print("to print without newlines  included in the list")
contents2=[i.rstrip("\n") for i in contents1]
print(contents2)
newfile.close()