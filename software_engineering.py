def encode(password):   # adds 3 to each number in password
    result = ''
    for element in password:
        element = str(int(element) + 3)
        result += element

    return result


def decode():
    pass


def print_menu():
    print()
    print('Menu\n'
          '------------\n'
          '1. Encode\n'
          '2. Decode\n'
          '3. Quit\n')


def main():
    program_continue = True

    while program_continue:
        print_menu()
        option = int(input('Please enter an option: '))

        # encodes password
        if option == 1:
            password = (input('Please enter your password to encode: '))
            encode(password)
            print('Your password has been encoded and stored!')

        # decodes password
        elif option == 2:
            pass

        # quits program
        elif option == 3:
            break


if __name__ == '__main__':
    main()

