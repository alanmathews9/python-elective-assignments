#to check if a number is a power of 2
def is_power_of_two(n):
    if n <= 0:
        return False
    return n & (n - 1) == 0


n = int(input("Enter a number: "))
if is_power_of_two(n):
    print(n, "is a power of 2")
else:
    print(n, "is not a power of 2")
