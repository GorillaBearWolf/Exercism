def steps(number):
    i = 0
    while number != 1:
        if number < 1:
            raise ValueError("Only positive integers are allowed")
        elif number % 2 == 0:
            number = number / 2
            i += 1
        elif number % 2 != 0:
            number = (number * 3) + 1
            i += 1
    return i
