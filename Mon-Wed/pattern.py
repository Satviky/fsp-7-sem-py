n = int(input("Please enter the ODD integer for layer count: "))
m = (n + 1) // 2

print("." * m + "*")

for i in range(1, n + 1):
    if (i <= m): b = (m - i); s = (2 * i - 1)
    else: b = (i - m); s = (2 * (n - i) + 1)
    print("." * b + "*" + "." * s + "*")
    
print("." * m + "*")
print("End of the pattern...")


