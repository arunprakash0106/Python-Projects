import random

a=input("enter the names in a team ")
b=a.split(",")
length=len(b)
choise=random.randint(0,length-1)
print(b[choise])
