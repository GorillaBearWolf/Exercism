def is_armstrong_number(number):
    str_number = str(number)
    exponent = len(str_number)
    total = 0
    for digit in str_number:
        total += int(digit) ** exponent
    return total == number
