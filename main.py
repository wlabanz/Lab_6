# Will Labanz - encoder and main function
newPassword = ''
userOption = 0
passwordInput = ''

def encode(integer_string):
    encodedPassword = ''
    for i in integer_string:
        new_digit = int(i) + 3
        if new_digit > 9:
            new_digit = new_digit % 10
            encodedPassword = encodedPassword + str(new_digit)
        else:
            encodedPassword = encodedPassword + str(new_digit)
    return encodedPassword

def decode(password):
    

if __name__ == '__main__':
    while userOption != 3:
        print("Menu", "-" * 13, "1. Encode", "2. Decode", "3. Quit\n", sep='\n')
        userOption = int(input("Please enter an option:"))
        if userOption == 1:
            passwordInput = input("Please enter your password to encode:")
            newPassword = encode(passwordInput)
            print("Your password has been encoded and stored!\n")
        elif userOption == 2:
            print("The encoded password is ", newPassword, ", and the original password is ", decode(newPassword), ".")
