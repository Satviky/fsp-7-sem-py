while(True):
    n = int(input("Please enter the number of layers: "))
    if (n % 2 == 1): break
matrix = [[0 for _ in range(n)] for _ in range(n)]
# print(matrix)
print("Filling up the matrix...")
row = 0; col = n // 2
for value in range(1, n*n + 1):
    matrix[row][col] = value
    row -= 1; col += 1
    if (row == -1 and col == n): row += 2; col -= 1  # corner logic
    elif (col == n): col = 0                         # col-wise folding
    elif (row == -1): row = (n - 1)                  # row-wise folding
    elif (matrix[row][col] != 0): row += 2; col -= 1 # Pre-occupied
print("Printing up the matrix...")
for row in range(n):
    for col in range(n):
        print("%4d"%matrix[row][col], end = "")
    print()
print("End of the program...")