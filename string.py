string_name = input("ENTER A WORD :    ")
if string_name == string_name[::-1]:
    print("The word is a palindrome.")
else:
    print("The word is not a palindrome.")