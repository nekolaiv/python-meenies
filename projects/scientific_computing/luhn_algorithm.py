class LuhnAlgorithm:
   
    def _filter_card_number(self, card_number: str) -> str:
        filtered_characters: str = str.maketrans({'-': '', ' ': ''})
        filtered_card_number: str = card_number.translate(filtered_characters)
        return filtered_card_number


    def _reverse_card_number(self, filtered_card_number: str) -> str:
        reversed_card_number: str = filtered_card_number[::-1]
        return reversed_card_number


    def _get_odd_and_even_digits(self, reversed_card_number: str) -> tuple(str, str):
        odd_digits: str = reversed_card_number[::2]
        even_digits: str = reversed_card_number[1::2]
        return odd_digits, even_digits


    def verify_card_number(self, card_number: str) -> bool:
        sum_of_odd_digits: int = 0
        sum_of_even_digits: int = 0
        filtered_card_number: str = self._filter_card_number(card_number)
        reversed_card_number: str = self._reverse_card_number(filtered_card_number)
        odd_digits, even_digits = self._get_odd_and_even_digits(reversed_card_number)

        for digit in odd_digits:
            sum_of_odd_digits += int(digit)

        for digit in even_digits:
            number: int = int(digit) * 2
            if number >= 10:
                number: int = (number // 10) + (number % 10)
            sum_of_even_digits += number
        total: int = sum_of_even_digits + sum_of_odd_digits
        return total % 10 == 0


def get_user_card_number() -> str:
    card_number: str = input('Enter your card number to verify: ')
    return card_number


if __name__ == '__main__':
    luhnAlgorithm: LuhnAlgorithm = LuhnAlgorithm()
    print("Luhn Algorithm:\n")
    card_number: str = get_user_card_number()
    result: bool = luhnAlgorithm.verify_card_number(card_number)
    print(f"Result: {result}")