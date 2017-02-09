print("Datatypes")
print("Lists")
listy=["first",2,3.0]
print(listy[0])

listy.append(3.142)
print(listy)

listy.remove(3.0)
print(listy)

print("tuples")
tp=("x","y","z")
print(tp)
print(type(tp))

print("Dictionaries")
dicy={"Name":"Mukesh","age":29,"Height":5.7}
print(dicy)
print(dicy["Name"])
print(dicy.values())
print(type(dicy.values()))
lisy=list(dicy.values())
print(lisy)

money={"saving_account":200, "checking_account":100, "under_bed":[500,10,100]}
k=money["under_bed"][1]
print(k)