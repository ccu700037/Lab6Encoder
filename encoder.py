# Sharanya's Code


def main():
    curr_password = ''
    while True:

        # Print menu
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print()

        choice = input("Please enter an option: ")

        if choice == "1":
            original = input("Please enter your password to encode: ")

            # encode password entered by user and print message
            curr_password = encode(original)
            print("Your password has been encoded and stored!")
            print()
        elif choice == "2":
            encoded = curr_password

            # decode password and print encoded + decoded version
            curr_password = decode(curr_password)
            print(f"The encoded password is {encoded}, and the original password is {curr_password}")
            print()
        else:
            # exit program
            break


def encode(original):
    ans = ""

    # add 3 to every digit and mod it by 10
    for char in original:
        ans += str((int(char) + 3) % 10)

    return ans


def decode(password):
    password_string = password
    decoded_password_string = ''
    for i in password_string:
        decoded_value = int(i) - 3
        if decoded_value < 0:
            decoded_value += 10
        decoded_password_string += str(decoded_value)
    decoded_password = decoded_password_string
    return decoded_password


if __name__ == "__main__":
    main()
