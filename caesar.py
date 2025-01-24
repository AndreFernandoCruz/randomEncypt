print('Digite um texto para criptografar')
text = input()
shift = 3

def caesar(text, shift):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''
    message = text
    offset = shift

    for char in message.lower():
        if char == ' ':
            encrypted_text += char
        else:
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]
    print('texto digitado:', message)
    print("texto encripitado:", encrypted_text)
caesar(text, shift)