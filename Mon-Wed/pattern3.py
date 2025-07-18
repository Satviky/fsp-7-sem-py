while(True):
    n = int(input("Please enter the ODD integer for layer count: "))
    if (n % 2 == 1): break
m = (n + 1) // 2
for i in range(1, n + 1):
    if (i <= m): b = (i - 1); ch = (2 * (m - i) + 1)
    else: b = (n - i); ch = (2 * (i - m) + 1)
    print("." * b + chr(64 + i) * ch)
print("End of the pattern...")