# 4.  Read a binary number as a string and find its corresponding decimal
bin_num = input("Enter a binary number: ")

dec_num = 0

for i in range(len(bin_num)):
    dec_num += int(bin_num[i]) * 2 ** (len(bin_num) - i - 1)

print("Decimal equivalent:", dec_num)
