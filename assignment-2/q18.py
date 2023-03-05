# 8.  Read a string and swap the case ( small lettesr to capital letters and capital letters to small letters)
string = input("Enter a string: ")
swapped_case = ""
for char in string:
    if char.isupper():
        swapped_case += char.lower()
    elif char.islower():
        swapped_case += char.upper()
    else:
        swapped_case += char
print("Swapped case string:", swapped_case)
