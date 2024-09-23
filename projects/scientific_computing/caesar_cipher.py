class CaesarCipher:
    def __init__(self, shift: int):
        self.shift = shift % 26
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    
    def _transform_text(self, text: str, direction: int = 1) -> str:
        transformed_text = ''
        for char in text.upper():
            if not char.isalpha():
                transformed_text += char
            else:
                index = reference.find(char)
                new_index = (index + self.shift * direction) % len(reference)
                transformed_text += self.alphabet[new_index]
        return transformed_text

    
    def encrypt(self, original_text: str) -> str:
        return self._transform_text(original_text)


    def decrypt(self, encrypted_text: str) -> str:
        return self._transform_text(encrypted_text, -1)


def main():
    print("Caesar Cipher:\n")
    while True:
        try:
            shift = int(input("Enter shift value: "))
            break
        except ValueError:
            print("Invalid Input")
    cipher = CaesarCipher(shift)
    choice =  input("Do you want to:\n1. Encrypt\n2. Decrypt\n=> ")
    while True:
        if choice == '1':
            text = input("Type the message you want to encrypt:\n=> ")
            print("Encrypted Text: " + cipher.encrypt(text))
            break
        elif choice == '2':
            text = input("Type the message you want to decrypt:\n=> ")
            print("Encrypted Text: " + cipher.decrypt(text))
            break
        else:
            print("Out of range.")
            continue

if __name__ == "__main__":
    main()