def fibonacciDPBottomUpSpaceOptimized(n):
    if (n == 0 or n == 1): return n
    f1 = 0; f2 = 1
    for i in range(2, n + 1):
        f3 = f1 + f2
        f1 = f2
        f2 = f3
    return f3
n = int(input("Please enter the value for n:"))
print(fibonacciDPBottomUpSpaceOptimized(n))