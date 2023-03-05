#6.  Read an 8 bit binary number and print the hex equivalent
bin_num = input("Enter an 8-bit binary number: ")
bin_num = bin_num.zfill(8)
hex_num = hex(int(bin_num, 2))[2:]
print("Hexadecimal equivalent:", hex_num.upper())
