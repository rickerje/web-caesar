import string

def alphabet_position(letter):
    
    alphabet = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 
        'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8,
        'j': 9, 'k': 10, 'l': 11, 'm': 12,  
        'n': 13, 'o': 14, 'p': 15, 'q': 16, 
        'r': 17, 's': 18, 't': 19, 'u': 20, 
        'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}

    return alphabet.get(letter.lower())

def rotate_character(char, rot):

    alphabet = string.ascii_lowercase
    
    if not char.isalpha():
        return char
    
    char_value = alphabet_position(char)

    char_pos = char_value + rot
    if char_pos < 25:
        new_char = alphabet[char_pos]
    else:
        new_char = alphabet[char_pos % 26]

    if char.isupper():
        return new_char.upper()
    else:
        return new_char


def encrypt(text, rot):
    encrypted_msg = ''
    
    for char in text:
        encrypted_msg = encrypted_msg + rotate_character(char, rot)
    
    return encrypted_msg

def main():
    message = input("Enter your message to encrypt: ")
    rotation = int(input("Enter the character rotation for encrypting: "))
    
    print(encrypt(message, rotation))

if __name__ == "__main__":
    main()