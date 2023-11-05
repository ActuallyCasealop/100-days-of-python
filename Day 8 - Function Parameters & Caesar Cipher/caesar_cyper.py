alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

print(len(alphabet))

def encrypt(text, shift):
    encrypted_text = ""
    for i in text:
        if alphabet.index(i) + shift > 25:
            encrypted_text += alphabet[(alphabet.index(i) + shift) - 26]
        else:
            encrypted_text += alphabet[alphabet.index(i) + shift]

    return print(encrypted_text)

def decrypt(text, shift):
    decrypted_text = ""
    for i in text:
        if (alphabet.index(i) - shift) < 0:
            decrypted_text += alphabet[(alphabet.index(i) - shift) + 26]
        else:
            decrypted_text += alphabet[alphabet.index(i) - shift]
    return print(decrypted_text)

if direction == 'encode':
    encrypt(text, shift)
else:
    decrypt(text, shift)