# 5.  Read a decimal number and find its binary.( Hint: divide by 2 and append the reminder to a string)
dec_num = int(input("Enter a decimal number: "))
bin_num = ""
while dec_num > 0:
    bin_num = str(dec_num % 2) + bin_num
    dec_num //= 2

print("Binary representation:", bin_num)
