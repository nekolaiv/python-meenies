class VigenereCipher:
    def __init__(self):
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


    def _transform_text(self, text: str, key: str, direction: int = 1) -> str:
        key_index = 0
        transformed_text = ''
        for text_character in text.upper():
            if not text_character.isalpha():
                transformed_text += text_character
            else:
                key_character = key[key_index % len(key)].upper()
                key_index += 1
                offset = self.alphabet.index(key_character)
                index = self.alphabet.index(text_character)
                new_index = (index + offset * direction) % len(self.alphabet)
                transformed_text += self.alphabet[new_index]
        return transformed_text


    def encrypt_text(self, original_text: str, key: str) -> str:
        return self._transform_text(original_text, key)


    def decrypt_text(self, encrypted_text: str, key: str) -> str:
        return self._transform_text(encrypted_text, key, -1)


    @staticmethod
    def get_user_text_and_key() -> str:
        user_text = input("Text: ")
        user_key = input("Key: ")
        print(user_text, user_key)
        return user_text, user_key

    
    def run(self) -> None:
        print("Vigenere Cipher:\n\n1. Encrypt\n2. Decrypt")
        while True:
            try:
                user_choice = int(input("=> "))
                if user_choice not in(1, 2):
                    continue
                break
            except ValueError:
                print("Invalid Input!")
        user_text, user_key = self.get_user_text_and_key()
        if user_choice == 1:
            print(f'Encrypted Text: {self.encrypt_text(user_text, user_key)}')
        elif user_choice == 2:
            print(f'Decrypted Text: {self.decrypt_text(user_text, user_key)}')


if __name__ == '__main__':
    cipher = VigenereCipher()
    cipher.run()