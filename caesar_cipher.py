# Percorre o texte, e através de cada letra vai constroindo o texto encriptado 
# A formula de encriptação é: encrypt(letter, n) = (letter + n)mod 26
def encrypt(text, rotation):
    message = ''

    for character in text:
        # Codifica os caracteres maiusculos
        # 65 é o codigo ASCII do caracter 'A' 
        if character.isupper(): 
            message += chr((((ord(character) - 65) + rotation) % 26) + 65) 
  
        # Codifica os caracteres minusculos
        # 97 é o codigo ASCII do caracter 'a'
        else: 
            message += chr((((ord(character) - 97) + rotation) % 26) + 97) 

    return message

# Percorre o texte, e através de cada letra vai constroindo o texto descriptografado
# A formula de descriptação é: decrypt(letter, n) = (letter - n)mod 26
def decrypt(text, rotation):
    message = ''

    for character in text:
        # Codifica os caracteres maiusculos
        # 65 é o codigo ASCII do caracter 'A' 
        if character.isupper(): 
            message += chr((((ord(character) - 65) + rotation) % 26) + 65) 
  
        # Codifica os caracteres minusculos
        # 97 é o codigo ASCII do caracter 'a'
        else: 
            message += chr((((ord(character) - 97) - rotation) % 26) + 97) 

    return message

print('***** CEASAR CIPHER *****')
text = input()
option = input('Do you want to encrypt or decrypt the text? (E/D) -> ')

# ord('x') dá o codigo ASCII do caracter 'x'
if ord(option) == 69:
    rotation = int(input('What rotation do you want? '))
    encryptedText = encrypt(text, rotation)

    print(encodedText)
elif ord(option) == 68:
    rotation = int(input('What rotation do you want? '))
    decryptedText = decrypt(text, rotation)

    print(decryptedText)
else:
    print('You did not chose any of the option sorry!! :(')