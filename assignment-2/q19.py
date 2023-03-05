# 9.  Encrypt a string using the shift cipher( key=3 Ceaser cipher)
message = input("Enter message to encrypt: ")
encrypted_message = ""
for char in message:

    if char.isupper():
        encrypted_message += chr((ord(char) + 3 - 65) % 26 + 65)
    elif char.islower():
        encrypted_message += chr((ord(char) + 3 - 97) % 26 + 97)
    else:
        encrypted_message += char
print("Encrypted message:", encrypted_message)
