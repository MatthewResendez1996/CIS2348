##Matthew James Resendez
##1431242
word = input()
password = ''
for letter in word:
    if (letter == 'i'):
        password += "!"

    elif (letter == 'a'):
        password += "@"

    elif (letter == 'm'):
        password += "M"

    elif (letter == 'B'):
        password += "8"

    elif (letter == 'o'):
        password += "."

    else:
        password += letter
password += "q*s"
print(password)