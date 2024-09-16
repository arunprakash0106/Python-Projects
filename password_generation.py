letters=["a","b","c","d","e","f","g","h","i","j","k","l",
         "n","o","p","q","r","s","t","u","v","w","x","y","z",
         "A","B","C","D","E","F","G","H","I","J","K","L",
         "M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
numbers=["0","1","2","3","4","5","6","7","8","9"]
symbols=["!","@","#","$","%","^","&","*","(",")","+","="]
import random
captcha=""
a=letters+numbers+symbols
digits=int(input("enter the number of digits in captcha "))
for i in range(digits):
    c=random.choice(a)
    captcha=c+captcha
print(captcha)

