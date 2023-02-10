"""Build  a program to:
a. read an integer number from the user. isinstance(x, int)
    123/10 = 12
    12/10 = 1
    1/10 = 0  
b. repeat the following until the number is 0.
c. shift it to the right and print it."""
10, 000, 000, 000


def int_right_shift():
    # a loop keeps prompt user to input an integer number
    while True:
        user_enter = input("Please enter a integer number:")
        # check if the user entered a valid integer
        if user_enter.isdigit() or (user_enter[0] in ["+", "-"] and user_enter[1:].isdigit()):
            number = int(user_enter)
            break  # break from the loop if user enter an integer
        else:
            print(
                "{} is not an integer. The right shift can't be processed.".format(user_enter))

    if number == 0:
        print("you input is: {} the right shift is not processed.".format(number))
    elif number > 0:
        print("you input is: {} the right shift is processing:".format(number))
        while number != 0:
            number //= 10  # right shift processing
            print(number)
    else:
        print("you input is: {} the right shift is processing:".format(number))
        number *= -1  # get absolute value from the negative integer
        while number != 0:
            number //= 10
            print(-1*number)  # reflecting the negative value


if __name__ == '__main__':
    int_right_shift()
