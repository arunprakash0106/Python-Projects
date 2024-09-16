import random
import hang_doll
word_list=("arun","ramya","mouni","dora","kavitha","yasmitha")
chosen_word=random.choice(word_list)
display=[]
for i in range(len(chosen_word)):
    display+="_"
print(display)
game_over=False
lives=6
while not game_over:
    gussed_letter=input("Guss the letter in the word ").lower()
    for position in range(len(chosen_word)):
        letter=chosen_word[position]
        if letter==gussed_letter:
            display[position]=gussed_letter
    print(display)
    if gussed_letter not in chosen_word:
        lives=lives-1
        print(hang_doll.hangman_doll[lives])
    print("you have remaing"+" "+str(lives)+" "+"lives only")
    if lives==0:
        game_over=True
        print("game over you lose!!")
    if "_" not in display:
        print(" congurlation you win!!")

