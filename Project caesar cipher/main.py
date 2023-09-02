alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
'o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n',
'o','p','q','r','s','t','u','v','w','x','y','z']

#Combine encrypt() and Decrypt() function in one caesar() function

def caesar(start_text,shift_amount,cipher_direction):
    
    end_text = ""
    if cipher_direction == 'decode':
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"Here`s the {direction}d result :{end_text}")

from art import logo
print(logo)

while True:
        direction = input("Type ('encode') to encript, type ('decode') to decrypt:\n")

        text = input("Type your message:\n").lower()
        shift = int(input("Type the shifting number:\n"))
        shift = shift % 26

        caesar(start_text = text, shift_amount = shift, cipher_direction = direction)
    
        option = input("Type 'yes' if you want to go again .Otherwise type 'no'")
        if option == 'no':
            print('Googbye')
            break

# That is indvidual code for encode() and decode() funstion


# def encript(plain_text,shift_amount):
#     chiper_text = ""
#     for letter in plain_text: 
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         new_letter = alphabet[new_position]
#         chiper_text += new_letter
#     print(f"The encoded text is :{chiper_text}")


# def decrypt(chiper_text, shift_amount):
#     plain_text = ""
#     for letter in chiper_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         new_letter = alphabet[new_position]
#         plain_text  += new_letter
#     print(f"The decoded text is : {plain_text}")

# if direction == 'encode':
#     encript(plain_text = text, shift_amount = shift)

# elif direction == 'decode':
#     decrypt(chiper_text = text, shift_amount = shift)
