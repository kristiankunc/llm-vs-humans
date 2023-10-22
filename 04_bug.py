# Description: A function that verifies a credit card number using the Luhn's algorithm (https://en.wikipedia.org/wiki/Luhn_algorithm). Currently, it does not work correctly. Fix the bug(s) so that it works correctly. You can use the tests to check if it works correctly.
def verify_card(card_number: str) -> bool:
    card_number = ''.join(filter(str.isdigit, card_number))

    if len(card_number) < 13 or len(card_number) > 19:
        return False

    card_number = card_number[:-1]

    total = 0
    double_digit = False

    for i, digit in enumerate(card_number):
        digit = int(digit)

        if double_digit:
            digit *= 2
            if digit > 9:
                digit -= 9

        total += digit
        double_digit = not double_digit

    return total % 10 == 0


# Tests
# Valid cards
print(verify_card("378282246310005"))  # True
print(verify_card("4222222222222"))  # True

# Invalid cards
print(verify_card("378282246310006"))  # False
print(verify_card("4222222222223"))  # False
