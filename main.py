# Name: Finn Walker

def encode_password(password):
    output = ""
    for digit in password:
        digit = int(digit) + 3
        if digit < 10:
            output += str(digit)
        else:
            output += str(digit - 10)
    return output

def decode_password(password):
    output = ""
    for digit in password:
        digit = int(digit) - 3
        if digit < 0:
            output += str(digit + 10)
        else:
            output += str(digit)
    return output

# main loop
while True:
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print()
    user_input = input("Please enter an option: ")

    match user_input:
        case "1":  # encode
            password = input("Please enter your password to encode: ")
            encoded_password = encode_password(password)
            print("Your password has been encoded and stored!\n")
        case "2":  # decode
            print(f"The encoded password is {encoded_password}, and the original password is {decode_password(encoded_password)}.\n")
        case "3":  # quit
            break
        case _:  # invalid input
            print("Invalid input!\n")
            continue