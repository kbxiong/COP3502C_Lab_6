# Kang Xiong
# COP3502C: Lab 6

# encoding password - Kang has to do this
def encode(num):
    new_password = ''

    # adding 3 to each digit for new password
    for i in num:
        # converting the digit and adding 3, mod by 10 if it's 7+ to keep the ones place
        new_num = (int(i) + 3) % 10

        # add the result to the new string to output the new string combo
        new_password += str(new_num)

    return new_password


# decoded password - Saher Alwani
def decode(password):
    decoded = ""

    for i in password:
        decoded += str((int(i) + 10 - 3) % 10)  # Add 10, subtract 3, and keep the last number

    return decoded


# main function
def main():
    # encoded password
    temp_pass = ''
    # display the menu
    while True:
        print('Menu')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')
        print()
        # user select an option
        option = int(input('Please enter an option: '))

        # encode or decode based on option
        if option == 1:
            # take user input as a string
            pass_num = input('Please enter your password to encode: ')

            # check to make sure it's 8 digits only and is all digits and not letter
            while len(pass_num) != 8 or (not pass_num.isdigit()):
                pass_num = input('Please enter a 8-digit password: ')

            temp_pass = encode(pass_num)

            # print out the new password
            print('Your password has been encoded and stored!')
            print()
        elif option == 2:
            # decode the encoded password and print out original password
            decoded_num = decode(pass_num)
            print(f'The encoded password is {temp_pass}, and the original password is {decoded_num}.')
            print()
            print(decoded_num)
        elif option == 3:
            break
        else:
            print('Please enter an option from 1-3')
            print()


if __name__ == '__main__':
    main()
