def get_valid_amount_atm_feedback():

    flag = True
    result = 0

    while flag:
        user_input = int(input('Enter an amount multiple of 10 and greater than 30: '))

        if (user_input % 10 != 0) and (user_input < 30):
            print('Your amount is not a multiple of 10 and is less or equal to 30.')
            flag = True

        elif user_input % 10 != 0:
            print('Your amount is not a multiple of 10.')
            flag = True

        elif user_input <= 30:
            print('Your amount is less or equal to 30.')
            flag = True

        else:
            flag = False
            result = user_input

    return result


def main():
    amount = get_valid_amount_atm_feedback()
    print("Thanks, you withdrew $" + str(amount))


main()
