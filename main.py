def caesar_cipher(text, shift, direction):
    """
    Encrypts or decrypts text using the Caesar Cipher algorithm.

    :param text: The text to encrypt or decrypt
    :param shift: The shift value (positive for encryption, negative for decryption)
    :param direction: 'encrypt' or 'decrypt'
    :return: The encrypted or decrypted text
    """
    result = ""
    for char in text:
        if char.isalpha():  # only encrypt letters, not spaces or punctuation
            ascii_offset = 65 if char.isupper() else 97  # ASCII offset for uppercase or lowercase letters
            char_code = ord(char) - ascii_offset
            char_code = (char_code + shift) % 26  # perform the shift
            result += chr(char_code + ascii_offset)
        else:
            result += char  # leave non-letter characters unchanged
    return result

def main():
    while True:
        print("Caesar Cipher Program")
        print("---------------------")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Quit")
        choice = input("Choose an option: ")

        if choice == "1":
            text = input("Enter a message to encrypt: ")
            shift = int(input("Enter a shift value: "))
            encrypted_text = caesar_cipher(text, shift, 'encrypt')
            print("Encrypted message:", encrypted_text)
        elif choice == "2":
            text = input("Enter a message to decrypt: ")
            shift = int(input("Enter a shift value: "))
            decrypted_text = caesar_cipher(text, -shift, 'decrypt')  # note the negative shift value
            print("Decrypted message:", decrypted_text)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Try again!")

if __name__ == "__main__":
    main()