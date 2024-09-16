a=float(input("Entre the weight in kg"))
b=float(input("Entre the height in cm"))
c=input("Entre the Gender male or female")
d=b/100
BMI=round(a/d**2,2)
if c=='male':
    if BMI<18.5:
        print(f"your BMI is {BMI} kg/mm2 and you are under weight")
    elif BMI<=24.9:
        print(f"your BMI is {BMI} kg/mm2 and you are normal")
    elif BMI<=29:
        print(f"your BMI is {BMI} kg/mm2 and you are over weight")
    elif BMI>=29.1:
        print(f"your BMI is {BMI} kg/mm2 and you are obese")
else:
    if BMI < 18.5:
        print(f"your BMI is {BMI} kg/mm2 and you are under weight")
    elif BMI <= 22:
        print(f"your BMI is {BMI} kg/mm2 and you are normal")
    elif BMI <= 28:
        print(f"your BMI is {BMI} kg/mm2 and you are over weight")
    elif BMI >= 28.1:
        print(f"your BMI is {BMI} kg/mm2 and you are obese")
