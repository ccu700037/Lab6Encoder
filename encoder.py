# Sharanya's Code


def main():
    while True:

        # Print menu
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print()

        choice = input("Please enter an option: ")

        curr_password = ""

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
    pass


if __name__ == "__main__":
    main()
