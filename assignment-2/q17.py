# 7.  Read a two digit hex number and print the binary and decimal equivalent.
hex_num = input("Enter a two-digit hexadecimal number: ")
dec_num = int(hex_num, 16)
bin_num = bin(dec_num)[2:]
print("Decimal equivalent:", dec_num)
print("Binary equivalent:", bin_num)
