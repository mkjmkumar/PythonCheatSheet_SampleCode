names=["Mukesh","COMP"]
for item in names:
    if 'COMP' in item:
        print(item)

password=''
while password!='passcode':
    password=input("Enter given passscode: ")
    if password == 'passcode':
        print("correct passcode")
    else:
        print("try again")

namez=['cool','hot','moderate']
food=['drink','tea','heat']
for i,j in zip(namez,food):
    print(i+' '+'mast'+' '+j)

print("User Input")
def cal(a,b):
    c=a*b+10
    print(c)
x=input("Enter 1st number: ")
y=input("Enter 2nd number: ")
cal(int(x),int(y))
cal(x,y)