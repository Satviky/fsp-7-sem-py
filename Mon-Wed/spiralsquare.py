# Fill up a marix with dimension nxn (where is a user given integer number) with numbers ranging from 1 to n^2.
# Use these numbers once in a clockwise spiral fashion starting from top-left corner.

# n = 5 (user given integer)

#      0   1   2   3   4
# ------------------------
# 0 |  1   2   3   4   5
# 1 |  16  17  18  19  6
# 2 |  15  24  25  20  7
# 3 |  14  23  22  21  8
# 4 |  13  12  11  10  9
# ------------------------

while(True):
    n = int(input("Please enter the number of layers: "))
    if (n % 2 == 1): break
matrix = [[0 for _ in range(n)] for _ in range(n)]

print("Filling up the matrix...")
row = 0; col = 0
for value in range(1, n*n + 1):
    matrix[row][col] = value
    col += 1
    if (col == n): row+=1; col=0
    elif (row == n): col-=1
    elif (row== -1): row-=1
    elif (matrix[row][col] != 0): col += 1

print("Printing the matrix...")
for row in range(n):
    for col in range(n):
        print("%4d"%matrix[row][col], end = "")
    print()
print("End of the program...")