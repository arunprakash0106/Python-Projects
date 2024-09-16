a=input("Enter the range of numbers by comma starting number,ending number ")
b=a.split(",")
starting_number=int(b[0])
ending_number=int(b[1])
for i in range(starting_number,ending_number):
    if i%3==0 and i%5==0:
        print("fizzbuzz")
    elif i%3==0:
        print("fizz")
    elif i%5==0:
        print("buzz")
    else:
        print(i)