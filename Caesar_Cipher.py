method = input('Do you want to encrypt or decrypt the text? (Enter "encrypt" or "decrypt"): ').strip().lower()
text = input('Enter the text : ')
shift = input('Enter the shift value (1-25): ')

def caesar(text, shift, encrypt=True):
    
    if not isinstance(text, str):
        return 'Text must be a string.'

    if not isinstance(shift, int):
        return 'Shift must be an integer value.'

    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if not encrypt:
        shift = - shift
    
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    encrypted_text = text.translate(translation_table)
    return encrypted_text

def encrypt(text, shift):
    return caesar(text, shift)
    
def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)

if method == 'encrypt':
    encrypted_text = encrypt(text, int(shift))
    print('Encrypted text:', encrypted_text)

elif method == 'decrypt':
    decrypted_text = decrypt(text, int(shift))
    print('Decrypted text:', decrypted_text)

else:
    print('Invalid method. Please enter "encrypt" or "decrypt".')
