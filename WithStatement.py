print("using with closing of file is not necessary at the end of code for file handling")
with open("sample.txt","a+") as file:
    file.write("\n1bg13cs042")
    contents=file.read()
    print(contents)