import os
import sys

print('Escolha uma criptografia: ')
print('1:caesar, 2:vigenere')
print('ou pressione Q para sair')

def exit():
    sys.exit

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
    #print('texto digitado:', message)
    print("texto encripitado:", encrypted_text)

def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():

        # Append any non-letter character to the message
        if not char.isalpha():
            final_message += char
        else:        
            # Find the right key character to encode/decode
            key_char = key[key_index % len(key)]
            key_index += 1

            # Define the offset and the encrypted/decrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset*direction) % len(alphabet)
            final_message += alphabet[new_index]
    
    return final_message

escolha = input('').lstrip(' 0').lower()

if escolha == '1':
    print('Digite um texto para criptografar')
    text = input()
    print('Digite a palavra chave:')
    custom_key = input()
    encryption = vigenere(text, custom_key)
    print(encryption)
if escolha == '2':
    print('Digite um texto para criptografar')
    text = input()
    shift = 3
    caesar(text, shift)
if escolha == 'Q':
    input('Saindo pressione qualquer tecla')
    exit()
