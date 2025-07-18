# n = 9 (ODD integer, user given)

#      1  2  3  4  5  6  7  8  9
# --------------------------------
# 1 |  1  1  1  1  1  1  1  1  1
# 2 |  1  2  2  2  2  2  2  2  1
# 3 |  1  2  3  3  3  3  3  2  1
# 4 |  1  2  3  4  4  4  3  2  1
# 5 |  1  2  3  4  5  4  3  2  1
# 6 |  1  2  3  4  4  4  3  2  1
# 7 |  1  2  3  3  3  3  3  2  1
# 8 |  1  2  2  2  2  2  2  2  1
# 9 |  1  1  1  1  1  1  1  1  1
# --------------------------------


while(True):
    n = int(input("Please enter the number of layers: "))
    if (n % 2 == 1): break
m = (n + 1) // 2
for i in range(1, n + 1):
    term = 1
    if (i <= m): ll = i; ul = (n - i + 1)
    else: ll = (n - i + 1); ul = i
    for j in range(1, n + 1):
        print("%4d"%term, end = "")
        if (j < ll): term = term + 1
        elif (j >= ul): term = term - 1
    print()
print("End of the pattern printing...")