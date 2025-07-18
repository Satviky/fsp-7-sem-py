# Problem on "Power of Two"
# Given an integer number n, write a function to determine if it is a power of two or not.

# Example:
# * if n = 16, output = True
# * if n = 64, output = True
# * if n = 60, output = False


n=int(input("Enter: "))
l=n-1
if n & (n-1) == 0: print("True")
else: print("false")
