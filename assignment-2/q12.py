#2.  Write a program to check whether the given string is palindrome or not .
string = input("Enter a string: ")
rev_string = string[::-1]
if string == rev_string:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
