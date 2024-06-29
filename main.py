import random


def main():
    """
    ########################################
    Code Your Program here
    ########################################
    """
    numbers = []
    i = 0
    while i < 5:
        numbers.append(random.randint(0,100))
        i += 1
    total = sum(numbers)

    print(f'The random values are {numbers}')
    print(f'The total is {total}')

    ########################################
    # Do not delete the return statement
    ########################################
    return numbers, total


if __name__ == '__main__':
    main()
