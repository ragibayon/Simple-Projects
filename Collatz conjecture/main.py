def collatz_sequence(number):
    """"Returns Collatz Sequence"""
    yield number
    while number != 1:
        # Check if the number is even
        if number % 2 == 0:
            number = number // 2
            yield number
        # Check if the number is odd
        elif number % 2 != 0:
            number = 3 * number + 1
            yield number


if __name__ == '__main__':
    while True:
        try:
            input_number = int(input('Input Number: '))
            head, *tail = collatz_sequence(input_number)
            print(f'Your input Number is: {head} \nThe Collatz conjecture is:', *tail)
            print('For more details visit: https://en.wikipedia.org/wiki/Collatz_conjecture')
            break
        except ValueError:
            print('Error! Please insert an integer')
            continue
