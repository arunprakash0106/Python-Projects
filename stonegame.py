a="✊"
b="🖐️"
c="✂"
images=[a,b,c]
user_choise=int(input("Entre your choise: For Stone entre 0,For Paper entre 1,for Scissor entre 2 "))
print(images[user_choise])
import random
computer_choise=random.randint(0,2)
print(images[computer_choise])
if user_choise==computer_choise:
    print("The match is draw")
elif user_choise==2 and computer_choise==0:
    print("you Lose")
elif user_choise==0 and computer_choise==2:
    print("you Win")
elif user_choise>computer_choise:
    print("you Win")
elif computer_choise>user_choise:
    print("you Lose")