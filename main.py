##Matthew James Resendez
##1431242
word = input()
norm = ""
mirr = ""
for letter in word.lower():
    if letter != ' ':
        norm += letter
        mirr = letter + mirr
if norm == mirr:
    print(word + " is a palindrome")
else:
    print(word + " is not a palindrome")