letters=["a","b","c","d","e","f","g","h","i","j","k","l",
         "n","o","p","q","r","s","t","u","v","w","x","y","z"]
def encryption(plain_text,shift_key):
    ciper_text=""
    for char in plain_text:
        if char in letters:
            position=letters.index(char)
            new_position=(position+shift_key)%26
            ciper_text +=letters[new_position]
        else:
            ciper_text += char
    print(ciper_text)

def decryption(plain_text,shift_key):
    new_text=""
    for char in plain_text:
        if char in letters:
            position=letters.index(char)
            new_position=(position-shift_key)%26
            new_text +=letters[new_position]
        else:
            new_text += char
    print(new_text)
to_end=False
while not to_end:
    what_to_do=input("type 'encrypt' for encryption and 'decrypt' for decryption\n")
    text=input("type your message:\n")
    shift=int(input("enter the shift key number:\n"))
    if what_to_do=="encrypt":
        encryption(plain_text=text,shift_key=shift)
    elif what_to_do=="decrypt":
       decryption(text,shift)
    play_again=input("enter 'yes' for continue and 'no' for discontinue:\n")
    if play_again=='no':
        to_end=True
        print("have a nice day")
