print("Write method")
file=open("sample.txt",'w')
lo=["kiran","raju","krishna"]
for item in lo:
    file.write(item+"\n")
file.close()

print("Append method")
file=open("sample.txt",'a')
file.write("cse")
file.close()